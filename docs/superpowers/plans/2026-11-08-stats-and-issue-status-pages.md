# Statistics Hub (`/stats/`) & Issue Status Page (`/stats/issues/`) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the `/stats/` portal hub and `/stats/issues/` build-time Issue statistics & year×question status explorer page with 100% Open/Closed GitHub Issue accounting and zero client-side API calls.

**Architecture:** Extend `scratch/issue_labels.py`'s `build_index()` to export non-`problem:*` Issues under `unmapped` alongside validated single-problem `problems` in `web/src/data/issues-by-problem.json`. Add a pure aggregation module `web/src/lib/issue-stats.mjs` consumed at Astro build time by `web/src/pages/stats/index.astro` and `web/src/pages/stats/issues.astro`, and expose `/stats/` in `web/src/layouts/Layout.astro`.

**Tech Stack:** Python 3.10+ (`pytest`), Node.js 20/22 (`node:test`), Astro 4 (`^4.11.3`), vanilla CSS & client-side `<script>` (`astro:page-load` ViewTransitions compatible).

## Global Constraints

- Do **NOT** run `git commit` (the repository owner manages commits explicitly).
- Preserve `schema_version: 1` backwards compatibility in `issues-by-problem.json`; `problems` must never guess single-question IDs from Issue titles (`docs/issue-labels.md`).
- Zero client-side GitHub API fetches; read `issues-by-problem.json` at most once per page build and degrade gracefully when the snapshot file is absent locally.
- Respect `import.meta.env.BASE_URL` and `trailingSlash: 'always'` on every internal link.
- Apply `content-visibility: auto` with `contain-intrinsic-size` only to below-the-fold heavy sections, and respect `@media (prefers-reduced-motion: reduce)`.

---

### Task 1: Extend Python Issue Snapshot Export (`unmapped`) & `.gitignore`

**Files:**
- Modify: `.gitignore`
- Modify: `scratch/issue_labels.py:8-19,137-159`
- Modify: `scratch/sync_issue_labels.py:214-218`
- Test: `tests/scratch/test_issue_labels.py`

**Interfaces:**
- Produces: `build_index(issues, repo=DEFAULT_REPO)` returning `{ schema_version: 1, repo, generated_at, problems, unmapped, rejected }` where each `unmapped` item is `{ number, title, state, url, updated_at, kinds, univ, exam }`.

- [ ] **Step 1: Add `.superpowers/` to `.gitignore`**

Append to `.gitignore`:
```gitignore

# Brainstorming visual companion artifacts
.superpowers/
```

- [ ] **Step 2: Write failing pytest tests in `tests/scratch/test_issue_labels.py`**

Append to `tests/scratch/test_issue_labels.py`:
```python
def test_build_index_exports_unmapped_without_guessing_from_title():
    mapped_labels = ['problem:titech/zenki/1985/3', 'univ:titech', 'exam:zenki', 'year:1985', 'kind:proof']
    mapped = issue(number=10, title='[監査] 東工大前期1985-3', labels=mapped_labels)
    cat_wide = dict(
        issue(number=20, title='京大前期のTikZ図改修', body='', labels=['univ:ukyoto', 'exam:zenki', 'kind:figure']),
        state='OPEN',
    )
    general_closed = issue(number=5, title='utokyo zenki: 未移行まとめ', body='', labels=['enhancement'])
    general_open = dict(
        issue(number=30, title='東大前期・後期 PDF整理', body='', labels=['univ:utokyo', 'univ:ukyoto', 'kind:unknown']),
        state='OPEN',
    )

    result = build_index([mapped, general_closed, general_open, cat_wide], 'a/b')

    assert list(result['problems'].keys()) == ['titech/zenki/1985/3']
    assert result['rejected'] == []
    assert [r['number'] for r in result['unmapped']] == [20, 30, 5]
    assert result['unmapped'][0] == dict(
        number=20,
        title='京大前期のTikZ図改修',
        state='open',
        url='https://github.com/a/b/issues/20',
        updated_at='2026-10-21T00:00:00Z',
        kinds=['figure'],
        univ='ukyoto',
        exam='zenki',
    )
    # Multiple conflicting univ labels or unknown kind labels fall back cleanly without guessing from title
    assert result['unmapped'][1]['univ'] is None
    assert result['unmapped'][1]['exam'] is None
    assert result['unmapped'][1]['kinds'] == []
    assert result['unmapped'][2]['state'] == 'closed'
    assert result['unmapped'][2]['univ'] is None
```

- [ ] **Step 3: Run pytest to verify RED**

Run: `python3 -m pytest tests/scratch/test_issue_labels.py -v`
Expected: FAIL with `KeyError: 'unmapped'`.

- [ ] **Step 4: Implement `unmapped` in `scratch/issue_labels.py` and log update in `scratch/sync_issue_labels.py`**

