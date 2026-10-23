"""Pure planning/validation for docs/issue-labels.md; never writes to GitHub."""
import hashlib
import json
import re
from collections import Counter, defaultdict
from datetime import datetime, timezone

DEFAULT_REPO = 'ToAmano/Univ_EntranceExam_Math_Collection'
KINDS = {'proof', 'figure', 'reference', 'transcription', 'style'}
ID = r'(?:utokyo|ukyoto|titech)/(?:zenki|kouki)/[0-9]{4}/[1-9][0-9]*'
ID_RE = re.compile(r'^' + ID + r'$')
PATH_RE = re.compile(r'(?<![\w])(' + ID + r')(?![0-9])(?=/|\b)')
MARKER_RE = re.compile(r'<!--\s*(math-audit-question|solution-figure-loss|original-problem-figure-audit):\s*(' + ID + r')\s*-->')
JP_RE = re.compile(r'(東京工業大学|東京大学|京都大学|東工大|東大|京大)\s*(前期|後期)\s*([0-9]{4})(?:年\s*第\s*([1-9][0-9]*)\s*問|[-/－]([1-9][0-9]*))')
EN_RE = re.compile(r'\b(utokyo|ukyoto|titech)[/ _-]+(zenki|kouki)[/ _:-]+([0-9]{4})[-/ ]+([1-9][0-9]*)\b')
UNIVERSITIES = {'東京工業大学': 'titech', '東工大': 'titech', '東京大学': 'utokyo', '東大': 'utokyo', '京都大学': 'ukyoto', '京大': 'ukyoto'}
GLOBAL_RE = re.compile(r'^\[(?:fix/|feat/|converter/|converter\]|分割済|後続課題)|まとめ|索引|Backlog', re.I)
PREFIXES = ('problem:', 'univ:', 'exam:', 'year:', 'kind:')


def explicit_ids(text):
    ids = {'/'.join((UNIVERSITIES[m[1]], 'zenki' if m[2] == '前期' else 'kouki', m[3], m[4] or m[5])) for m in JP_RE.finditer(text)}
    ids.update('/'.join(m.groups()) for m in EN_RE.finditer(text))
    ids.update(m[1] for m in PATH_RE.finditer(text))
    return ids


def question_list(text):
    return any(re.match(r'\s*(?:[・,、〜～~]|と|および|及び|[-–—])\s*(?:第\s*)?[1-9]', text[m.end():])
               for pattern in (JP_RE, EN_RE, PATH_RE) for m in pattern.finditer(text))


def now():
    return datetime.now(timezone.utc).isoformat()


def names(issue):
    return {x['name'] if isinstance(x, dict) else x for x in issue.get('labels', [])}


def fingerprint(issue):
    text = json.dumps([issue.get('title', ''), issue.get('body') or ''], ensure_ascii=False)
    return hashlib.sha256(text.encode()).hexdigest()


def identity_labels(problem_id):
    university, exam, year, question = problem_id.split('/')
    return {f'problem:{problem_id}', f'univ:{university}', f'exam:{exam}', f'year:{year}'}


def validate_labels(labels):
    labels = set(labels)
    ids = [n[8:] for n in labels if n.startswith('problem:')]
    if len(ids) != 1 or not ID_RE.fullmatch(ids[0]):
        return None, 'exactly one valid problem label required'
    pid = ids[0]
    expected = identity_labels(pid)
    actual = {n for n in labels if n.startswith(PREFIXES[:4])}
    if actual != expected:
        return None, 'identity facets disagree with problem ID or are missing'
    if any(n[5:] not in KINDS for n in labels if n.startswith('kind:')):
        return None, 'unknown kind label'
    return pid, None


