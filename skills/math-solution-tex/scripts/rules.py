#!/usr/bin/env python3
"""規約（references/・local/）から、必要な節だけを引き出す。

全部を読まずに、工程や lint の指摘に応じた節だけを読むための道具。

節番号:
  N5.3   数式・記法（references/notation-rules.md）
  F7.1   図（references/figure-rules.md。見出しは数字だけなので F を付けて呼ぶ。付録は FA・FB・FC）
  TB2.4  表（references/table-rules.md）
  TR4    文字起こし（references/transcription-rules.md）
  LN1・L2・W3   利用先固有（local/notation.md・local/transcription.md・local/workflow.md）
  「§N5.3」「[§F1.3]」（lint の表示）「figure §7.1」の形でも指定できる。上位の節を指定すると下位の節も含む。

使い方:
  python3 scripts/rules.py --sec N5.3 F7.1      # 節を表示する
  python3 scripts/rules.py --phase figure       # 工程ごとに読む節を表示する（--list と併用すると見出しだけ）
  python3 scripts/rules.py --list [--file figure]   # 節番号と見出しの一覧
  python3 scripts/rules.py --grep dcases        # 語句を含む節の一覧
"""
import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent

# (短い名前, ファイル, 数字だけの見出しに付ける接頭辞)
SOURCES = (
    ('notation', SKILL / 'references' / 'notation-rules.md', ''),
    ('figure', SKILL / 'references' / 'figure-rules.md', 'F'),
    ('table', SKILL / 'references' / 'table-rules.md', ''),
    ('transcription', SKILL / 'references' / 'transcription-rules.md', ''),
    ('local-notation', SKILL / 'local' / 'notation.md', ''),
    ('local-transcription', SKILL / 'local' / 'transcription.md', ''),
    ('local-workflow', SKILL / 'local' / 'workflow.md', ''),
)

# 工程ごとに読む節（SKILL.md の工程に対応する）
PHASES = {
    'transcribe': ['TR', 'L'],
    'define': ['F0.1', 'N1', 'N10'],
    'write': ['N', 'LN1', 'LN2', 'LN3'],
    'figure': ['F0', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'FA', 'FC'],
    'figure-only': ['F12', 'W3'],
    'table': ['TB', 'LN4', 'LN5'],
    'check': ['W1', 'W2', 'W3', 'F11'],
    'view': ['F11', 'W4', 'W5'],
}

HEADING_RE = re.compile(r'^(#{2,4})\s+(.*)$')
ID_RE = re.compile(r'^([A-Z]*)(\d+(?:\.\d+)*)\.?$')
APPENDIX_RE = re.compile(r'^付録\s*([A-Z])\.?$')


@dataclass
class Section:
    sid: str
    title: str
    level: int
    source: str
    path: Path
    text: str


def _section_id(heading, prefix):
    """見出しの文字列から (節番号, 見出しの残り) を返す。節番号のない見出しは None。"""
    first, _, rest = heading.partition(' ')
    m = ID_RE.match(first)
    if m:
        letters, number = m.groups()
        if not letters:
            if not prefix:
                return None
            letters = prefix
        return letters + number, rest.strip()
    m = APPENDIX_RE.match(' '.join(heading.split()[:2]))
    if m and prefix:
        return prefix + m.group(1), ' '.join(heading.split()[2:])
    return None


def load_sections(sources=SOURCES):
    sections = []
    for name, path, prefix in sources:
        if not path.exists():
            continue
        lines = path.read_text(encoding='utf-8').split('\n')
        heads = []
        in_code = False
        for i, line in enumerate(lines):
            if line.lstrip().startswith('```'):
                in_code = not in_code
            if in_code:
                continue
            m = HEADING_RE.match(line)
            if m:
                heads.append((i, len(m.group(1)), m.group(2)))
        for k, (i, level, heading) in enumerate(heads):
            parsed = _section_id(heading, prefix)
            if parsed is None:
                continue
            end = len(lines)
            for j, lvl, _ in heads[k + 1:]:
                if lvl <= level:
                    end = j
                    break
            text = '\n'.join(lines[i:end]).rstrip()
            text = re.sub(r'\n-{3,}\s*$', '', text).rstrip()
            sections.append(Section(parsed[0], parsed[1], level, name, path, text))
    return sections


