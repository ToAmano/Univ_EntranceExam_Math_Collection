import os
import sys
import re
import subprocess
import shutil
import pypandoc
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

def convert_tex_hybrid(tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir):
    with open(tex_path, 'r', encoding='utf-8') as f:
        raw_tex = f.read()

    # 1. 冒頭・末尾のドキュメントタグや不要なプリアンブルコメントの事前整理
    if '\\begin{document}' in raw_tex:
        m = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', raw_tex, re.DOTALL)
        if m:
            raw_tex = m.group(1)

    # % コメント行の除去
    lines = []
    for line in raw_tex.splitlines():
        line_strip = line.strip()
        if line_strip.startswith('%'):
            continue
        # インラインコメント % ... の削除（\% は保持）
        line_clean = re.sub(r'(?<!\\)%.*', '', line)
        lines.append(line_clean)
    raw_tex = "\n".join(lines)

    # マクロ定義の事前収集 (TikZ用)
    macro_defs = "\n".join(re.findall(r'(\\(?:def|pgfmath|tdplot)[^\n]+)', raw_tex))

    # 不要なレイアウトコマンドの除去
    raw_tex = re.sub(r'\\rhead\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\begin\{oframed\}\s*\\input\{[^}]+\}\s*\\end\{oframed\}', '', raw_tex)
    raw_tex = re.sub(r'\\setlength\{[^}]*\}\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\begin\{multicols\}\{\d+\}', '', raw_tex)
    raw_tex = re.sub(r'\\end\{multicols\}', '', raw_tex)
    raw_tex = re.sub(r'\\newpage', '', raw_tex)
    raw_tex = re.sub(r'\\vspace\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\noindent', '', raw_tex)
    raw_tex = re.sub(r'\\fontsize\{[^}]*\}\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\selectfont', '', raw_tex)

    # 2. TexSoup による構造化エレメントのピンポイント事前変換
    soup = TexSoup(raw_tex)

    # shadowbox 枠のアンラップ
    for sbox in list(soup.find_all('shadowbox')):
        if sbox.args:
            sbox.replace_with(str(sbox.args[0]).strip('{}'))

    fig_map = {}
    fig_count = 1
    os.makedirs(output_svg_dir, exist_ok=True)

    # figure 環境（TikZ図）のビルドと HTML <figure> ノード置換
    for fig in list(soup.find_all('figure')):
        caption_node = fig.find('caption')
        label_node = fig.find('label')
        
        caption_text = str(caption_node.args[0]).strip('{}') if caption_node and caption_node.args else ''
        label_id = str(label_node.args[0]).strip('{}') if label_node and label_node.args else f'fig_{fig_count}'

        fig_map[label_id] = fig_count

        tikz_node = fig.find('tikzpicture')
        if tikz_node:
            tikz_code = str(tikz_node)
            svg_filename = f"fig_{fig_count}.svg"
            svg_dest_path = os.path.join(output_svg_dir, svg_filename)
            compile_tikz_to_svg(tikz_code, svg_dest_path, macro_defs)

            web_img_src = f"{public_img_dir_rel}/{svg_filename}"
            caption_label = f"図 {fig_count}" + (f": {caption_text}" if caption_text else "")
            fig_html = f'\n<figure id="{label_id}">\n  <img src="{web_img_src}" alt="図 {fig_count}" />\n  <figcaption>{caption_label}</figcaption>\n</figure>\n'
            fig.replace_with(fig_html)
            fig_count += 1

    # TexSoup で前処理された TeX 文字列
    preprocessed_tex = str(soup)

    # 行頭の多すぎるインデント（4スペース以上）の除去（Markdownコードブロック化防止）
    clean_lines = []
    for l in preprocessed_tex.splitlines():
        clean_lines.append(l.lstrip())
    preprocessed_tex = "\n".join(clean_lines)

    # 3. Pandoc による本文・表 (tabular)・リストの一括自動変換
    try:
        md_content = pypandoc.convert_text(preprocessed_tex, 'markdown+raw_html-smart', format='latex')
    except Exception as e:
        print(f"Pandoc fallback warning for {tex_path}: {e}")
        md_content = preprocessed_tex

    # Pandoc が吐き出した \{reference-type...\} 属性のクリーンアップ
    md_content = re.sub(r'\{reference-type="[^"]*"\s*reference="[^"]*"\}', '', md_content)
    md_content = re.sub(r'\[\\\[([^\]]+)\\\]\]', r'[\1]', md_content)

    # 4. \cref / \ref のアンカーリンク置換 (Pandoc変換後)
    for ref_node in list(soup.find_all(['cref', 'ref'])):
        if ref_node.args:
            target = str(ref_node.args[0]).strip('{}')
            raw_target_link = f'[{target}](#{target})'
            if 'fig:' in target or target in fig_map:
                fig_num = fig_map.get(target, 1)
                link_str = f'[図{fig_num}](#{target})'
                md_content = md_content.replace(raw_target_link, link_str)
            else:
                eq_str = f'$\\eqref{{{target}}}$'
                md_content = md_content.replace(raw_target_link, eq_str)

    # HTML <figure> タグのエスケープ解除
    md_content = md_content.replace(r'\<figure', '<figure').replace(r'\</figure\>', '</figure>')
    md_content = md_content.replace(r'\<img', '<img').replace(r'/\>', '/>')
    md_content = md_content.replace(r'\<figcaption\>', '<figcaption>').replace(r'\</figcaption\>', '</figcaption>')

    # 4. 見映えと表記の最終整頓
    md_content = re.sub(r'\{\\bf\s*\\?\[解\\?\]\}|\*\*\[解\]\*\*', r'**【解】**', md_content)
    md_content = re.sub(r'\{\\bf\s*\\?\[解説\\?\]\}|\*\*\[解説\]\*\*', r'**【解説】**', md_content)
    md_content = re.sub(r'\{\\bf\s*\\?\[方針\\?\]\}|\*\*\[方針\]\*\*', r'**【方針】**', md_content)

    # 小設問 (1), (2) などの見出し化
    md_content = re.sub(r'^\s*\(([0-9]+)\)', r'\n### (\1)\n', md_content, flags=re.MULTILINE)

    # 連続する空行のトリム
    md_content = re.sub(r'\n{3,}', '\n\n', md_content).strip()

    fm_str = "---\n"
    for k, v in frontmatter.items():
        escaped_v = str(v).replace('"', '\\"')
        fm_str += f'{k}: "{escaped_v}"\n'
    fm_str += "---\n\n"

    os.makedirs(os.path.dirname(output_md_path), exist_ok=True)
    with open(output_md_path, 'w', encoding='utf-8') as f:
        f.write(fm_str + md_content)

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
                    print(f"Converting Hybrid: {tex_path} -> {output_md_path}")
                    convert_tex_hybrid(tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir)

if __name__ == '__main__':
    process_all_src()
