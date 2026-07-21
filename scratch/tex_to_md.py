# scratch/tex_to_md.py
import os
import re
import sys
import subprocess
import tempfile
import shutil

# 独自マクロ置換
def preprocess_latex_macros(content):
    # \bm{x} ➔ \mathbf{x} (allowing 1 level of nested braces)
    content = re.sub(r'\\bm\{((?:[^{}]|\{[^{}]*\})*)\}', r'\\mathbf{\1}', content)
    # \shadowbox unwrap (supporting 2 levels of nested braces e.g. tabular specs with p{8cm})
    content = re.sub(r'\\shadowbox\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}', r'\1', content, flags=re.DOTALL)
    # \R ➔ \mathbb{R} (assuring no preceding backslash, e.g. from \\R, but allowing even number of backslashes)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\R(?![a-zA-Z])', r'\1\\mathbb{R}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\C(?![a-zA-Z])', r'\1\\mathbb{C}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\N(?![a-zA-Z])', r'\1\\mathbb{N}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\Z(?![a-zA-Z])', r'\1\\mathbb{Z}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\Q(?![a-zA-Z])', r'\1\\mathbb{Q}', content)
    return content

# TikZを抽出し、SVG画像化してMarkdownの画像タグに置換する
def render_tikz_to_svg(content, uni, category, year, q_num):
    # Astro公開ディレクトリ
    rel_tikz_dir = f"images/tikz/{uni}/{category}/{year}/{q_num}"
    public_tikz_dir = os.path.join("web/public", rel_tikz_dir)
    os.makedirs(public_tikz_dir, exist_ok=True)

    # TikZ環境の抽出
    pattern = re.compile(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', re.DOTALL)
    matches = list(pattern.finditer(content))
    
    for i, m in enumerate(matches):
        tikz_code = m.group(1)
        full_tikz = f"\\begin{{tikzpicture}}{tikz_code}\\end{{tikzpicture}}"
        fig_name = f"fig_{i+1}.svg"
        svg_dest_path = os.path.join(public_tikz_dir, fig_name)
        rel_svg_path = f"/Math-Solutions/{rel_tikz_dir}/{fig_name}"
        
        start_pos = m.start()
        preceding = content[:start_pos]
        fig_start = preceding.rfind(r"\begin{figure}")
        preamble = ""
        if fig_start != -1 and fig_start > content.rfind(r"\end{figure}", 0, start_pos):
            fig_block = preceding[fig_start:start_pos]
            for line in fig_block.splitlines():
                if any(k in line for k in [r"\def", r"\pgfmath", r"\tdplot"]):
                    preamble += line + "\n"

        # 1. 最小限の standalone LaTeX ドキュメントを作成
        standalone_latex = f"""\\documentclass{{standalone}}
\\usepackage{{tikz}}
\\usepackage{{tikz-3dplot}}
\\usepackage{{pgfplots}}
\\pgfplotsset{{compat=1.18}}
\\usetikzlibrary{{angles,quotes,intersections,patterns,calc,arrows.meta,decorations.pathmorphing,decorations.pathreplacing}}
\\usepgfplotslibrary{{fillbetween}}
\\begin{{document}}
{preamble}
{full_tikz}
\\end{{document}}
"""
        # 一時ディレクトリでビルド
        with tempfile.TemporaryDirectory() as tmpdir:
            tex_file = os.path.join(tmpdir, "tikz.tex")
            with open(tex_file, 'w', encoding='utf-8') as f:
                f.write(standalone_latex)
                
            # Compile to PDF using pdflatex or lualatex
            try:
                subprocess.run(
                    ["pdflatex", "-interaction=nonstopmode", "tikz.tex"],
                    cwd=tmpdir, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=True
                )
                pdf_file = os.path.join(tmpdir, "tikz.pdf")
                
                # Convert PDF to SVG using pdftocairo
                subprocess.run(
                    ["pdftocairo", "-svg", pdf_file, svg_dest_path],
                    check=True
                )
            except Exception as e:
                sys.stderr.write(f"Warning: Failed to compile TikZ for {uni}/{category}/{year}/{q_num} {fig_name}: {e}\n")
                continue

        # Markdown/LaTeX画像タグに置換 (最初の1箇所のみ置換)
        latex_image_tag = f"\\includegraphics{{{rel_svg_path}}}"
        content = content.replace(full_tikz, latex_image_tag, 1)
        
    return content

def preprocess_latex(content, uni="test", category="test", year="test", q_num="test"):
    content = preprocess_latex_macros(content)
    content = render_tikz_to_svg(content, uni, category, year, q_num)
    return content

def convert_tex_to_md(tex_path, output_md_path, frontmatter, uni, category, year, q_num):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # マクロ置換 & TikZ置換
    processed_content = preprocess_latex(content, uni, category, year, q_num)
    
    # テンポラリファイルを作成してPandocで変換
    temp_tex = tex_path + ".temp.tex"
    with open(temp_tex, 'w', encoding='utf-8') as f:
        f.write(processed_content)
        
    try:
        cmd = ["pandoc", temp_tex, "-t", "markdown", "--mathjax"]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        md_body = result.stdout
    finally:
        if os.path.exists(temp_tex):
            os.remove(temp_tex)

    # Markdown後処理 (KaTeXの二重$$囲み、Pandoc参照属性、非標準:::コンテナの修正)
    md_body = postprocess_markdown(md_body)

    # Frontmatterを付与して保存
    fm_str = "---\n"
    for k, v in frontmatter.items():
        # クォートのエスケープ
        escaped_v = str(v).replace('"', '\\"')
        fm_str += f"{k}: \"{escaped_v}\"\n"
    fm_str += "---\n\n"
    
    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(fm_str + md_body)

def postprocess_markdown(md_body):
    # 1. $$\begin{align} ... \end{align}$$ の二重$$囲みを修正 (\begin{align} / \begin{aligned} は単体で動く)
    md_body = re.sub(r'\$\$\s*(\\begin\{(?:align|align\*|aligned|aligned\*|gather|gather\*|eqnarray|eqnarray\*)\})', r'\1', md_body)
    md_body = re.sub(r'(\\end\{(?:align|align\*|aligned|aligned\*|gather|gather\*|eqnarray|eqnarray\*)\})\s*\$\$', r'\1', md_body)

    # 2. \label{...} と \nonumber の除去 (KaTeXパースエラーの防止)
    md_body = re.sub(r'\\label\{[^}]+\}', '', md_body)
    md_body = re.sub(r'\\nonumber\b', '', md_body)

    # 3. Pandocの生参照属性記号やラベル残骸 (例: \(1990-1:eq:1\)) の除去・式番号整形
    md_body = re.sub(r'\\\([a-zA-Z0-9_-]+:eq:(\d+)\\\)', r'(式\1)', md_body)
    md_body = re.sub(r'\([a-zA-Z0-9_-]+:eq:(\d+)\\?\)', r'(式\1)', md_body)
    md_body = re.sub(r'\[\\?\[([^\]]+)\\?\]\]\([^)]+\)\{reference-type="[^"]*"[^}]*\}', r'(\1)', md_body)
    md_body = re.sub(r'\[([^\]]+)\]\([^)]+\)\{reference-type="[^"]*"[^}]*\}', r'\1', md_body)
    md_body = re.sub(r'\{reference-type="[^"]*"[^}]*\}', '', md_body)

    # 4. Pandoc ::: コンテナ (oframed, multicols) のクリーンアップ
    md_body = re.sub(r'^:::\s*(?:oframed|multicols.*)?\s*$', '', md_body, flags=re.MULTILINE)

    # 5. 冒頭の「2 **\[解\]**」などの不要な数字とエスケープブラケットの整形
    md_body = re.sub(r'^\s*\d+\s*\*\*\\?\[解\\?\]\*\*', r'**【解】**', md_body, flags=re.MULTILINE)
    md_body = re.sub(r'\*\*\\?\[解\\?\]\*\*', r'**【解】**', md_body)
    md_body = re.sub(r'\*\*\\?\[解説\\?\]\*\*', r'**【解説】**', md_body)
    md_body = re.sub(r'\*\*\\?\[方針\\?\]\*\*', r'**【方針】**', md_body)

    # 6. \bm{...} の残骸等の処理
    md_body = re.sub(r'\\bm\{((?:[^{}]|\{[^{}]*\})*)\}', r'\\mathbf{\1}', md_body)
    
    return md_body

def process_all_src():
    src_root = "src"
    dest_root = "web/src/content/solutions"
    has_errors = False
    
    for root, _, files in os.walk(src_root):
        for file in files:
            if file in ("problem.tex", "solution.tex"):
                parts = os.path.normpath(root).split(os.sep)
                # 深さ制限チェック（5番目の要素まで）
                if len(parts) == 5: 
                    uni, category, year, q_num = parts[1], parts[2], parts[3], parts[4]
                    if q_num == "0":
                        type_str = "summary"
                        title_str = f"{year}年 全体サマリ"
                    else:
                        type_str = "problem" if file == "problem.tex" else "solution"
                        title_str = f"{uni.upper()} {year} {category} Q{q_num} ({type_str})"
                    
                    base_name = f"{uni}-{category}-{year}-{q_num}"
                    output_name = f"{base_name}-{type_str}.md"
                    output_path = os.path.join(dest_root, output_name)
                    
                    fm = {
                        "university": uni,
                        "category": category,
                        "year": year,
                        "question": q_num,
                        "type": type_str,
                        "title": title_str
                    }
                    
                    try:
                        convert_tex_to_md(os.path.join(root, file), output_path, fm, uni, category, year, q_num)
                    except Exception as e:
                        sys.stderr.write(f"Error converting {os.path.join(root, file)}: {e}\n")
                        has_errors = True
                        
    if has_errors:
        sys.exit(1)

if __name__ == "__main__":
    process_all_src()
