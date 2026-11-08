# Statistics Hub (`/stats/`) & Issue Status Page (`/stats/issues/`) Design Spec

- **Author**: Antigravity
- **Date**: 2026-11-08
- **Status**: Draft (Pending User Review)

## 1. Overview & Objectives

We add a **Statistics Hub (`/stats/`)** and a dedicated **Issue Statistics & Status subpage (`/stats/issues/`)** to the Astro static website (`web/`), powered by **build-time snapshot aggregation** (zero client-side GitHub API requests).

Key goals:
1. **Visibility without navigation bloat**: Add a single evergreen `統計` (`/stats/`) link to the global header (`Layout.astro`). Place the Issue status tracker under `/stats/issues/` so top-level navigation remains compact even when future sections (such as `/blog/` or topic-trend analytics) are introduced.
2. **Complete Issue accounting**: Extend the existing build-time Issue snapshot (`web/src/data/issues-by-problem.json`) to include non-single-problem Issues (`unmapped`) alongside validated single-problem Issues (`problems`), accounting for 100% of Open and Closed repository Issues with zero extra GitHub API calls in CI.
3. **Actionable visual exploration**: Combine high-level KPI & 6-category progress cards (Option A) with an interactive full-year × question status heatmap and filterable Open Issue list (Option C) on `/stats/issues/`.

---

## 2. Routing, Navigation & Sitemap

### 2.1 New Routes
- `web/src/pages/stats/index.astro` → `/Univ_EntranceExam_Math_Collection/stats/`
- `web/src/pages/stats/issues.astro` → `/Univ_EntranceExam_Math_Collection/stats/issues/`

Both routes respect `trailingSlash: 'always'` and `import.meta.env.BASE_URL` in `web/astro.config.mjs`.

### 2.2 Global Navigation
- In `web/src/layouts/Layout.astro`, insert `統計` (`${baseUrl}/stats/`) into `.nav-links` between `過去問アーカイブ` and `サイトについて`:
  - `トップ` | `過去問アーカイブ` | `統計` | `サイトについて` | `GitHub`
- No secondary banners or extra links are added to `index.astro`, `about.astro`, or `ProblemIssues.astro`.
- Breadcrumbs:
  - `/stats/`: `トップ / 統計`
  - `/stats/issues/`: `トップ / 統計 / Issue 統計`

### 2.3 Sitemap & SEO
- `web/src/lib/canonical-sitemap.mjs` already includes non-`/solutions/` static pages and assigns `latestDate` as `<lastmod>`. Both `/stats/` and `/stats/issues/` will be included in the generated sitemap automatically.

### 2.4 CI / Refresh Schedule
- `.github/workflows/deploy-pages.yml` keeps its existing triggers unchanged (`push` on `main`, weekly schedule `17 3 * * 0`, and `workflow_dispatch`) to conserve GitHub Actions runner minutes.
- Add `.superpowers/` to `.gitignore` so local visual brainstorming artifacts never pollute the working tree.

---

## 3. Build-Time Data Pipeline & Schema

### 3.1 Python Snapshot Export (`scratch/issue_labels.py`)
`deploy-pages.yml` already executes:
```bash
python3 scratch/sync_issue_labels.py --repo "$GITHUB_REPOSITORY" --export web/src/data/issues-by-problem.json
```
which fetches all Open and Closed repository Issues (`--state all --limit 10000`).

We extend `build_index(issues, repo)` in `scratch/issue_labels.py` while preserving full backwards compatibility with `schema_version: 1`:
- **`problems`** (unchanged): Maps validated single-question IDs (`{univ}/{exam}/{year}/{q}`) to sorted Issue entries (`{number, title, state, url, updated_at, kinds}`). Strict label validation and `rejected` detection remain completely unchanged (`docs/issue-labels.md` invariant preserved: `problems` never guesses from titles).
- **`unmapped`** (new top-level array): Collects every Issue that has **no** `problem:*` label, sorted by `(state != 'open', number)`:
  ```json
  {
    "number": 1408,
    "title": "【作図・表示】京大前期のTikZ図が他大学（東大・東工大）に比べて全体的に小さい問題の検討・改修",
    "state": "open",
    "url": "https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1408",
    "updated_at": "2026-11-07T12:00:00Z",
    "kinds": ["figure"],
    "univ": "ukyoto",
    "exam": "zenki"
  }
  ```
  - `univ`: Set to `'utokyo' | 'ukyoto' | 'titech'` iff the Issue carries **exactly one** valid `univ:*` label; otherwise `null`.
  - `exam`: Set to `'zenki' | 'kouki'` iff the Issue carries **exactly one** valid `exam:*` label; otherwise `null`.
  - `kinds`: Sorted list of valid `kind:*` label suffixes (`proof`, `figure`, `reference`, `transcription`, `style`).

