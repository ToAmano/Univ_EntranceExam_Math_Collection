import os
import sys
import re
import subprocess
import shutil
from TexSoup import TexSoup

def compile_tikz_to_svg(tikz_code, output_svg_path, macro_defs=""):
    """
    TikZコードと大問レベルのマクロ定義を組み合わせてスタンドアロンSVG画像を生成する
    """
    temp_dir = os.path.join("scratch", "tikz_build")
    os.makedirs(temp_dir, exist_ok=True)
    tex_filename = os.path.join(temp_dir, "fig.tex")
    pdf_filename = os.path.join(temp_dir, "fig.pdf")

    full_tex = f"""\\documentclass[tikz,border=2pt]{{standalone}}
\\usepackage{{amsmath,amssymb,amsfonts,amsthm}}
\\usepackage{{tikz,pgfplots}}
\\usepackage{{tikz-3dplot}}
\\usetikzlibrary{{arrows.meta,calc,intersections,patterns,angles,quotes,through}}
\\pgfplotsset{{compat=1.18}}

{macro_defs}

\\begin{{document}}
{tikz_code}
\\end{{document}}
"""

    with open(tex_filename, 'w', encoding='utf-8') as f:
        f.write(full_tex)

    try:
        cmd_compile = ["latexmk", "-lualatex", "-interaction=batchmode", "-output-directory=" + temp_dir, tex_filename]
        res_compile = subprocess.run(cmd_compile, capture_output=True, text=True)
        if res_compile.returncode != 0:
            cmd_compile_pdf = ["pdflatex", "-interaction=batchmode", "-output-directory=" + temp_dir, tex_filename]
            subprocess.run(cmd_compile_pdf, capture_output=True, text=True)

        if not os.path.exists(pdf_filename):
            print(f"Failed to produce PDF for TikZ figure at {output_svg_path}")
            return False

        cmd_svg = ["dvisvgm", "--pdf", "--no-fonts", "-o", output_svg_path, pdf_filename]
        res_svg = subprocess.run(cmd_svg, capture_output=True, text=True)
        return res_svg.returncode == 0
    except Exception as e:
        print(f"Error compiling TikZ to SVG: {e}")
        return False