def classify_issue(issue, root, overrides=None):
    title, body = issue.get('title', ''), issue.get('body') or ''
    result = dict(number=issue['number'], id=issue.get('id'), title=title,
                  fingerprint=fingerprint(issue), problem_id=None, labels=[], evidence={})
    def finish(status, reason):
        return dict(result, status=status, reason=reason)
    if GLOBAL_RE.search(title):
        return finish('excluded', 'aggregate or repository-wide issue')
    title_ids = explicit_ids(title)
    markers = list(MARKER_RE.finditer(body))
    marker_ids = {m[2] for m in markers}
    paths = explicit_ids(body)
    multiple = question_list(title) or question_list(body)
    existing = names(issue)
    label_ids = {n[8:] for n in existing if n.startswith('problem:')}
    result['evidence'] = dict(title_ids=sorted(title_ids), marker_ids=sorted(marker_ids), body_paths=sorted(paths))
    override = (overrides or {}).get(str(issue['number']))
    if override:
        if override.get('fingerprint') != result['fingerprint'] or not override.get('reason', '').strip():
            return finish('review', 'override is stale or has no review reason')
        pid = override.get('problem_id', '')
        if not ID_RE.fullmatch(pid):
            return finish('review', 'invalid override problem ID')
        result['evidence']['review_reason'] = override['reason']
    else:
        if multiple:
            return finish('review', 'abbreviated question list or range in title')
        strong = title_ids | marker_ids | label_ids
        if not strong:
            return finish('excluded', 'no explicit single-question identity in title, marker or label')
        if len(strong) != 1:
            return finish('review', 'title, marker or problem labels disagree')
        pid = next(iter(strong))
        if not ID_RE.fullmatch(pid):
            return finish('review', 'invalid problem label')
        if paths and paths != {pid}:
            return finish('review', 'body paths refer to different questions')
    result['problem_id'] = pid
    if not any((root / 'src' / pid / name).is_file() for name in ('problem.tex', 'solution.tex')) and not override:
        return finish('review', 'canonical source not found; confirm source or intended destination')
    expected = identity_labels(pid)
    conflicting = {n for n in existing if n.startswith(PREFIXES[:4])} - expected
    if conflicting or any(n[5:] not in KINDS for n in existing if n.startswith('kind:')):
        return finish('review', 'existing managed labels conflict with convention')
    kinds = {n for n in existing if n.startswith('kind:')}
    if '[監査]' in title or any(m[1] == 'math-audit-question' for m in markers):
        kinds.add('kind:proof')
    if re.search(r'TikZ|図監査|図表|図の|図が|図中|caption', title, re.I) or any(m[1] != 'math-audit-question' for m in markers):
        kinds.add('kind:figure')
    if re.search(r'未定義参照|参照違い|相互参照|式番号|\\(?:cref|label|ref)\b', title):
        kinds.add('kind:reference')
    if re.search(r'TeX化|文字起こし|未収録|原稿照合', title):
        kinds.add('kind:transcription')
    if re.search(r'句読点|字下げ|フォント|書式', title):
        kinds.add('kind:style')
    if override and 'kinds' in override:
        if not set(override['kinds']) <= KINDS:
            return finish('review', 'unknown reviewed kind')
        kinds.update('kind:' + k for k in override['kinds'])
    result['labels'] = sorted(expected | kinds)
    result['add_labels'] = sorted(set(result['labels']) - existing)
    result['kind_review'] = not bool(kinds)
    return finish('candidate', 'single question verified' if not override else 'explicitly reviewed mapping')


def build_plan(issues, root, repo=DEFAULT_REPO, overrides=None):
    rows = [classify_issue(i, root, overrides) for i in sorted(issues, key=lambda x: x['number'])]
    return dict(schema_version=1, repo=repo, generated_at=now(), overrides=overrides or {},
                summary=dict(Counter(r['status'] for r in rows)), issues=rows)


def build_index(issues, repo=DEFAULT_REPO):
    problems, rejected = defaultdict(list), []
    for issue in issues:
        labels = names(issue)
        if not any(n.startswith('problem:') for n in labels):
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
    return dict(schema_version=1, repo=repo, generated_at=now(),
                problems=dict(sorted(problems.items())), rejected=rejected)