In `scratch/issue_labels.py`, add valid facet sets near `KINDS` and update `build_index`:
```python
VALID_UNIVS = {'utokyo', 'ukyoto', 'titech'}
VALID_EXAMS = {'zenki', 'kouki'}
```
```python
def build_index(issues, repo=DEFAULT_REPO):
    problems, unmapped, rejected = defaultdict(list), [], []
    for issue in issues:
        labels = names(issue)
        if not any(n.startswith('problem:') for n in labels):
            univs = [n[5:] for n in labels if n.startswith('univ:') and n[5:] in VALID_UNIVS]
            exams = [n[5:] for n in labels if n.startswith('exam:') and n[5:] in VALID_EXAMS]
            all_univs = [n for n in labels if n.startswith('univ:')]
            all_exams = [n for n in labels if n.startswith('exam:')]
            unmapped.append(dict(
                number=issue['number'],
                title=issue['title'],
                state=issue['state'].lower(),
                url=issue['url'],
                updated_at=issue.get('updatedAt'),
                kinds=sorted(n[5:] for n in labels if n.startswith('kind:') and n[5:] in KINDS),
                univ=univs[0] if len(univs) == 1 and len(all_univs) == 1 else None,
                exam=exams[0] if len(exams) == 1 and len(all_exams) == 1 else None,
            ))
            continue
        pid, error = validate_labels(labels)
        title, body = issue.get('title', ''), issue.get('body') or ''
        scope = explicit_ids(title) | explicit_ids(body)
        if (GLOBAL_RE.search(title) or question_list(title) or question_list(body)
                or (pid and scope - {pid})):
            error = 'current scope conflicts with single-question labels'
        if error:
            rejected.append(dict(number=issue['number'], reason=error))
            continue
        problems[pid].append(dict(number=issue['number'], title=issue['title'],
                                  state=issue['state'].lower(), url=issue['url'],
                                  updated_at=issue.get('updatedAt'),
                                  kinds=sorted(n[5:] for n in labels if n.startswith('kind:'))))
    for rows in problems.values():
        rows.sort(key=lambda r: (r['state'] != 'open', r['number']))
    unmapped.sort(key=lambda r: (r['state'] != 'open', r['number']))
    return dict(schema_version=1, repo=repo, generated_at=now(),
                problems=dict(sorted(problems.items())), unmapped=unmapped, rejected=rejected)
```

In `scratch/sync_issue_labels.py` lines 214–218:
```python
    if args.export:
        data = build_index(issues, args.repo)
        write_json(args.export, data)
        print(f'Exported {len(data["problems"])} problems, {len(data["unmapped"])} unmapped; rejected {len(data["rejected"])} issues')
        return 1 if data['rejected'] else 0
```

- [ ] **Step 5: Run pytest to verify GREEN**

Run: `python3 -m pytest tests/scratch/test_issue_labels.py -v`
Expected: PASS (all tests green).

---

### Task 2: Extend Node Snapshot Reader (`web/src/lib/issues.mjs`)

**Files:**
- Modify: `web/src/lib/issues.mjs`
- Test: `web/tests/issues.test.mjs`

**Interfaces:**
- Consumes: `web/src/data/issues-by-problem.json`
- Produces: `readIssueIndex(file)` returning `{ available: boolean, generatedAt: string | null, problems: Record<string, IssueRow[]>, unmapped: UnmappedIssueRow[] }`.

- [ ] **Step 1: Write failing tests in `web/tests/issues.test.mjs`**

Append to `web/tests/issues.test.mjs`:
```javascript
test('readIssueIndex supports optional unmapped list and validates its entries', () => {
  withSnapshot(snapshot(), index => {
    assert.equal(index.available, true);
    assert.deepEqual(index.unmapped, []);
  });

  const withUnmapped = {
    ...snapshot(),
    unmapped: [
      { ...row(50, 'open'), updated_at: '2026-11-01T00:00:00Z', kinds: ['figure'], univ: 'ukyoto', exam: 'zenki' },
      { ...row(51, 'closed'), updated_at: null, kinds: [], univ: null, exam: null },
    ],
  };
  withSnapshot(withUnmapped, index => {
    assert.equal(index.available, true);
    assert.equal(index.unmapped.length, 2);
    assert.equal(index.unmapped[0].univ, 'ukyoto');
  });

  for (const bad of [
    s => { s.unmapped = 'not-an-array'; },
    s => { s.unmapped = [{ ...row(9), url: 'https://evil.example/issues/9', kinds: [], univ: null, exam: null }]; },
    s => { s.unmapped = [{ ...row(9), kinds: [], univ: 'waseda', exam: null }]; },
    s => { s.unmapped = [{ ...row(9), kinds: ['invalid'], univ: null, exam: null }]; },
  ]) {
    const s = snapshot();
    bad(s);
    withSnapshot(s, index => assert.equal(index.available, false));
  }
});
```

- [ ] **Step 2: Run Node tests to verify RED**