### 3.2 Node Snapshot Reader & Aggregator (`web/src/lib/issues.mjs`)
1. **`readIssueIndex(file)`**:
   - Continues validating `schema_version === 1`, `repo`, `generated_at`, `problems`, and `rejected.length === 0`.
   - Validates `index.unmapped` when present (defaulting to `[]` if omitted so existing `schema_version: 1` test fixtures remain valid):
     - Each entry must have safe positive integer `number`, string `title`, `state` in `['open', 'closed']`, exact `url === ${REPO_URL}/issues/${entry.number}`, `univ` in `['utokyo', 'ukyoto', 'titech', null]`, `exam` in `['zenki', 'kouki', null]`, and `kinds` array of valid kind strings.
   - Returns `{ available: true, generatedAt, problems, unmapped }` (or `{ available: false, generatedAt: null, problems: {}, unmapped: [] }` on missing/invalid file).

2. **`buildIssueStats(index, catalogEntries, baseUrl)`** (new pure helper in `web/src/lib/issue-stats.mjs` to keep `issues.mjs` small and focused):
   - **Inputs**:
     - `index`: Result of `readIssueIndex()`.
     - `catalogEntries`: All solution/problem entries from `getCollection('solutions')` (excluding `sample_*` and `question === '0'` summaries).
     - `baseUrl`: Normalized Astro base URL.
   - **Classification rules**:
     - **Single-problem Issues** (`index.problems[id]`): Attributed to their exact `(univ, exam, year, question)` cell and `(univ, exam)` category.
     - **Category-wide Issues** (`index.unmapped` where both `univ !== null` and `exam !== null`): Attributed to that `(univ, exam)` category's Open/Closed totals and category Open Issue list (badged `区分横断`), without tying to a single matrix cell.
     - **General / Cross-cutting Issues** (remaining `index.unmapped` where `univ === null` or `exam === null`): Attributed to the `general` (`横断・全体`) bucket.
   - **Year × Question Matrix construction (per category)**:
     - Collects the union of `(year, question)` pairs from **both** `catalogEntries` (recorded problems) and `index.problems` (including unrecorded problems that have `kind:transcription` Issues).
     - Years are sorted descending (e.g. `2014` → `1961`, all 54 years for `zenki` and 18–22 years for `kouki`) and grouped by decade (`2010s`, `2000s`, ..., `1960s`).
     - Within each year, questions are sorted numerically (`1..N`, matching the actual question count of that year, whether 2, 4, 5, 6, or 7 questions).
     - Each cell stores:
       - `question`: Question number string
       - `hasSolution` / `hasProblem` / `pageHref`: Preferred internal link (`-solution` slug if present, else `-problem` slug, else `null` for unrecorded problems)
       - `openCount`, `closedCount`, `openIssues`
   - **Totals & KPIs**:
     - `totalOpen`, `totalClosed`, `totalAll`, `completionRate` (`totalClosed / totalAll` when `totalAll > 0`, else `null`)
     - `problemOpenCount` (single-problem + category-wide open), `generalOpenCount`
     - `openByKind`: Counts of Open Issues carrying `proof`, `transcription`, `figure`, `reference`, `style`, plus `unclassified` (Open Issues with zero `kind:*` labels). Because a single Issue may carry multiple `kind:*` labels (`docs/issue-labels.md`), per-kind counts are non-exclusive tag frequencies rather than a partition of `totalOpen`.

---

## 4. Page Specifications

