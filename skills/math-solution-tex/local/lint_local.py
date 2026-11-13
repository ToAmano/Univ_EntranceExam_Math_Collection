"""このリポジトリ固有の lint の検査（汎用の検査は scripts/lint_tex.py）。

- 解答の見出し（{\bf [解答]}・[別解]・[別解1]・[解説]）と proof 環境の見出し
- subfiles の \documentclass[../../main.tex]{subfiles}
- solution.tex での問題文の読み込み（\begin{oframed}\subfile{problem}\end{oframed}）
- problem.tex の形式（subfiles 文書であること、figure は [H]）と、solution.tex とのラベルの重複
- 対象ファイル（src/ の solution.tex・problem.tex）と、年度のまとめ（0/）を本文の検査から外す条件

使い方:
  python3 skills/math-solution-tex/scripts/lint_tex.py --rules skills/math-solution-tex/local/lint_local.py <file>
  （リポジトリでは scratch/lint_latex_style.py がこの設定で lint_tex を呼ぶ）
"""
import importlib.util
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SRC_DIR = REPO_ROOT / 'src'
_SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'


def _load_lint_tex():
    name = '_math_solution_tex_lint_tex'
    if name not in sys.modules:
        spec = importlib.util.spec_from_file_location(name, _SCRIPTS / 'lint_tex.py')
        module = importlib.util.module_from_spec(spec)
        sys.modules[name] = module
        spec.loader.exec_module(module)
    return sys.modules[name]


lint_tex = _load_lint_tex()
tex_references = lint_tex.tex_references
line_of = lint_tex.line_of
strip_comments = lint_tex.strip_comments
check_duplicate_labels = lint_tex.check_duplicate_labels
check_equation_references = lint_tex.check_equation_references

def check_proof_env(text):
    """\\begin{proof}[解] / \\begin{proof}[別解] のように、解答冒頭の見出し
    として proof 環境が使われているケースだけを検出する（local/notation.md LN1
    の趣旨は「解答冒頭を {\\bf [解答]} にする」ことであり、\\begin{lemma}...
    \\end{lemma} に対する本物の \\begin{proof}...\\end{proof}（補題の証明）
    はそもそも対象外）。ラベル無しの素の \\begin{proof} まで拾うと
    utokyo/kouki/2005/2 のような正当な用法を誤検知するため、[...] 引数の
    有無で判別する。"""
    errors = []
    for m in re.finditer(r'\\begin\{proof\}\[', text):
        errors.append((line_of(text, m.start()), "\\begin{proof}[...] は解答冒頭に使わない（{\\bf [...]} を使う）"))
    return errors


SOLUTION_HEADING_LINE_RE = re.compile(
    r'^(?P<prefix>[ \t]*(?:\\(?:smallskip|medskip|bigskip)\s*)*(?:\\noindent\s*)?)'
    r'(?P<token>'
    r'\{\\bf\s*[\[［]\s*(?P<k1>解答|解|別解|解説|注)\s*(?P<n1>[0-9０-９]*)\s*[\]］]\s*\}'
    r'|\\textbf\{\s*[\[［]\s*(?P<k2>解答|解|別解|解説|注)\s*(?P<n2>[0-9０-９]*)\s*[\]］]\s*\}'
    r'|[\[［]\s*\\textbf\{\s*(?P<k3>解答|解|別解|解説|注)\s*(?P<n3>[0-9０-９]*)\s*\}\s*[\]］]'
    r'|[\[［]\s*\{\\bf\s*(?P<k4>解答|解|別解|解説|注)\s*(?P<n4>[0-9０-９]*)\s*\}\s*[\]］]'
    r'|［\s*(?P<k5>解答|解|別解|解説)\s*(?P<n5>[0-9０-９]*)\s*］'
    r'|\[\s*(?P<k6>解答|解|別解|解説)\s*(?P<n6>[0-9０-９]*)\s*\](?=[ \t\r\n%]|$)'
    r')',
    re.MULTILINE,
)
CURRICULUM_SECTION_RE = re.compile(r'\\paragraph\{[^}]*課程[^}]*\}|\\section\*?\{')


def _iter_solution_heading_targets(text):
    all_matches = list(SOLUTION_HEADING_LINE_RE.finditer(text))
    if not all_matches:
        return []
    split_points = [0] + [m.start() for m in CURRICULUM_SECTION_RE.finditer(text)] + [len(text) + 1]
    results = []
    for sec_start, sec_end in zip(split_points[:-1], split_points[1:]):
        sec_matches = [m for m in all_matches if sec_start <= m.start() < sec_end]
        if not sec_matches:
            continue
        sol_indices = [
            idx for idx, m in enumerate(sec_matches)
            if (m.group('k1') or m.group('k2') or m.group('k3')
                or m.group('k4') or m.group('k5') or m.group('k6')) in ('解答', '解', '別解')
        ]
        num_sols = len(sol_indices)
        sol_rank = {idx: rank for rank, idx in enumerate(sol_indices)}
        for idx, m in enumerate(sec_matches):
            kind = (m.group('k1') or m.group('k2') or m.group('k3')
                    or m.group('k4') or m.group('k5') or m.group('k6'))
            tok = m.group('token')
            if kind in ('解説', '注'):
                target = r'{\bf [解説]}'
            else:
                rank = sol_rank[idx]
                if rank == 0:
                    target = r'{\bf [解答]}'
                elif num_sols == 2:
                    target = r'{\bf [別解]}'
                else:
                    target = f'{{\\bf [別解{rank}]}}'
            results.append((m.start('token'), m.end('token'), tok, target))
    return results