Run: `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web test`
Expected: FAIL (`index.unmapped` is `undefined`).

- [ ] **Step 3: Update `web/src/lib/issues.mjs` with `unmapped` validation**

Update `web/src/lib/issues.mjs`:
```javascript
import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

export const REPO = 'ToAmano/Univ_EntranceExam_Math_Collection';
export const REPO_URL = `https://github.com/${REPO}`;
const PROBLEM_ID = /^(utokyo|ukyoto|titech)\/(zenki|kouki)\/[0-9]{4}\/[1-9][0-9]*$/;
const VALID_UNIVS = new Set(['utokyo', 'ukyoto', 'titech']);
const VALID_EXAMS = new Set(['zenki', 'kouki']);
const VALID_KINDS = new Set(['proof', 'figure', 'reference', 'transcription', 'style']);

function isValidIssueCore(issue) {
  if (!issue || typeof issue !== 'object') return false;
  if (!Number.isSafeInteger(issue.number) || issue.number < 1 || typeof issue.title !== 'string') return false;
  if (!['open', 'closed'].includes(issue.state) || issue.url !== `${REPO_URL}/issues/${issue.number}`) return false;
  if (issue.kinds !== undefined) {
    if (!Array.isArray(issue.kinds) || issue.kinds.some(k => typeof k !== 'string' || !VALID_KINDS.has(k))) return false;
  }
  return true;
}

/** Read once per build, never once per page or from a visitor's browser. */
export function readIssueIndex(file = resolve('src/data/issues-by-problem.json')) {
  try {
    const index = JSON.parse(readFileSync(file, 'utf8'));
    if (index.schema_version !== 1 || index.repo !== REPO ||
        typeof index.generated_at !== 'string' || !Number.isFinite(Date.parse(index.generated_at)) ||
        !index.problems || typeof index.problems !== 'object' || Array.isArray(index.problems) ||
        !Array.isArray(index.rejected) || index.rejected.length) throw new Error('Invalid issue index');
    for (const [id, issues] of Object.entries(index.problems)) {
      if (!PROBLEM_ID.test(id) || !Array.isArray(issues)) throw new Error('Invalid problem mapping');
      for (const issue of issues) {
        if (!isValidIssueCore(issue)) throw new Error('Invalid issue entry');
      }
    }
    const unmapped = index.unmapped ?? [];
    if (!Array.isArray(unmapped)) throw new Error('Invalid unmapped list');
    for (const issue of unmapped) {
      if (!isValidIssueCore(issue)) throw new Error('Invalid unmapped issue entry');
      if (issue.univ !== null && issue.univ !== undefined && !VALID_UNIVS.has(issue.univ)) throw new Error('Invalid unmapped univ');
      if (issue.exam !== null && issue.exam !== undefined && !VALID_EXAMS.has(issue.exam)) throw new Error('Invalid unmapped exam');
    }
    return { available: true, generatedAt: index.generated_at, problems: index.problems, unmapped };
  } catch (error) {
    console.warn(`[issues] Snapshot unavailable: ${error.message}`);
    return { available: false, generatedAt: null, problems: {}, unmapped: [] };
  }
}

/** The page type is excluded from the identity: problem and solution share Issues. */
export function problemIssues(index, data) {
  const id = `${data.university}/${data.category}/${data.year}/${data.question}`;
  if (data.type === 'summary' || !PROBLEM_ID.test(id)) return null;
  const query = new URLSearchParams({ q: `is:issue is:open label:"problem:${id}"` });
  return {
    available: index.available,
    generatedAt: index.generatedAt,
    searchUrl: `${REPO_URL}/issues?${query}`,
    issues: (index.problems[id] || []).filter(i => i.state === 'open').sort((a, b) => a.number - b.number),
  };
}
```

- [ ] **Step 4: Run Node tests to verify GREEN**

Run: `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web test`
Expected: PASS.

---

### Task 3: Build Issue & Archive Statistics Aggregator (`web/src/lib/issue-stats.mjs`)

**Files:**
- Create: `web/src/lib/issue-stats.mjs`
- Test: `web/tests/issue-stats.test.mjs`

**Interfaces:**
- Consumes: `index` from `readIssueIndex()`, `allEntries` array from `getCollection('solutions')`, `baseUrl` string.
- Produces:
  - `CATEGORIES`: 6 category definitions (`utokyo-zenki`, `ukyoto-zenki`, `titech-zenki`, `utokyo-kouki`, `ukyoto-kouki`, `titech-kouki`)
  - `KIND_META`: ordered kind definitions
  - `buildArchiveSummary(allEntries)`
  - `buildIssueStats(index, allEntries, baseUrl)`

- [ ] **Step 1: Write failing tests in `web/tests/issue-stats.test.mjs`**

Create `web/tests/issue-stats.test.mjs`:
```javascript
import test from 'node:test';
import assert from 'node:assert/strict';
import { buildArchiveSummary, buildIssueStats } from '../src/lib/issue-stats.mjs';
import { REPO_URL } from '../src/lib/issues.mjs';