def normalize(query):
    """「§N5.3」「[§F1.3]」「figure §7.1」「f7.1」などを節番号にそろえる。"""
    q = query.strip().strip('[]').replace('§', '').strip()
    m = re.match(r'^figure\s*(.+)$', q, re.IGNORECASE)
    if m:
        q = 'F' + m.group(1).strip()
    return q.upper().rstrip('.')


def matches(section, query):
    """節番号がその節か、その下位の節なら True（N5 は N5.1 を含むが N50 は含まない）。
    英字だけの指定（TR、L など）は、その接頭辞の節すべて。"""
    sid = section.sid.upper()
    if query.isalpha():
        return re.match(rf'^{query}(\d|$)', sid) is not None and re.match(r'^[A-Z]+', sid).group() == query
    return sid == query or sid.startswith(query + '.')


def select(sections, queries):
    """指定された節を、重複を除いて元の順に返す（下位の節は上位の節の本文に含まれるので除く）。"""
    chosen = []
    for q in queries:
        nq = normalize(q)
        hit = [s for s in sections if matches(s, nq)]
        if not hit:
            raise KeyError(q)
        chosen.extend(hit)
    result = []
    for s in chosen:
        covered = any(r.sid != s.sid and r.source == s.source and s.sid.startswith(r.sid + '.') for r in chosen)
        if not covered and s not in result:
            result.append(s)
    return result


def own_text(section):
    """節の本文のうち、下位の節の見出しより前の部分（下位の節と同じ語句で二重に当たらないように）。"""
    lines = section.text.split('\n')
    for i, line in enumerate(lines[1:], start=1):
        m = HEADING_RE.match(line)
        if m and len(m.group(1)) > section.level:
            return '\n'.join(lines[:i])
    return section.text


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--sec', nargs='+', metavar='ID', help='表示する節（N5.3、F7.1、TB2、[§N5.1] など）')
    parser.add_argument('--phase', choices=sorted(PHASES), help='工程ごとに読む節を表示する')
    parser.add_argument('--list', action='store_true', help='節番号と見出しの一覧を表示する')
    parser.add_argument('--file', choices=[name for name, _, _ in SOURCES], help='--list の対象を1つの規約に絞る')
    parser.add_argument('--grep', metavar='WORD', help='語句を含む節の一覧を表示する')
    args = parser.parse_args(argv)
    sections = load_sections()

    if args.grep:
        word = args.grep.lower()
        for s in sections:
            if word in own_text(s).lower():
                print(f'{s.sid:8s} {s.title}  ({s.source})')
        return 0

    queries = list(args.sec or [])
    if args.phase:
        queries += PHASES[args.phase]
    if args.list:
        pool = [s for s in sections if any(matches(s, normalize(q)) for q in queries)] if queries else sections
        for s in pool:
            if args.file and s.source != args.file:
                continue
            print(f'{"  " * (s.level - 2)}{s.sid:8s} {s.title}  ({s.source})')
        return 0
    if not queries:
        parser.print_help()
        return 2
    try:
        chosen = select(sections, queries)
    except KeyError as missing:
        print(f'節が見つからない：{missing.args[0]}（--list で一覧を表示できる）', file=sys.stderr)
        return 1
    for k, s in enumerate(chosen):
        if k:
            print('\n' + '-' * 40 + '\n')
        print(f'<!-- {s.source}: {s.path.relative_to(SKILL)} -->')
        print(s.text)
    return 0


if __name__ == '__main__':
    sys.exit(main())