### 4.1 Statistics Hub: `/stats/` (`web/src/pages/stats/index.astro`)
Follows **Hub Option 1 (KPI + Portal Navigation Cards)** using `Layout.astro`'s dark glassmorphism styling:
1. **Page Header**: Breadcrumb (`トップ / 統計`), title `アーカイブ 統計・データ`, and brief description.
2. **Archive Overview KPI Grid (4 cards)**:
   - **総収録問題数**: `countRealQuestions(realSolutions)` (currently 1,119 questions) + per-university breakdown (`東大 / 京大 / 東工大`).
   - **収録対象年度**: Min–max year across `realSolutions` (`1961–2014`) + `前期 / 後期` year counts.
   - **分類トピック**: `TOPIC_TAGS.length` (`15 分野`) + representative tag names.
   - **Issue 消化率**: When `index.available` is `true`, displays `completionRate%` (`Closed X / 残 Open Y`); when `false` (local build without snapshot), displays `未取得` with a link to GitHub Issues.
3. **Portal Navigation Cards (2 cards)**:
   - **Card 1 — 収録・校閲ステータス（Issue 統計）** (`href="${baseUrl}/stats/issues/"`):
     - Badge `🛠️ 品質・整備データ`, summary of what the page shows, current `Open / Closed` badge (when available), and `開く →` CTA.
   - **Card 2 — 分野タグ別 収録問題一覧** (`href="${baseUrl}/tags/"`):
     - Badge `🏷️ 出題テーマ分類`, description of the 15 controlled topic tags, and `開く →` CTA.

### 4.2 Issue Statistics Page: `/stats/issues/` (`web/src/pages/stats/issues.astro`)
Follows the **Combined Option A + Option C** layout:

1. **Page Header**:
   - Breadcrumb (`トップ / 統計 / Issue 統計`), title `収録・校閲ステータス Issue 統計`, and build-time timestamp badge (`最終集計: YYYY/MM/DD HH:mm JST` rendered via `<time datetime={generatedAt}>`).
   - **Offline / Missing Snapshot Fallback**: If `index.available === false`, displays a clear yellow `.notice` banner explaining that the local Issue snapshot is unavailable with a direct link to GitHub Issues, while still rendering the archive structure cleanly without build errors.

2. **Section A — Overall KPIs & 6 Category Cards**:
   - **4 KPI Cards**:
     1. `残 Open Issue 総数` (with breakdown: `問題・区分別 X / 横断・全体 Y`)
     2. `解決済み (Closed)` (with overall completion rate `%`)
     3. `種別 (kind) 内訳` (open counts across `proof`, `transcription`, `figure`, `reference`, `style`)
     4. `横断・全体 Issue` (clickable: switches Section C to the `横断・全体` tab and scrolls smoothly to Section C)
   - **6 Category Cards** (`utokyo-zenki`, `ukyoto-zenki`, `titech-zenki`, `utokyo-kouki`, `ukyoto-kouki`, `titech-kouki`, styled with the same university accent colors as `index.astro`):
     - Header: University & exam name + Open Issue count
     - Progress bar: Completion rate (`closed / (open + closed)`) + Closed count
     - Kind pills: Non-zero `kind:*` counts for open Issues in that category
     - Footer: Direct `GitHub検索 ↗` link (`is:issue is:open label:"univ:..." label:"exam:..."`) + `年度マップを見る ↓` indicator
     - **Card interaction**: Clicking a card (outside the external `GitHub検索 ↗` link) activates that category's tab in Section C, updates the URL hash (e.g. `#utokyo-zenki`), and smoothly scrolls to Section C.