const makeEntry = (university, category, year, question, type = 'solution') => ({
  slug: `${university}-${category}-${year}-${question}-${type}`,
  data: { university, category, year, question, type },
});

const sampleEntries = [
  makeEntry('utokyo', 'zenki', '1975', '1', 'problem'),
  makeEntry('utokyo', 'zenki', '1975', '1', 'solution'),
  makeEntry('utokyo', 'zenki', '1975', '2', 'problem'),
  makeEntry('utokyo', 'zenki', '2014', '1', 'solution'),
  makeEntry('utokyo', 'zenki', '2014', '0', 'summary'),
  makeEntry('sample_utokyo', 'zenki', '2020', '1', 'solution'),
  makeEntry('ukyoto', 'kouki', '1995', '1', 'solution'),
];

test('buildArchiveSummary deduplicates problem/solution pairs and ignores summaries and samples', () => {
  const summary = buildArchiveSummary(sampleEntries);
  assert.equal(summary.totalQuestions, 4);
  assert.deepEqual(summary.byUniversity, { utokyo: 3, ukyoto: 1, titech: 0 });
  assert.equal(summary.minYear, '1975');
  assert.equal(summary.maxYear, '2014');
  assert.equal(summary.zenkiYearCount, 2);
  assert.equal(summary.koukiYearCount, 1);
});

test('buildIssueStats aggregates single-problem, category-wide, general, and unrecorded-problem issues', () => {
  const index = {
    available: true,
    generatedAt: '2026-11-08T18:00:00Z',
    problems: {
      'utokyo/zenki/1975/1': [
        { number: 101, title: 'Proof & fig issue', state: 'open', url: `${REPO_URL}/issues/101`, updated_at: '2026-11-05T10:00:00Z', kinds: ['figure', 'proof'] },
        { number: 102, title: 'Second open issue', state: 'open', url: `${REPO_URL}/issues/102`, updated_at: '2026-11-06T10:00:00Z', kinds: [] },
        { number: 90, title: 'Closed issue', state: 'closed', url: `${REPO_URL}/issues/90`, updated_at: '2026-10-01T10:00:00Z', kinds: ['proof'] },
      ],
      // Unrecorded problem (not in sampleEntries yet, e.g. transcription issue)
      'titech/kouki/1996/2': [
        { number: 11, title: '[TeX化] 東工大後期1996年 第2問', state: 'open', url: `${REPO_URL}/issues/11`, updated_at: '2026-07-22T00:00:00Z', kinds: ['transcription'] },
      ],
    },
    unmapped: [
      { number: 1408, title: '京大前期TikZ改修', state: 'open', url: `${REPO_URL}/issues/1408`, updated_at: '2026-11-07T00:00:00Z', kinds: ['figure'], univ: 'ukyoto', exam: 'zenki' },
      { number: 593, title: '横断タスク', state: 'open', url: `${REPO_URL}/issues/593`, updated_at: '2026-11-08T00:00:00Z', kinds: [], univ: null, exam: null },
      { number: 500, title: '完了済みCI改修', state: 'closed', url: `${REPO_URL}/issues/500`, updated_at: '2026-09-01T00:00:00Z', kinds: [], univ: null, exam: null },
    ],
  };

  const stats = buildIssueStats(index, sampleEntries, '/base');
  assert.equal(stats.available, true);
  // Open: #101, #102, #11, #1408, #593 = 5. Closed: #90, #500 = 2. Total = 7.
  assert.equal(stats.totals.open, 5);
  assert.equal(stats.totals.closed, 2);
  assert.equal(stats.totals.all, 7);
  assert.equal(stats.totals.problemOpen, 4);
  assert.equal(stats.totals.generalOpen, 1);
  assert.equal(stats.totals.completionRate, 28.6);
  assert.equal(stats.totals.openByKind.proof, 1);
  assert.equal(stats.totals.openByKind.figure, 2);
  assert.equal(stats.totals.openByKind.transcription, 1);
  assert.equal(stats.totals.openByKind.unclassified, 2);

  const utokyoZenki = stats.categories.find(c => c.id === 'utokyo-zenki');
  assert.equal(utokyoZenki.openCount, 2);
  assert.equal(utokyoZenki.closedCount, 1);
  // Solution page preferred over problem page for 1975/1; problem page fallback for 1975/2
  const y1975 = utokyoZenki.decades.flatMap(d => d.years).find(y => y.year === '1975');
  assert.equal(y1975.questions[0].pageHref, '/base/solutions/utokyo-zenki-1975-1-solution/');
  assert.equal(y1975.questions[0].pageLabel, '解答ページ →');
  assert.equal(y1975.questions[0].openCount, 2);
  assert.equal(y1975.questions[1].pageHref, '/base/solutions/utokyo-zenki-1975-2-problem/');
  assert.equal(y1975.questions[1].pageLabel, '問題ページ →');

  // Category-wide unmapped issue (#1408) counted in ukyoto-zenki
  const ukyotoZenki = stats.categories.find(c => c.id === 'ukyoto-zenki');
  assert.equal(ukyotoZenki.openCount, 1);
  assert.equal(ukyotoZenki.openIssues[0].badge, '区分横断');

  // Unrecorded problem appears in titech-kouki matrix with recorded=false and pageHref=null
  const titechKouki = stats.categories.find(c => c.id === 'titech-kouki');
  assert.equal(titechKouki.openCount, 1);
  const y1996 = titechKouki.decades.flatMap(d => d.years).find(y => y.year === '1996');
  assert.equal(y1996.questions[0].question, '2');
  assert.equal(y1996.questions[0].recorded, false);
  assert.equal(y1996.questions[0].pageHref, null);

  // General bucket holds #593 (open) and counts #500 (closed)
  assert.equal(stats.general.openCount, 1);
  assert.equal(stats.general.closedCount, 1);
  assert.equal(stats.general.openIssues[0].number, 593);
});

