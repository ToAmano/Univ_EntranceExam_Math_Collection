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
    # \R ➔ \mathbb{R} (assuring no preceding backslash, e.g. from \\R, but allowing even number of backslashes)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\R(?![a-zA-Z])', r'\1\\mathbb{R}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\C(?![a-zA-Z])', r'\1\\mathbb{C}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\N(?![a-zA-Z])', r'\1\\mathbb{N}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\Z(?![a-zA-Z])', r'\1\\mathbb{Z}', content)
    content = re.sub(r'(?<!\\)((?:\\\\)*)\\Q(?![a-zA-Z])', r'\1\\mathbb{Q}', content)
    return content

# TikZを抽出し、SVG画像化してMarkdownの画像タグに置換する
def render_tikz_to_svg(content, base_name):
    # Astro公開ディレクトリ
    public_tikz_dir = "web/public/images/tikz"
    os.makedirs(public_tikz_dir, exist_ok=True)

    # TikZ環境の抽出
    pattern = re.compile(r'\\begin\{tikzpicture\}(.*?)\\end\{tikzpicture\}', re.DOTALL)
    matches = pattern.findall(content)
    
    for i, tikz_code in enumerate(matches):
        full_tikz = f"\\begin{{tikzpicture}}{tikz_code}\\end{{tikzpicture}}"
        fig_id = f"{base_name}_tikz_{i+1}"
        svg_filename = f"{fig_id}.svg"
        svg_dest_path = os.path.join(public_tikz_dir, svg_filename)
        
        # 1. 最小限の standalone LaTeX ドキュメントを作成
        standalone_latex = f"""\\documentclass{{standalone}}
\\usepackage{{tikz}}
\\usepackage{{pgfplots}}
\\pgfplotsset{{compat=1.18}}
\\usetikzlibrary{{angles,quotes,intersections,patterns}}
\\usepgfplotslibrary{{fillbetween}}
\\begin{{document}}
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
                sys.stderr.write(f"Warning: Failed to compile TikZ for {fig_id}: {e}\n")
                # 失敗時はプレースホルダー画像を配置するか、元のコードのままとする
                continue

        # Markdown/LaTeX画像タグに置換 (最初の1箇所のみ置換)
        latex_image_tag = f"\\includegraphics{{/Math-Solutions/images/tikz/{svg_filename}}}"
        content = content.replace(full_tikz, latex_image_tag, 1)
        
    return content

def preprocess_latex(content, base_name="test"):
    content = preprocess_latex_macros(content)
    content = render_tikz_to_svg(content, base_name)
    return content

def convert_tex_to_md(tex_path, output_md_path, frontmatter, base_name):
    with open(tex_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # マクロ置換 & TikZ置換
    processed_content = preprocess_latex(content, base_name)
    
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
                    type_str = "problem" if file == "problem.tex" else "solution"
                    
                    base_name = f"{uni}-{category}-{year}-{q_num}"
                    output_name = f"{base_name}-{type_str}.md"
                    output_path = os.path.join(dest_root, output_name)
                    
                    fm = {
                        "university": uni,
                        "category": category,
                        "year": year,
                        "question": q_num,
                        "type": type_str,
                        "title": f"{uni.upper()} {year} {category} Q{q_num} ({type_str})"
                    }
                    
                    try:
                        convert_tex_to_md(os.path.join(root, file), output_path, fm, base_name)
                    except Exception as e:
                        sys.stderr.write(f"Error converting {os.path.join(root, file)}: {e}\n")
                        has_errors = True
                        
    if has_errors:
        sys.exit(1)

if __name__ == "__main__":
    process_all_src()