def check_solution_headings(text):
    """解答関連の見出し（AGENTS.md「解答見出しの表記」）をチェックする。
    - 最初の解法: {\\bf [解答]}
    - 別解が1つ: {\\bf [別解]}
    - 別解が複数: {\\bf [別解1]}, {\\bf [別解2]}, ...
    - 解法の後の説明: {\\bf [解説]}
    """
    errors = []
    for start, _, tok, target in _iter_solution_heading_targets(text):
        if tok != target:
            errors.append((
                line_of(text, start),
                f"解答見出しは {target} に統一する（{tok} → {target}）",
            ))
    return errors


def _find_solution_heading_edits(text, raw):
    edits = []
    for start, end, tok, target in _iter_solution_heading_targets(text):
        if end < len(raw) and raw[end] not in (' ', '\t', '\r', '\n'):
            replacement = target + ' '
        else:
            replacement = target
        if raw[start:end] != replacement:
            edits.append((start, end, replacement))
    return edits


def check_documentclass(text):
    """\\begin{document} を持つ文書は \\documentclass[../../main.tex]{subfiles} にする。
    problem.tex が \\begin{document} を持つこと自体は check_problem_is_document で検査する（#1472）。"""
    errors = []
    if '\\begin{document}' not in text:
        return errors
    m = re.search(r'\\documentclass\[([./]*)main\.tex\]\{subfiles\}', text)
    if not m:
        errors.append((1, "\\documentclass[../../main.tex]{subfiles} が見つからない"))
        return errors
    up_count = m.group(1).count('../')
    if up_count != 2:
        errors.append((line_of(text, m.start()),
                        f"\\documentclass の相対パスは ../../ であるべき（{up_count} 階層になっている）"))
    return errors


EMBED_PROBLEM_RE = re.compile(r'\\begin\{oframed\}\s*\\subfile\{problem\}\s*\\end\{oframed\}')


def check_problem_embedded(text):
    """solution.tex は先頭で問題文を枠付きで読み込む（#1472）。
    \\begin{oframed}\\subfile{problem}\\end{oframed} が [解答] の見出しより前にあること。"""
    m = EMBED_PROBLEM_RE.search(text)
    heading = re.search(r'\\bf\s*\[解答\]', text)
    if not m:
        return [(1, "solution.tex の先頭で \\begin{oframed}\\subfile{problem}\\end{oframed} を使って問題文を読み込む")]
    if heading and heading.start() < m.start():
        return [(line_of(text, m.start()), "問題文の読み込み（\\subfile{problem}）は [解答] の見出しより前に置く")]
    return []


def check_problem_is_document(text):
    """problem.tex は solution.tex から \\subfile で読み込む独立した subfiles 文書にする（#1472）。
    以前の後期の problem.tex は \\begin{document} を持たない中身だけの断片だった。"""
    if '\\begin{document}' not in text:
        return [(1, "problem.tex は \\documentclass[../../main.tex]{subfiles} と \\begin{document} を持つ文書にする")]
    return []


def check_problem_figure_float(text):
    """problem.tex は solution.tex の枠（oframed）の中に読み込まれ、枠の中では浮動体を使えないので、
    figure は [H] にする（#1472）。"""
    errors = []
    for m in re.finditer(r'\\begin\{figure\}(\[[^\]]*\])?', text):
        if m.group(1) != '[H]':
            errors.append((line_of(text, m.start()),
                           "problem.tex の figure は [H] にする（solution.tex の枠の中では浮動体を使えない）"))
    return errors


def check_problem_label_conflicts(text, problem_text):
    """solution.tex のラベルが、同じ問題の problem.tex のラベルと重複していないか。"""
    errors = []
    problem_labels = {name for command, name, _, _ in tex_references.commands(problem_text)
                      if command == 'label'}
    for command, name, start, _ in tex_references.commands(text):
        if command == 'label' and name in problem_labels:
            errors.append((line_of(text, start), f"\\label{{{name}}} が同じ問題の problem.tex と重複している"))
    return errors


def check_local_references(text, problem_text):
    """ラベル・参照の検査一式（汎用の重複・参照の検査に、problem.tex との重複を加えたもの）。"""
    errors = check_duplicate_labels(text)
    errors += check_problem_label_conflicts(text, problem_text)
    errors += check_equation_references(text, problem_text)
    return errors


class RepoProfile(lint_tex.Profile):
    """このリポジトリ（src/{univ}/{cat}/{year}/{q}/{solution,problem}.tex）の設定。"""

    def default_targets(self):
        return sorted(SRC_DIR.rglob('*.tex'))

    def is_target(self, path):
        return path.name in ('solution.tex', 'problem.tex')

    def label_context(self, path):
        problem = path.with_name('problem.tex') if path.name == 'solution.tex' else None
        if problem and problem.exists():
            return strip_comments(problem.read_text(encoding='utf-8'))
        return ''

    def body_rules_apply(self, path):
        # 年度のまとめ（0/solution.tex）は本文の書き方の検査から外す
        return path.name in ('problem.tex', 'solution.tex') and path.parent.name != '0'

    def reference_errors(self, path, text, context):
        return check_problem_label_conflicts(text, context)

    def errors(self, path, text):
        errors = []
        errors += check_documentclass(text)
        errors += check_proof_env(text)
        if path.name == 'solution.tex':
            errors += check_solution_headings(text)
            if path.parent.name != '0' and path.with_name('problem.tex').exists():
                errors += check_problem_embedded(text)
        if path.name == 'problem.tex':
            errors += check_problem_is_document(text)
            errors += check_problem_figure_float(text)
        return errors

    def edit_finders(self):
        return (_find_solution_heading_edits,)

    def display_path(self, path):
        try:
            return path.relative_to(REPO_ROOT)
        except ValueError:
            return path


PROFILE = RepoProfile()