test('buildIssueStats degrades gracefully when snapshot is unavailable', () => {
  const stats = buildIssueStats({ available: false, generatedAt: null, problems: {}, unmapped: [] }, sampleEntries, '');
  assert.equal(stats.available, false);
  assert.equal(stats.totals.completionRate, null);
  const utokyoZenki = stats.categories.find(c => c.id === 'utokyo-zenki');
  assert.equal(utokyoZenki.decades.flatMap(d => d.years).length, 2);
});
```

- [ ] **Step 2: Run Node tests to verify RED**

Run: `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web test`
Expected: FAIL (`Cannot find module '../src/lib/issue-stats.mjs'`).

- [ ] **Step 3: Implement `web/src/lib/issue-stats.mjs`**

Create `web/src/lib/issue-stats.mjs`:
```javascript
import { REPO_URL } from './issues.mjs';

export const CATEGORIES = [
  {
    id: 'utokyo-zenki',
    university: 'utokyo',
    category: 'zenki',
    univName: '東京大学',
    catName: '前期 理系数学',
    shortLabel: '東大前期',
    color: '#ef4444',
    textAccent: '#fca5a5',
    gradient: 'linear-gradient(135deg, rgba(239, 68, 68, 0.16), rgba(15, 23, 42, 0.82))',
    border: 'rgba(239, 68, 68, 0.35)',
  },
  {
    id: 'ukyoto-zenki',
    university: 'ukyoto',
    category: 'zenki',
    univName: '京都大学',
    catName: '前期 理系数学',
    shortLabel: '京大前期',
    color: '#8b5cf6',
    textAccent: '#c4b5fd',
    gradient: 'linear-gradient(135deg, rgba(139, 92, 246, 0.16), rgba(15, 23, 42, 0.82))',
    border: 'rgba(139, 92, 246, 0.35)',
  },
  {
    id: 'titech-zenki',
    university: 'titech',
    category: 'zenki',
    univName: '東京工業大学',
    catName: '前期 理系数学',
    shortLabel: '東工大前期',
    color: '#10b981',
    textAccent: '#6ee7b7',
    gradient: 'linear-gradient(135deg, rgba(16, 185, 129, 0.16), rgba(15, 23, 42, 0.82))',
    border: 'rgba(16, 185, 129, 0.35)',
  },
  {
    id: 'utokyo-kouki',
    university: 'utokyo',
    category: 'kouki',
    univName: '東京大学',
    catName: '後期 理系数学',
    shortLabel: '東大後期',
    color: '#f43f5e',
    textAccent: '#fda4af',
    gradient: 'linear-gradient(135deg, rgba(244, 63, 94, 0.14), rgba(15, 23, 42, 0.82))',
    border: 'rgba(244, 63, 94, 0.3)',
  },
  {
    id: 'ukyoto-kouki',
    university: 'ukyoto',
    category: 'kouki',
    univName: '京都大学',
    catName: '後期 理系数学',
    shortLabel: '京大後期',
    color: '#a78bfa',
    textAccent: '#ddd6fe',
    gradient: 'linear-gradient(135deg, rgba(167, 139, 250, 0.14), rgba(15, 23, 42, 0.82))',
    border: 'rgba(167, 139, 250, 0.3)',
  },
  {
    id: 'titech-kouki',
    university: 'titech',
    category: 'kouki',
    univName: '東京工業大学',
    catName: '後期 理系数学',
    shortLabel: '東工大後期',
    color: '#34d399',
    textAccent: '#a7f3d0',
    gradient: 'linear-gradient(135deg, rgba(52, 211, 153, 0.14), rgba(15, 23, 42, 0.82))',
    border: 'rgba(52, 211, 153, 0.3)',
  },
];

