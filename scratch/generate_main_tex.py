"""
大学/区分（例: titech/kouki）ごとに 1 つの main.tex を生成する。

- kouki 系（problem.tex が中身のみのフラグメントで、solution.tex 側の
  \\begin{oframed}\\input{problem.tex}\\end{oframed} で問題文を埋め込む構成）は
  solution.tex を \\subfile するだけで問題文＋解答が両方載る。
- zenki 系（problem.tex 自体が \\documentclass[...]{subfiles} の独立文書）は
  problem.tex を \\subfile し、solution.tex が同じく subfiles 形式で存在すれば
  続けて \\subfile する。

各 q_num の書式は個々のファイルの実際の \\documentclass 行を見て自動判定するため、
将来 zenki 側の solution.tex が subfiles 形式に統一されていっても、
このスクリプトを再実行するだけで main.tex に自動的に取り込まれる。
"""
import os
import re
import sys

SRC_ROOT = "src"
UNIV_CATS = [
    ("titech", "kouki"),
    ("titech", "zenki"),
    ("utokyo", "kouki"),
    ("utokyo", "zenki"),
    ("ukyoto", "kouki"),
    ("ukyoto", "zenki"),
]

UNIV_LABEL = {"titech": "東京工業大学", "utokyo": "東京大学", "ukyoto": "京都大学"}
CAT_LABEL = {"kouki": "後期", "zenki": "前期"}

SUBFILES_RE = re.compile(r'\\documentclass\[[^\]]*main\.tex[^\]]*\]\{subfiles\}')

PREAMBLE = r"""\documentclass[a4paper,10pt]{ltjsarticle}
\usepackage{luatexja}
\usepackage[haranoaji]{luatexja-preset}
\usepackage{luatexja-ruby}
\usepackage[truedimen,top=25truemm,bottom=20truemm,left=15truemm,right=15truemm]{geometry}
\usepackage{amsmath,amssymb,amsfonts,amsthm,mathtools}
\usepackage{cases}
\usepackage{physics}
\usepackage{array}
\usepackage{float}
\usepackage{caption}
\usepackage{subcaption}
\usepackage{tcolorbox}
\tcbuselibrary{most}
\usepackage{pifont}
\usepackage{diagbox}
\usepackage{fancybox}
\usepackage{framed}
\usepackage{multicol}
\usepackage{multirow}
\usepackage{enumerate}
\usepackage{fancyhdr}
\usepackage{cleveref}
\usepackage{bm}
\usepackage{tikz,pgfplots}
\usepackage{tikz-3dplot}
\usetikzlibrary{arrows.meta,calc,intersections,patterns,patterns.meta,angles,quotes,through,positioning,decorations.pathmorphing,decorations.markings,math,3d,perspective,shapes.geometric,backgrounds}
\usepgfplotslibrary{fillbetween,colormaps,groupplots}
\pgfplotsset{compat=1.18}
% tdplot_main_coords スタイルを使う figure が \tdplotsetmaincoords を呼び忘れている
% 場合のフォールバック（各 figure 側で呼んでいれば上書きされる）
\tdplotsetmaincoords{70}{110}

% 手書き解答からの移行元ソースで使われている略記マクロ
\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\Q}{\mathbb{Q}}
\newtheorem{lemma}{補題}
% 増減表用の矢印記号を使っているが定義されていないソースがあるためのフォールバック
\providecommand{\roundedArrowDR}{\searrow}
\providecommand{\roundedArrowUR}{\nearrow}
\providecommand{\roundedArrowRU}{\nearrow}
\providecommand{\roundedArrowDL}{\swarrow}
\providecommand{\roundedArrowUL}{\nwarrow}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[R]{\slshape\leftmark}
\fancyfoot[C]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}

\usepackage{subfiles}

\title{{{TITLE}}}
\author{}
\date{}

\begin{document}
\maketitle
\tableofcontents
\clearpage
"""


def is_subfiles(path):
    if not os.path.isfile(path):
        return False
    with open(path, encoding="utf-8", errors="ignore") as f:
        head = f.read(500)
    return bool(SUBFILES_RE.search(head))


def collect_years(base):
    years = []
    for name in os.listdir(base):
        full = os.path.join(base, name)
        if os.path.isdir(full) and name.isdigit():
            years.append(name)
    return sorted(years, key=int)


def collect_questions(year_dir):
    qs = []
    for name in os.listdir(year_dir):
        full = os.path.join(year_dir, name)
        if os.path.isdir(full) and name.isdigit():
            qs.append(name)
    return sorted(qs, key=int)


def generate_category(univ, cat):
    base = os.path.join(SRC_ROOT, univ, cat)
    if not os.path.isdir(base):
        print(f"skip {univ}/{cat}: no such directory")
        return None

    body_lines = []
    included = 0
    skipped = []

    for year in collect_years(base):
        year_dir = os.path.join(base, year)
        questions = collect_questions(year_dir)
        if not questions:
            continue

        year_body = []
        for q in questions:
            qdir = os.path.join(year_dir, q)
            problem = os.path.join(qdir, "problem.tex")
            solution = os.path.join(qdir, "solution.tex")
            rel_problem = f"{year}/{q}/problem"
            rel_solution = f"{year}/{q}/solution"

            if q == "0":
                if is_subfiles(solution):
                    year_body.append(f"\\subfile{{{rel_solution}}}")
                    year_body.append("\\clearpage")
                    included += 1
                else:
                    skipped.append((year, q, "summary solution.tex missing/not subfiles"))
                continue

            label = f"{UNIV_LABEL[univ]}{CAT_LABEL[cat]} {year}年 第{q}問"

            if is_subfiles(solution) and not is_subfiles(problem):
                # kouki 形式: solution.tex が内部で problem.tex を \input している
                year_body.append(f"\\rhead{{{label}}}")
                year_body.append(f"\\subfile{{{rel_solution}}}")
                included += 1
            elif is_subfiles(problem):
                # zenki 形式: problem.tex 自体が独立した subfiles 文書
                year_body.append(f"\\rhead{{{label}}}")
                year_body.append(f"\\subfile{{{rel_problem}}}")
                if is_subfiles(solution):
                    year_body.append(f"\\subfile{{{rel_solution}}}")
                year_body.append("\\clearpage")
                included += 1
            else:
                skipped.append((year, q, "neither problem.tex nor solution.tex is in subfiles format"))

        if year_body:
            body_lines.append(f"\\section*{{{year}年}}")
            body_lines.append(f"\\addcontentsline{{toc}}{{section}}{{{year}年}}")
            body_lines.extend(year_body)

    title = f"{UNIV_LABEL[univ]} {CAT_LABEL[cat]} 数学 過去問解答集"
    preamble = PREAMBLE.replace("{TITLE}", title)
    content = preamble + "\n" + "\n".join(body_lines) + "\n\\end{document}\n"

    out_path = os.path.join(base, "main.tex")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{univ}/{cat}: wrote {out_path} ({included} 問収録, {len(skipped)} 件スキップ)")
    if skipped:
        for year, q, reason in skipped[:10]:
            print(f"    skip {year}/{q}: {reason}")
        if len(skipped) > 10:
            print(f"    ... and {len(skipped) - 10} more")
    return out_path


def main():
    targets = UNIV_CATS
    if len(sys.argv) > 1:
        univ, cat = sys.argv[1].split("/")
        targets = [(univ, cat)]
    for univ, cat in targets:
        generate_category(univ, cat)


if __name__ == "__main__":
    main()
