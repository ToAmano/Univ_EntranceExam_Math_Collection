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
    pdftocairo (Poppler) を最優先で使用し、完璧なベクトル描画を行う
    """
    temp_dir = os.path.join("scratch", "tikz_build")
    os.makedirs(temp_dir, exist_ok=True)
    tex_filename = os.path.join(temp_dir, "fig.tex")
    pdf_filename = os.path.join(temp_dir, "fig.pdf")

    full_tex = f"""\\documentclass[tikz,border=2pt]{{standalone}}
\\usepackage{{amsmath,amssymb,amsfonts,amsthm}}
\\usepackage{{tikz,pgfplots}}
\\usepackage{{tikz-3dplot}}
\\usetikzlibrary{{arrows.meta,calc,intersections,patterns,patterns.meta,angles,quotes,through,positioning,decorations.pathmorphing,decorations.markings}}
\\usepgfplotslibrary{{fillbetween,colormaps}}
\\pgfplotsset{{compat=1.18}}

{macro_defs}

\\begin{{document}}
{tikz_code}
\\end{{document}}
"""

    with open(tex_filename, 'w', encoding='utf-8') as f:
        f.write(full_tex)

    try:
        # 1. LuaLaTeX または pdflatex で高品質 PDF の作成
        cmd_compile_pdf = ["lualatex", "-interaction=batchmode", "-output-directory=" + temp_dir, tex_filename]
        subprocess.run(cmd_compile_pdf, capture_output=True, text=True)

        if not os.path.exists(pdf_filename):
            cmd_pdflatex = ["pdflatex", "-interaction=batchmode", "-output-directory=" + temp_dir, tex_filename]
            subprocess.run(cmd_pdflatex, capture_output=True, text=True)

        if not os.path.exists(pdf_filename):
            print(f"Failed to produce PDF for TikZ figure at {output_svg_path}")
            return False

        # 2. pdftocairo (Poppler) による完璧な SVG 変換
        pdftocairo_bin = shutil.which("pdftocairo") or "/opt/homebrew/bin/pdftocairo"
        if os.path.exists(pdftocairo_bin):
            cmd_svg = [pdftocairo_bin, "-svg", pdf_filename, output_svg_path]
            subprocess.run(cmd_svg, capture_output=True, text=True)

        # 3. pdf2svg フォールバック
        if not os.path.exists(output_svg_path) and shutil.which("pdf2svg"):
            cmd_svg = ["pdf2svg", pdf_filename, output_svg_path]
            subprocess.run(cmd_svg, capture_output=True, text=True)

        # 4. dvisvgm フォールバック
        if not os.path.exists(output_svg_path) and shutil.which("dvisvgm"):
            cmd_svg = ["dvisvgm", "--pdf", "--no-fonts", "-o", output_svg_path, pdf_filename]
            subprocess.run(cmd_svg, capture_output=True, text=True)

        return os.path.exists(output_svg_path)
    except Exception as e:
        print(f"Error compiling TikZ to SVG: {e}")
        return False

def convert_tex_clean(tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir):
    with open(tex_path, 'r', encoding='utf-8') as f:
        raw_tex = f.read()

    # 1. 冒頭・末尾のドキュメント構造・不要コマンドの削除
    if '\\begin{document}' in raw_tex:
        m = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', raw_tex, re.DOTALL)
        if m:
            raw_tex = m.group(1)

    # % コメント行の削除
    clean_lines = []
    for line in raw_tex.splitlines():
        line_s = line.strip()
        if line_s.startswith('%'):
            continue
        line_clean = re.sub(r'(?<!\\)%.*', '', line)
        clean_lines.append(line_clean)
    raw_tex = "\n".join(clean_lines)

    macro_defs = "\n".join(re.findall(r'(\\(?:def|pgfmath|tdplot)[^\n]+)', raw_tex))

    # 不要なレイアウトマクロの削除
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
    raw_tex = re.sub(r'\\centerline', '', raw_tex)

    # 3. tabular 環境の pypandoc による完全自動 Markdown 表変換
    def convert_tabular_block(tab_input):
        tab_str = tab_input.group(0) if hasattr(tab_input, 'group') else str(tab_input)
        # Pandoc が HTML <table> にエスケープする原因となる multirow / multicolumn マクロの展開
        tab_clean = re.sub(r'\\multirow\{[^}]*\}\{[^}]*\}', '', tab_str)
        tab_clean = re.sub(r'\\multicolumn\{[^}]*\}\{[^}]*\}', '', tab_clean)
        # standalone tabular 文脈を構築して Pandoc に入力
        wrapped_tex = f"\\documentclass{{article}}\n\\begin{{document}}\n{tab_clean}\n\\end{{document}}"
        try:
            md_table = pypandoc.convert_text(wrapped_tex, 'gfm', format='latex')
            clean_table_lines = []
            for line in md_table.splitlines():
                if line.strip().startswith('|'):
                    # $`math`$ 形式を通常の $math$ に変換
                    line_clean = re.sub(r'\$`([^`]+)`\$', r'$\1$', line)
                    clean_table_lines.append(line_clean)
            if clean_table_lines:
                return "\n\n" + "\n".join(clean_table_lines).strip() + "\n\n"
            return "\n\n" + tab_str + "\n\n"
        except Exception as e:
            print(f"Pandoc table conversion warning: {e}")
            return tab_str

    fig_count = 1
    fig_map = {}
    tab_count = 1
    tab_map = {}

    try:
        soup = TexSoup(raw_tex, tolerance=1)

        # 4. table 環境の HTML/Markdown ノード置換
        tables = list(soup.find_all('table'))
        for tbl in tables:
            caption_node = tbl.find('caption')
            label_node = tbl.find('label')

            caption_text = str(caption_node.args[0]).strip('{}') if caption_node and caption_node.args else ''
            label_id = str(label_node.args[0]).strip('{}') if label_node and label_node.args else f'tab_{tab_count}'

            tab_map[label_id] = tab_count

            tbl_str = str(tbl)
            tabular_html = ""
            m_tab = re.search(r'\\begin\{tabular\}.*?\\end\{tabular\}', tbl_str, re.DOTALL)
            if m_tab:
                tabular_html = convert_tabular_block(m_tab.group(0))

            if caption_text:
                caption_label = f"表 {tab_count}" + (f": {caption_text}" if caption_text else "")
                tbl_html = f'\n\n<figure id="{label_id}" class="table-wrapper">\n{tabular_html}\n  <figcaption>{caption_label}</figcaption>\n</figure>\n\n'
            else:
                tbl_html = f'\n\n<div id="{label_id}" class="table-wrapper">\n{tabular_html}\n</div>\n\n'

            tbl.replace_with(tbl_html)
            tab_count += 1

        # 5. figure 環境の SVG ビルドと HTML <figure> ノード置換
        figs = list(soup.find_all('figure'))
        for fig in figs:
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
                os.makedirs(output_svg_dir, exist_ok=True)
                compile_tikz_to_svg(tikz_code, svg_dest_path, macro_defs)

                web_img_src = f"{public_img_dir_rel}/{svg_filename}"
                caption_label = f"図 {fig_count}" + (f": {caption_text}" if caption_text else "")
                fig_html = f'\n\n<figure id="{label_id}">\n  <img src="{web_img_src}" alt="図 {fig_count}" />\n  <figcaption>{caption_label}</figcaption>\n</figure>\n\n'
                fig.replace_with(fig_html)
                fig_count += 1

        # 6. \cref / \ref ノード置換 (図・表のスマート参照)
        for ref_node in list(soup.find_all(['cref', 'ref'])):
            if ref_node.args:
                target = str(ref_node.args[0]).strip('{}')
                if 'fig:' in target or target in fig_map:
                    fig_num = fig_map.get(target, 1)
                    ref_node.replace_with(f'[図{fig_num}](#{target})')
                elif 'tab:' in target or target in tab_map:
                    tab_num = tab_map.get(target, 1)
                    ref_node.replace_with(f'[表{tab_num}](#{target})')
                else:
                    ref_node.replace_with(f'$\\eqref{{{target}}}$')

        # 6. \begin{enumerate} リスト置換
        for enum in list(soup.find_all('enumerate')):
            items = enum.find_all('item')
            list_md = []
            for i, item in enumerate(items, 1):
                item_text = str(item).replace('\\item', '').strip()
                list_md.append(f"{i}.  {item_text}")
            enum.replace_with('\n\n' + '\n\n'.join(list_md) + '\n\n')

        # 7. align / align* / gather / gather* 数式ブロック置換
        for math_env in list(soup.find_all(['align', 'align*', 'gather', 'gather*', 'eqnarray', 'eqnarray*'])):
            env_name = math_env.name
            body = []
            for child in math_env.contents:
                body.append(str(child))
            align_str = ''.join(body).strip()
            math_env.replace_with(f'\n$$\n\\begin{{{env_name}}}\n{align_str}\n\\end{{{env_name}}}\n$$\n')

        md_body = str(soup)
        md_body = re.sub(r'\\begin\{tabular\}.*?\\end\{tabular\}', convert_tabular_block, md_body, flags=re.DOTALL)

        # --------------------------------------------------------------------------
        # numcases / subnumcases 環境の基本対応 (Issue #8 にて将来的に包括的対応)
        # 複雑な式番号付与を行わず、シンプルに標準の cases 環境 ($$ ... \begin{cases} ... \end{cases} $$)
        # へ変換するにとどめる。
        # --------------------------------------------------------------------------
        def replace_numcases(match):
            left_expr = re.sub(r'\\+$', '', match.group(1).strip()).strip()
            body = match.group(2).strip()
            # cases 内でパースエラーとなる \label をクリーン除去
            body_clean = re.sub(r'\\label\{[^}]+\}', '', body)

            if left_expr:
                return f"\n$$\n{left_expr} \\begin{{cases}}\n{body_clean}\n\\end{{cases}}\n$$\n"
            else:
                return f"\n$$\n\\begin{{cases}}\n{body_clean}\n\\end{{cases}}\n$$\n"

        md_body = re.sub(r'\\begin\{(?:numcases|subnumcases)\}\s*\{([^}]*)\}(.*?)\\end\{(?:numcases|subnumcases)\}', replace_numcases, md_body, flags=re.DOTALL)
    except Exception as e:
        print(f"TexSoup warning for {tex_path}: {e}")
        # TexSoup が不整合な TeX をパース失敗した際のフォールバック
        md_body = raw_tex
        
        # フォールバック処理でも figure / tikzpicture の SVG 生成を試みる
        def replace_figure_fallback(match):
            nonlocal fig_count
            fig_content = match.group(0)
            m_tikz = re.search(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', fig_content, re.DOTALL)
            m_cap = re.search(r'\\caption\{([^}]+)\}', fig_content)
            m_lbl = re.search(r'\\label\{([^}]+)\}', fig_content)

            cap_text = m_cap.group(1) if m_cap else ''
            lbl_id = m_lbl.group(1) if m_lbl else f'fig_{fig_count}'

            if m_tikz:
                tikz_code = m_tikz.group(0)
                svg_filename = f"fig_{fig_count}.svg"
                svg_dest_path = os.path.join(output_svg_dir, svg_filename)
                os.makedirs(output_svg_dir, exist_ok=True)
                compile_tikz_to_svg(tikz_code, svg_dest_path, macro_defs)

                web_img_src = f"{public_img_dir_rel}/{svg_filename}"
                caption_label = f"図 {fig_count}" + (f": {cap_text}" if cap_text else "")
                fig_html = f'\n\n<figure id="{lbl_id}">\n  <img src="{web_img_src}" alt="図 {fig_count}" />\n  <figcaption>{caption_label}</figcaption>\n</figure>\n\n'
                fig_count += 1
                return fig_html
            return fig_content

        md_body = re.sub(r'\\begin\{figure\}.*?\\end\{figure\}', replace_figure_fallback, md_body, flags=re.DOTALL)
        md_body = re.sub(r'\\begin\{(align\*?|gather\*?)\}(.*?)\\end\{\1\}', r'\n$$\n\\begin{\1}\2\\end{\1}\n$$\n', md_body, flags=re.DOTALL)

    # physics パッケージ \mqty マクロの標準 LaTeX 行列環境への変換
    md_body = re.sub(r'\\mqty\((.*?)\)', r'\\begin{pmatrix}\1\\end{pmatrix}', md_body, flags=re.DOTALL)
    md_body = re.sub(r'\\mqty\[(.*?)\]', r'\\begin{bmatrix}\1\\end{bmatrix}', md_body, flags=re.DOTALL)
    md_body = re.sub(r'\\mqty\{(.*?)\}', r'\\begin{matrix}\1\\end{matrix}', md_body, flags=re.DOTALL)

    # 見出しと見映えの最終整頓
    md_content = re.sub(r'\\begin\{table\}[^}\n]*|\\end\{table\}|\\centering|\\begin\{center\}|\\end\{center\}|\\shadowbox\{|\\endtabular', '', md_body)
    md_content = re.sub(r'\\renewcommand\{[^}]*\}\{[^}]*\}', '', md_content)
    md_content = re.sub(r'\\textbf\{([^{}]+)\}', r'**\1**', md_content)
    md_content = re.sub(r'\\normalsize', '', md_content)
    md_content = re.sub(r'\{\\bf\s*\\?\[解\\?\]\}|\*\*\[解\]\*\*|\\\[解\\\]|(?<!#)\s*【解】', r'\n\n## 【解】\n\n', md_content)
    md_content = re.sub(r'\{\\bf\s*\\?\[解説\\?\]\}|\*\*\[解説\]\*\*|\\\[解説\\\]|(?<!#)\s*【解説】', r'\n\n## 【解説】\n\n', md_content)
    md_content = re.sub(r'\{\\bf\s*\\?\[方針\\?\]\}|\*\*\[方針\]\*\*|\\\[方針\\\]|(?<!#)\s*【方針】', r'\n\n## 【方針】\n\n', md_content)

    # 明示的な TeX 見出し \paragraph{...} の変換
    md_content = re.sub(r'\\paragraph\*?\s*\{([^}]+)\}', r'\n\n### \1\n\n', md_content)
    md_content = re.sub(r'\\subparagraph\*?\s*\{([^}]+)\}', r'\n\n#### \1\n\n', md_content)

    # --------------------------------------------------------------------------
    # 数式参照 (\eqref, \ref, \cref) の Markdown アンカーリンク化処理
    # --------------------------------------------------------------------------
    # \eqref{lbl} -> [(1)](#lbl) や \ref{lbl} -> [(1)](#lbl) への動的変換
    eq_counter = {}
    def replace_ref_links(m):
        cmd = m.group(1) # eqref, ref, cref
        lbl = m.group(2)
        # ラベル名が eq:X のような場合は式番号風にリンク化
        if 'eq' in lbl:
            num = lbl.split(':')[-1]
            return f'[(式{num})](#{lbl})'
        elif 'fig' in lbl:
            num = lbl.split(':')[-1]
            return f'[図{num}](#{lbl})'
        elif 'tab' in lbl:
            num = lbl.split(':')[-1]
            return f'[表{num}](#{lbl})'
        return f'[{lbl}](#{lbl})'

    md_content = re.sub(r'\\(eqref|ref|cref)\{([^}]+)\}', replace_ref_links, md_content)
    # $...$ で囲まれた Markdown リンク $[(...)](#id)$ の $ 剥ぎ取り
    md_content = re.sub(r'\$\s*(\[.*?\]\(#[^)]+\))\s*\$', r'\1', md_content)

    # --------------------------------------------------------------------------
    # 数式ブロック $$ ... $$ の中のネストされた不要な $ や \displaystyle の除去
    # --------------------------------------------------------------------------
    def clean_math_block_dollars(match):
        block_content = match.group(1)
        # $...$ または $\displaystyle ...$ を外枠の数式に統合
        block_clean = re.sub(r'\$\s*(\\displaystyle\s*)?([^$]+)\$', r'\2', block_content)
        return f"\n$$\n{block_clean.strip()}\n$$\n"

    md_content = re.sub(r'\$\$\n(.*?)\n\$\$', clean_math_block_dollars, md_content, flags=re.DOTALL)

    # 連続する空行を縮小
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
                    print(f"Converting Clean: {tex_path} -> {output_md_path}")
                    convert_tex_clean(tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir)

if __name__ == '__main__':
    process_all_src()