export const KIND_META = [
  { key: 'proof', label: 'proof', jp: '論証・解答' },
  { key: 'transcription', label: 'transcription', jp: '文字起こし' },
  { key: 'figure', label: 'figure', jp: '図表・TikZ' },
  { key: 'reference', label: 'reference', jp: '相互参照' },
  { key: 'style', label: 'style', jp: '書式' },
];

const VALID_UNIVS = new Set(['utokyo', 'ukyoto', 'titech']);
const VALID_CATS = new Set(['zenki', 'kouki']);

function emptyKindCounts() {
  return { proof: 0, transcription: 0, figure: 0, reference: 0, style: 0, unclassified: 0 };
}

function addKinds(target, kinds = []) {
  if (!kinds || kinds.length === 0) {
    target.unclassified += 1;
    return;
  }
  for (const k of kinds) {
    if (k in target) target[k] += 1;
  }
}

function calcRate(closed, open) {
  const all = closed + open;
  if (all === 0) return null;
  return Math.round((closed / all) * 1000) / 10;
}

function formatShortDate(iso) {
  if (!iso || typeof iso !== 'string') return null;
  const t = Date.parse(iso);
  if (!Number.isFinite(t)) return null;
  return new Date(t).toISOString().slice(0, 10);
}

function isRealCatalogEntry(entry) {
  const d = entry?.data;
  if (!d) return false;
  if (!VALID_UNIVS.has(d.university) || !VALID_CATS.has(d.category)) return false;
  if (d.question === '0' || d.type === 'summary') return false;
  return true;
}

export function buildArchiveSummary(allEntries = []) {
  const seenQuestions = new Set();
  const byUniversity = { utokyo: 0, ukyoto: 0, titech: 0 };
  const zenkiYears = new Set();
  const koukiYears = new Set();
  let minYear = null;
  let maxYear = null;

  for (const entry of allEntries) {
    if (!isRealCatalogEntry(entry)) continue;
    const { university, category, year, question } = entry.data;
    const key = `${university}/${category}/${year}/${question}`;
    if (!seenQuestions.has(key)) {
      seenQuestions.add(key);
      byUniversity[university] += 1;
    }
    if (category === 'zenki') zenkiYears.add(`${university}:${year}`);
    if (category === 'kouki') koukiYears.add(`${university}:${year}`);
    if (minYear === null || year < minYear) minYear = year;
    if (maxYear === null || year > maxYear) maxYear = year;
  }

  const distinctZenkiYears = new Set([...zenkiYears].map(s => s.split(':')[1]));
  const distinctKoukiYears = new Set([...koukiYears].map(s => s.split(':')[1]));

  return {
    totalQuestions: seenQuestions.size,
    byUniversity,
    minYear,
    maxYear,
    zenkiYearCount: distinctZenkiYears.size,
    koukiYearCount: distinctKoukiYears.size,
  };
}