3. **Section C — Interactive Category Explorer (All-Year Matrix + Open Issue List)**:
   - **Tab Bar (`role="tablist"`)**:
     - 7 tabs: `東大前期`, `東大後期`, `京大前期`, `京大後期`, `東工大前期`, `東工大後期`, and `横断・全体` (each showing its Open Issue count).
   - **Filter Toolbar** (visible on the 6 category tabs):
     - `kind` filter buttons: `すべて` (default), `proof`, `transcription`, `figure`, `その他 (reference / style / 未分類)`. Selecting a `kind` filter updates **both** the heatmap cell states (counting Open Issues matching the selected `kind`) and the right-pane Open Issue list.
     - Checkbox: `Open がある年度のみ表示` (**unchecked by default** so all years in the category are displayed initially; when checked, hides year rows that have 0 Open Issues under the currently active `kind` filter).
   - **Two-Pane Explorer Body** (side-by-side on desktop `> 860px` with sticky right pane; single-column stacked on mobile):
     - **Left Pane — Year × Question Heatmap**:
       - Displays **all years** for the active category in descending order, grouped under decade subheadings (`2010s`, `2000s`, ..., `1960s`).
       - Each year row shows the 4-digit year and buttons for each question `1..N`.
       - Visual states use color + border style + accessible `aria-label` / `title` (never color alone):
         - `0 open` (recorded): emerald tint (`c-ok`)
         - `0 open` (unrecorded): subtle dashed border (`c-na`)
         - `1 open`: amber tint (`c-w1`)
         - `2+ open`: rose/red tint (`c-w2`)
       - Clicking a question cell toggles cell-level filtering on the Right Pane (showing that question's Open Issues, or if 0 Open Issues, a clean card with a direct link to its solution/problem page). Clicking the selected cell again or clicking `絞り込み解除 ×` restores the category-level list.
     - **Right Pane — Open Issue List**:
       - Lists matching Open Issues for the active category (including `区分横断` category-wide Issues when no specific cell is selected, followed by single-problem Issues ordered by year desc, question asc, issue number asc).
       - Each row shows: problem badge (`YYYY年 第Q問` or `区分横断`), `kind:*` pills, `#number` + Issue title, updated date (`YYYY-MM-DD`), internal link (`解答ページ →` / `問題ページ →` if recorded), and external link (`GitHub ↗`).
   - **7th Tab (`横断・全体`)**:
     - Displays a single-column list of all Open `general` Issues (`#number`, title, `kinds` if any, updated date, `GitHub ↗` link) plus a summary link to view Closed general Issues on GitHub.

4. **Client-Side Interactivity & ViewTransitions**:
   - Written in vanilla `<script>` inside `issues.astro` with zero external JS framework dependencies.
   - Initialized on `astro:page-load` so state binding and URL hash deep-linking (`#utokyo-zenki`, `#general`, etc.) work both on initial page load and after Astro `<ViewTransitions />` navigation from `/stats/`.

---

## 5. Error Handling & Edge Cases

1. **Missing `issues-by-problem.json` in local dev**: `readIssueIndex()` catches missing-file errors, logs a single build warning, and returns `available: false`. Both `/stats/` and `/stats/issues/` build and render cleanly without throwing.
2. **Rejected single-problem labels**: Behavior in `sync_issue_labels.py --export` and `readIssueIndex()` remains strict (`rejected.length > 0` fails export / marks index unavailable) so single-problem integrity is never silently compromised.
3. **Zero Open Issues in a category or filter**: Displays a positive empty state (`条件に一致する Open Issue はありません`) rather than a blank box, and `0 / 0` division in completion rate safely renders `—` instead of `NaN%`.
4. **Mobile layout (`<= 640px` / `<= 860px`)**: KPI grids wrap to 2 columns, 6-category cards stack to 1 column, and the explorer panes stack vertically with comfortable touch targets (`min-height: 28px` on matrix cells).

---

## 6. Testing & Verification Plan

1. **Python Unit Tests (`tests/scratch/test_issue_labels.py`)**:
   - Verify `build_index` populates `unmapped` for Issues without `problem:*` labels (both category-scoped `univ+exam` Issues and repo-wide Issues), preserves exact `problems` behavior, and never guesses problem IDs from titles.
2. **Node Unit Tests (`web/tests/issues.test.mjs` & `web/tests/issue-stats.test.mjs`)**:
   - Verify `readIssueIndex` accepts both legacy `schema_version: 1` fixtures (without `unmapped`) and new fixtures (with `unmapped`), while rejecting malformed `unmapped` URLs/states.
   - Verify `buildIssueStats` accurately computes global/category Open & Closed totals, completion rates, `kind` counts, unrecorded-problem matrix inclusion, and `available: false` fallback.
3. **Astro Build & Visual Verification**:
   - Generate a fresh local `web/src/data/issues-by-problem.json` via `python3 scratch/sync_issue_labels.py --export web/src/data/issues-by-problem.json` (and also test building without it).
   - Run `pytest tests/scratch/test_issue_labels.py`, `cd web && npm test`, and `cd web && npm run build`.
   - Visually inspect `/stats/` and `/stats/issues/` (desktop & mobile widths) to confirm styling, contrast, tab/card/cell interactivity, and link accuracy.