def convert_tex_with_texsoup(tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir):
    with open(tex_path, 'r', encoding='utf-8') as f:
        raw_tex = f.read()

    macro_defs = "\n".join(re.findall(r'(\\(?:def|pgfmath|tdplot)[^\n]+)', raw_tex))

    if '\\begin{document}' in raw_tex:
        m = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', raw_tex, re.DOTALL)
        if m:
            raw_tex = m.group(1)

    raw_tex = re.sub(r'\\rhead\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\begin\{oframed\}\s*\\input\{[^}]+\}\s*\\end\{oframed\}', '', raw_tex)
    raw_tex = re.sub(r'\\setlength\{[^}]*\}\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\begin\{multicols\}\{\d+\}', '', raw_tex)
    raw_tex = re.sub(r'\\end\{multicols\}', '', raw_tex)
    raw_tex = re.sub(r'\\newpage', '', raw_tex)
    raw_tex = re.sub(r'\\vspace\{[^}]*\}', '', raw_tex)

    soup = TexSoup(raw_tex)

    # 1. \cref ノードの標準化
    for cref in list(soup.find_all('cref')):
        if cref.args:
            target = str(cref.args[0]).strip('{}')
            if 'fig:' in target:
                cref.replace_with(f'$\\ref{{{target}}}$')
            else:
                cref.replace_with(f'$\\eqref{{{target}}}$')

    # 2. figure 環境（TikZ図）のビルドと HTML <figure> タグ置換
    fig_count = 1
    os.makedirs(output_svg_dir, exist_ok=True)
    for fig in list(soup.find_all('figure')):
        caption_node = fig.find('caption')
        label_node = fig.find('label')
        
        caption_text = str(caption_node.args[0]).strip('{}') if caption_node and caption_node.args else ''
        label_id = str(label_node.args[0]).strip('{}') if label_node and label_node.args else f'fig_{fig_count}'

        tikz_node = fig.find('tikzpicture')
        if tikz_node:
            tikz_code = str(tikz_node)
            svg_filename = f"fig_{fig_count}.svg"
            svg_dest_path = os.path.join(output_svg_dir, svg_filename)
            compile_tikz_to_svg(tikz_code, svg_dest_path, macro_defs)

            web_img_src = f"{public_img_dir_rel}/{svg_filename}"
            fig_html = f'\n<figure id="{label_id}">\n  <img src="{web_img_src}" />\n  <figcaption>{caption_text}</figcaption>\n</figure>\n'
            fig.replace_with(fig_html)
            fig_count += 1

    # 3. \begin{enumerate} リスト置換
    for enum in list(soup.find_all('enumerate')):
        items = enum.find_all('item')
        list_md = []
        for i, item in enumerate(items, 1):
            item_text = str(item).replace('\\item', '').strip()
            list_md.append(f"{i}.  {item_text}")
        enum.replace_with('\n\n' + '\n\n'.join(list_md) + '\n\n')

    # 4. align / align* / gather / gather* 数式ブロック置換
    for math_env in list(soup.find_all(['align', 'align*', 'gather', 'gather*', 'eqnarray', 'eqnarray*'])):
        env_name = math_env.name
        body = []
        for child in math_env.contents:
            body.append(str(child))
        align_str = ''.join(body).strip()
        math_env.replace_with(f'\n$$\n\\begin{{{env_name}}}\n{align_str}\n\\end{{{env_name}}}\n$$\n')

    md_body = str(soup)

    # 見出しと見映えの整形
    md_body = re.sub(r'\{\\bf\s*\\?\[解\\?\]\}', r'**【解】**', md_body)
    md_body = re.sub(r'\{\\bf\s*\\?\[解説\\?\]\}', r'**【解説】**', md_body)
    md_body = re.sub(r'\{\\bf\s*\\?\[方針\\?\]\}', r'**【方針】**', md_body)

    # 小設問 (1), (2) などの見出し化
    md_body = re.sub(r'^\s*\(([0-9]+)\)', r'\n### (\1)\n', md_body, flags=re.MULTILINE)

    # 連続する空行を縮小
    md_body = re.sub(r'\n{3,}', '\n\n', md_body).strip()

    fm_str = "---\n"
    for k, v in frontmatter.items():
        escaped_v = str(v).replace('"', '\\"')
        fm_str += f'{k}: "{escaped_v}"\n'
    fm_str += "---\n\n"

    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(fm_str + md_body)

def process_all_src():
    src_root = "src"
    dest_root = "web/src/content/solutions"

    for root, _, files in os.walk(src_root):
        for file in files:
            if file in ("problem.tex", "solution.tex"):
                parts = os.path.normpath(root).split(os.sep)
                if len(parts) == 5:
                    uni, category, year, q_num = parts[1], parts[2], parts[3], parts[4]
                    if q_num == "0":
                        type_str = "summary"
                        title_str = f"{year}年 全体サマリ"
                    else:
                        type_str = "problem" if file == "problem.tex" else "solution"
                        title_str = f"{uni.upper()} {year} {category} Q{q_num} ({type_str})"

                    frontmatter = {
                        "university": uni,
                        "category": category,
                        "year": year,
                        "question": q_num,
                        "type": type_str,
                        "title": title_str
                    }

                    filename = f"{uni}-{category}-{year}-{q_num}-{type_str}.md"
                    output_md_path = os.path.join(dest_root, filename)

                    public_img_dir_rel = f"/Univ_EntranceExam_Math_Collection/images/tikz/{uni}/{category}/{year}/{q_num}"
                    output_svg_dir = os.path.join("web", "public", "images", "tikz", uni, category, year, q_num)

                    tex_path = os.path.join(root, file)
                    print(f"Converting AST: {tex_path} -> {output_md_path}")
                    convert_tex_with_texsoup(tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir)

if __name__ == '__main__':
    process_all_src()