export function buildIssueStats(index, allEntries = [], baseUrl = '') {
  const cleanBase = baseUrl.replace(/\/$/, '');
  const catalogMap = new Map();

  for (const entry of allEntries) {
    if (!isRealCatalogEntry(entry)) continue;
    const { university, category, year, question, type } = entry.data;
    const id = `${university}/${category}/${year}/${question}`;
    const rec = catalogMap.get(id) || { solutionSlug: null, problemSlug: null };
    if (type === 'solution') rec.solutionSlug = entry.slug;
    else if (type === 'problem') rec.problemSlug = entry.slug;
    catalogMap.set(id, rec);
  }

  const catWideByKey = new Map();
  const generalOpenIssues = [];
  let generalClosedCount = 0;

  for (const item of index.unmapped || []) {
    if (item.univ && item.exam) {
      const catKey = `${item.univ}-${item.exam}`;
      if (!catWideByKey.has(catKey)) catWideByKey.set(catKey, []);
      catWideByKey.get(catKey).push(item);
    } else if (item.state === 'open') {
      generalOpenIssues.push({
        number: item.number,
        title: item.title,
        url: item.url,
        updatedDate: formatShortDate(item.updated_at),
        kinds: item.kinds || [],
      });
    } else {
      generalClosedCount += 1;
    }
  }
  generalOpenIssues.sort((a, b) => b.number - a.number);

  const globalOpenByKind = emptyKindCounts();
  for (const gi of generalOpenIssues) addKinds(globalOpenByKind, gi.kinds);

  let totalProblemOpen = 0;
  let totalProblemClosed = 0;

  const categories = CATEGORIES.map(cfg => {
    const prefix = `${cfg.university}/${cfg.category}/`;
    const yearMap = new Map();

    const ensureCell = (year, question) => {
      if (!yearMap.has(year)) yearMap.set(year, new Map());
      const qMap = yearMap.get(year);
      if (!qMap.has(question)) qMap.set(question, { question, catalog: null, issues: [] });
      return qMap.get(question);
    };

    for (const [id, rec] of catalogMap.entries()) {
      if (!id.startsWith(prefix)) continue;
      const [, , year, question] = id.split('/');
      ensureCell(year, question).catalog = rec;
    }

    for (const [id, issues] of Object.entries(index.problems || {})) {
      if (!id.startsWith(prefix)) continue;
      const [, , year, question] = id.split('/');
      ensureCell(year, question).issues = issues;
    }

    const catOpenByKind = emptyKindCounts();
    let catOpenCount = 0;
    let catClosedCount = 0;
    const catOpenIssues = [];

    for (const cw of catWideByKey.get(cfg.id) || []) {
      if (cw.state === 'open') {
        catOpenCount += 1;
        addKinds(catOpenByKind, cw.kinds || []);
        addKinds(globalOpenByKind, cw.kinds || []);
        catOpenIssues.push({
          scope: 'category',
          problemKey: null,
          year: null,
          question: null,
          badge: '区分横断',
          number: cw.number,
          title: cw.title,
          url: cw.url,
          updatedDate: formatShortDate(cw.updated_at),
          kinds: cw.kinds || [],
          pageHref: null,
          pageLabel: null,
        });
      } else {
        catClosedCount += 1;
      }
    }

    const sortedYears = [...yearMap.keys()].sort((a, b) => b.localeCompare(a));
    const decadeMap = new Map();

    for (const year of sortedYears) {
      const qMap = yearMap.get(year);
      const sortedQs = [...qMap.values()].sort((a, b) =>
        a.question.localeCompare(b.question, undefined, { numeric: true })
      );

      let yearOpenCount = 0;
      const questions = sortedQs.map(cell => {
        const openList = cell.issues.filter(i => i.state === 'open');
        const closedCount = cell.issues.length - openList.length;
        catOpenCount += openList.length;
        catClosedCount += closedCount;
        yearOpenCount += openList.length;

        const recorded = Boolean(cell.catalog?.solutionSlug || cell.catalog?.problemSlug);
        const pageHref = cell.catalog?.solutionSlug
          ? `${cleanBase}/solutions/${cell.catalog.solutionSlug}/`
          : cell.catalog?.problemSlug
            ? `${cleanBase}/solutions/${cell.catalog.problemSlug}/`
            : null;
        const pageLabel = cell.catalog?.solutionSlug
          ? '解答ページ →'
          : cell.catalog?.problemSlug
            ? '問題ページ →'
            : null;

        const problemKey = `${year}/${cell.question}`;
        const openKindSet = new Set();
        for (const iss of openList) {
          const ks = iss.kinds || [];
          addKinds(catOpenByKind, ks);
          addKinds(globalOpenByKind, ks);
          if (ks.length === 0) openKindSet.add('unclassified');
          for (const k of ks) openKindSet.add(k);

          catOpenIssues.push({
            scope: 'problem',
            problemKey,
            year,
            question: cell.question,
            badge: `${year}年 第${cell.question}問`,
            number: iss.number,
            title: iss.title,
            url: iss.url,
            updatedDate: formatShortDate(iss.updated_at),
            kinds: ks,
            pageHref,
            pageLabel,
          });
        }

        return {
          question: cell.question,
          problemKey,
          recorded,
          pageHref,
          pageLabel,
          openCount: openList.length,
          closedCount,
          openIssueKinds: openList.map(i => i.kinds || []),
          hasUnclassifiedOpen: openKindSet.has('unclassified'),
        };
      });

      const decadeLabel = `${year.slice(0, 3)}0s`;
      if (!decadeMap.has(decadeLabel)) decadeMap.set(decadeLabel, []);
      decadeMap.get(decadeLabel).push({ year, openCount: yearOpenCount, questions });
    }

    totalProblemOpen += catOpenCount;
    totalProblemClosed += catClosedCount;

    const searchQuery = new URLSearchParams({
      q: `is:issue is:open label:"univ:${cfg.university}" label:"exam:${cfg.category}"`,
    });

    return {
      ...cfg,
      openCount: catOpenCount,
      closedCount: catClosedCount,
      completionRate: index.available ? calcRate(catClosedCount, catOpenCount) : null,
      openByKind: catOpenByKind,
      githubSearchUrl: `${REPO_URL}/issues?${searchQuery}`,
      decades: [...decadeMap.entries()].map(([label, years]) => ({ label, years })),
      openIssues: catOpenIssues,
    };
  });

  const totalOpen = totalProblemOpen + generalOpenIssues.length;
  const totalClosed = totalProblemClosed + generalClosedCount;
  const totalAll = totalOpen + totalClosed;

  const generalQuery = new URLSearchParams({
    q: 'is:issue is:open -label:univ:utokyo -label:univ:ukyoto -label:univ:titech',
  });

  return {
    available: Boolean(index.available),
    generatedAt: index.generatedAt || null,
    repoIssuesUrl: `${REPO_URL}/issues`,
    totals: {
      open: totalOpen,
      closed: totalClosed,
      all: totalAll,
      completionRate: index.available ? calcRate(totalClosed, totalOpen) : null,
      problemOpen: totalProblemOpen,
      generalOpen: generalOpenIssues.length,
      openByKind: globalOpenByKind,
    },
    categories,
    general: {
      openCount: generalOpenIssues.length,
      closedCount: generalClosedCount,
      githubSearchUrl: `${REPO_URL}/issues?${generalQuery}`,
      openIssues: generalOpenIssues,
    },
  };
}
```

- [ ] **Step 4: Run Node tests to verify GREEN**

Run: `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web test`
Expected: PASS (all tests in `canonical-sitemap.test.mjs`, `issues.test.mjs`, and `issue-stats.test.mjs` pass).

---

### Task 4: Add Global Navigation Link & Build `/stats/` Hub Page

**Files:**
- Modify: `web/src/layouts/Layout.astro:683-697`
- Create: `web/src/pages/stats/index.astro`

**Interfaces:**
- Consumes: `readIssueIndex` from `web/src/lib/issues.mjs`, `buildArchiveSummary` & `buildIssueStats` from `web/src/lib/issue-stats.mjs`, `TOPIC_TAGS` from `web/src/lib/tags.ts`, `buildBreadcrumbListJsonLd` from `web/src/utils/seo.ts`.

- [ ] **Step 1: Add `統計` link to `web/src/layouts/Layout.astro`**

In `web/src/layouts/Layout.astro`, update `.nav-links`:
```astro
					<ul class="nav-links">
						<li><a href={`${baseUrl}/`} class="nav-link">トップ</a></li>
						<li><a href={`${baseUrl}/#archive`} class="nav-link">過去問アーカイブ</a></li>
						<li><a href={`${baseUrl}/stats/`} class="nav-link">統計</a></li>
						<li><a href={`${baseUrl}/about/`} class="nav-link">サイトについて</a></li>
						<li>
							<a
								href="https://github.com/ToAmano/Univ_EntranceExam_Math_Collection"
								target="_blank" 
								rel="noopener noreferrer" 
								class="nav-link"
							>
								GitHub
							</a>
						</li>
					</ul>
```

- [ ] **Step 2: Create `web/src/pages/stats/index.astro`**

Create `web/src/pages/stats/index.astro` implementing Hub Option 1 (Breadcrumb + JSON-LD, 4 KPI Glass Cards, 2 Portal Navigation Cards to `/stats/issues/` and `/tags/`).

---

### Task 5: Build `/stats/issues/` Page (Combined Option A + Option C)

**Files:**
- Create: `web/src/pages/stats/issues.astro`

**Interfaces:**
- Consumes: `readIssueIndex`, `buildIssueStats`, `KIND_META`, `buildBreadcrumbListJsonLd`.
- Features:
  - Section A: 4 KPI cards + 6 university/exam cards with completion bars, `kind` pills, external `GitHub検索 ↗` links, and card click → Section C tab switch + reduced-motion-aware scroll + URL hash sync.
  - Section C: `content-visibility: auto; contain-intrinsic-size: auto none auto 640px;` explorer container with 7 accessible tabs, `kind` filter buttons, `Open がある年度のみ表示` checkbox (unchecked by default so all years render initially), full-year × question heatmap (updating cell colors/counts dynamically when `kind` filter changes), and sticky Open Issue list with cell-level drilldown and reset.
  - Initialized inside `document.addEventListener('astro:page-load', ...)` for `<ViewTransitions />` compatibility.

- [ ] **Step 1: Create `web/src/pages/stats/issues.astro`**

Write complete Astro component, scoped styles (with mobile breakpoints and `@media (prefers-reduced-motion: reduce)`), and vanilla JS controller.

---

### Task 6: End-to-End Verification (Tests, Live Snapshot, Fallback Build & Visual Check)

- [ ] **Step 1: Run Python & Node test suites**

Run:
- `python3 -m pytest tests/scratch/test_issue_labels.py -v`
- `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web test`

- [ ] **Step 2: Verify Astro build WITHOUT `issues-by-problem.json` (offline fallback)**

Temporarily move `web/src/data/issues-by-problem.json` aside, run `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web run build`, confirm exit code `0` and offline notice rendering in `web/dist/stats/issues/index.html`.

- [ ] **Step 3: Export fresh live GitHub Issue snapshot & build production site**

Run:
- `python3 scratch/sync_issue_labels.py --export web/src/data/issues-by-problem.json`
- `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web test`
- `PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" npm --prefix web run build`

- [ ] **Step 4: Visually inspect rendered `/stats/` and `/stats/issues/`**

Verify built HTML counts (`605` open issues, `806` closed issues, 6 categories + general bucket = 605) and inspect live preview rendering cleanly.
