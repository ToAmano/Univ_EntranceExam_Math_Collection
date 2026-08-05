import os
import sys
import re
import subprocess
import shutil
import tempfile
import pypandoc
from concurrent.futures import ProcessPoolExecutor, as_completed
from TexSoup import TexSoup


def _extract_braced(text, start):
    """text[start] は '{' である前提。対応する閉じ '}' までを中括弧の
    ネストを数えながら走査し、(全体の文字列, 閉じ括弧直後のインデックス) を返す。
    \\newcommand の本体は複数行・ネスト中括弧を含みうるため、単純な正規表現では
    正しく切り出せない。"""
    depth = 0
    i = start
    n = len(text)
    while i < n:
        c = text[i]
        if c == '\\' and i + 1 < n:
            i += 2
            continue
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return text[start:i + 1], i + 1
        i += 1
    return text[start:], n


def _split_top_level_rows(content):
    """align/gather 系環境の中身を、トップレベルの \\\\ でのみ行分割する。
    \\begin{cases}/\\begin{split}/\\begin{pmatrix} などネストした環境内部の \\\\ は
    その環境自身の行区切りであって、外側の align にとっての行区切りではない
    ため、ネスト深度を数えて無視する（split の中身は丸ごと 1 行として扱われる）。
    """
    begin_re = re.compile(r'\\begin\{[a-zA-Z*]+\}')
    end_re = re.compile(r'\\end\{[a-zA-Z*]+\}')
    rows = []
    buf = []
    depth = 0
    i = 0
    n = len(content)
    while i < n:
        m = begin_re.match(content, i)
        if m:
            depth += 1
            buf.append(m.group(0))
            i = m.end()
            continue
        m = end_re.match(content, i)
        if m:
            depth -= 1
            buf.append(m.group(0))
            i = m.end()
            continue
        if content[i:i + 2] == '\\\\' and depth == 0:
            rows.append(''.join(buf))
            buf = []
            i += 2
            continue
        buf.append(content[i])
        i += 1
    if ''.join(buf).strip():
        rows.append(''.join(buf))
    return rows


_EQ_NUMBER_ENV_RE = re.compile(r'\\begin\{(align|gather|eqnarray|equation)(\*?)\}')
_EQ_NUMBER_LABEL_RE = re.compile(r'\\label\{([^}]+)\}')


def compute_eq_numbers(raw_tex):
    """MathJax (tags:'ams') の数式自動採番を模倣し、\\label{...} が実際に画面上
    表示される番号を計算して {ラベル名: 番号} の辞書として返す。

    \\cref/\\eqref の表示テキストをラベル名 (例 "eq:2" の "2") からそのまま
    生成すると、align は「ブロック単位」ではなく「\\\\ で区切られた行単位」で
    採番されるため、1つの align に複数行あるとラベルが指す実際の番号とずれる
    （\\begin{split} で包まれた行は 1 行分としてまとめて数える）。

    numcases/subnumcases (cases パッケージ) は意図的に対象外: このサイトでは
    $$...$$ にラップされる際に無採番の \\begin{cases} へ変換されて表示される
    ため（tags:'ams' は素の $$...$$ を採番しない）、実際には画面上に番号が
    一切表示されない。ここでカウンタを進めてしまうと、同じファイル内で後に
    続く本物の align ブロックの番号が実際の表示より大きくずれてしまう。
    """
    numbers = {}
    counter = 0
    pos = 0
    while True:
        m = _EQ_NUMBER_ENV_RE.search(raw_tex, pos)
        if not m:
            break
        env, star = m.group(1), m.group(2)
        end_re = re.compile(r'\\end\{' + re.escape(env + star) + r'\}')
        end_m = end_re.search(raw_tex, m.end())
        if not end_m:
            pos = m.end()
            continue
        block = raw_tex[m.end():end_m.start()]
        pos = end_m.end()

        if star:
            continue  # 星付き環境は無採番なのでカウンタを進めない

        rows = [block] if env == 'equation' else _split_top_level_rows(block)
        for row in rows:
            if not row.strip():
                continue
            has_notag = '\\notag' in row
            labels = _EQ_NUMBER_LABEL_RE.findall(row)
            if not has_notag:
                counter += 1
                for lbl in labels:
                    numbers[lbl] = counter
    return numbers


def extract_global_macro_defs(raw_tex):
    """図を単体で（別ドキュメントとして）コンパイルする際に必要な、外部で定義された
    マクロ／設定だけを、出現順を保ったまま抽出する。

    tikzpicture 本体の内側で定義されている \\def / \\pgfmathsetmacro は対象外とする：
    \\foreach \\i in {...}{ \\pgfmathsetmacro{\\angle}{\\i * ...} } や
    \\pgfplotsinvokeforeach{...}{ \\pgfmathsetmacro{...}{...#1...} } のようにループ変数
    （\\i, #1 等）に依存する行がそのまま拾われると、ループの外（プリアンブル）では
    その変数が未定義でエラーになる。また、tikzpicture 内の行は元々その figure の
    tikz_code に含まれているため、外側へ複製する必要自体がない
    （実例: utokyo 後期2006年第2問、utokyo 後期1999年第3問で発生）。

    \\pgfmathsetmacro{\\foo}{...}; のように文末に踏襲された `;` がプリアンブルへ
    そのままハイストされると、`;` が地の文字としてタイプセットされ
    "Missing \\begin{document}" エラーになる（実例: titech 後期2006年第1問、
    utokyo 後期1992年第1問）。これも上記の「tikzpicture 内側は対象外」ルールで
    合わせて回避される。

    \\newcommand / \\renewcommand は本体が複数行・ネスト中括弧を含みうるため、
    _extract_braced() でブレース対応を追跡しながら抽出する
    （実例: utokyo 後期1990年第3問の \\recursiveTriangleQTwo）。
    """
    outer_text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', '', raw_tex, flags=re.DOTALL)

    newcommand_defs = []
    masked = list(outer_text)
    for m in re.finditer(r'\\(?:newcommand|renewcommand)\s*(?:\{\\[a-zA-Z]+\}|\\[a-zA-Z]+)', outer_text):
        start = m.start()
        j = m.end()
        while True:
            m_opt = re.match(r'\s*\[[^\]]*\]', outer_text[j:])
            if not m_opt:
                break
            j += m_opt.end()
        m_ws = re.match(r'\s*', outer_text[j:])
        j += m_ws.end()
        if j < len(outer_text) and outer_text[j] == '{':
            snippet, end = _extract_braced(outer_text, j)
            newcommand_defs.append((start, outer_text[start:end]))
            for k in range(start, end):
                masked[k] = ' '
    masked_text = ''.join(masked)

    other_defs = [(m.start(), m.group(0))
                  for m in re.finditer(r'\\(?:def|pgfmathsetmacro|tdplot)[^\n]+', masked_text)]

    seen = set()
    ordered = []
    for _, snippet in sorted(newcommand_defs + other_defs, key=lambda t: t[0]):
        if snippet not in seen:
            seen.add(snippet)
            ordered.append(snippet)
    return "\n".join(ordered)


def compile_tikz_to_svg(tikz_code, output_svg_path, macro_defs=""):
    """
    TikZコードと大問レベルのマクロ定義を組み合わせてスタンドアロンSVG画像を生成する
    pdftocairo (Poppler) を最優先で使用し、完璧なベクトル描画を行う

    図ごとに独立した一時ディレクトリを使い、コンパイラの終了コードを必ず確認する。
    以前は固定パス scratch/tikz_build/fig.pdf を使い回し、かつ os.path.exists() のみで
    成否判定していたため、ある図のコンパイルが失敗しても直前の図の fig.pdf が
    残っていれば「成功」と誤判定され、その古い画像が使い回されてしまう不具合があった
    （CI環境で全ての図が同一画像になる原因になっていた）。
    """
    os.makedirs("scratch", exist_ok=True)
    temp_dir = tempfile.mkdtemp(prefix="tikz_build_", dir="scratch")
    tex_filename = os.path.join(temp_dir, "fig.tex")
    pdf_filename = os.path.join(temp_dir, "fig.pdf")
    log_filename = os.path.join(temp_dir, "fig.log")

    full_tex = f"""\\documentclass[tikz,border=2pt]{{standalone}}
\\usepackage{{amsmath,amssymb,amsfonts,amsthm}}
\\usepackage{{luatexja}}
\\usepackage[haranoaji]{{luatexja-preset}}
\\usepackage{{tikz,pgfplots}}
\\usepackage{{tikz-3dplot}}
\\usetikzlibrary{{arrows.meta,calc,intersections,patterns,patterns.meta,angles,quotes,through,positioning,decorations.pathmorphing,decorations.markings,math,3d,perspective,shapes.geometric,backgrounds}}
\\usepgfplotslibrary{{fillbetween,colormaps,groupplots}}
\\pgfplotsset{{compat=1.18}}
% ここから下は generate_main_tex.py の PREAMBLE と同じフォールバック・略記マクロ群。
% 図を単体でコンパイルする際、全体ビルドでは定義済みの前提で書かれている図
% （\\tikzmath や \\R 等）が単体コンパイルだけ失敗するのを防ぐため、
% 実質的に同じプリアンブルを維持する。
% tdplot_main_coords スタイルを使う figure が \\tdplotsetmaincoords を
% 自前で呼んでいない場合、ここで呼んでおかないと
% "I do not know the key '/tikz/tdplot_main_coords'" で単体コンパイルが失敗する
% （各 figure 側で呼んでいれば tikz_code 側の呼び出しで上書きされる）。
\\tdplotsetmaincoords{{70}}{{110}}
\\newcommand{{\\R}}{{\\mathbb{{R}}}}
\\newcommand{{\\C}}{{\\mathbb{{C}}}}
\\newcommand{{\\N}}{{\\mathbb{{N}}}}
\\newcommand{{\\Z}}{{\\mathbb{{Z}}}}
\\newcommand{{\\Q}}{{\\mathbb{{Q}}}}
\\providecommand{{\\roundedArrowDR}}{{\\searrow}}

{macro_defs}

\\begin{{document}}
{tikz_code}
\\end{{document}}
"""

    with open(tex_filename, 'w', encoding='utf-8') as f:
        f.write(full_tex)

    def _log_tail(result):
        if os.path.exists(log_filename):
            return open(log_filename, encoding='utf-8', errors='ignore').read()[-2000:]
        return ((result.stdout or "") + (result.stderr or ""))[-2000:]

    try:
        # 1. LuaLaTeX で高品質 PDF の作成。失敗したら pdflatex にフォールバック。
        #    どちらも終了コードと pdf_filename の存在を両方確認する
        #    （終了コードだけ／存在だけの片方の確認では不十分）。
        cmd_compile_pdf = ["lualatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-output-directory=" + temp_dir, tex_filename]
        result = subprocess.run(cmd_compile_pdf, capture_output=True, text=True)

        if result.returncode != 0 or not os.path.exists(pdf_filename):
            cmd_pdflatex = ["pdflatex", "-interaction=nonstopmode", "-halt-on-error",
                             "-output-directory=" + temp_dir, tex_filename]
            result = subprocess.run(cmd_pdflatex, capture_output=True, text=True)

        if result.returncode != 0 or not os.path.exists(pdf_filename):
            print(f"[tex_to_md] Failed to produce PDF for TikZ figure at {output_svg_path} "
                  f"(exit code {result.returncode})")
            print(f"[tex_to_md]   log tail:\n{_log_tail(result)}")
            return False

        # 2. pdftocairo (Poppler) による完璧な SVG 変換
        svg_ok = False
        pdftocairo_bin = shutil.which("pdftocairo") or "/opt/homebrew/bin/pdftocairo"
        if pdftocairo_bin and os.path.exists(pdftocairo_bin):
            cmd_svg = [pdftocairo_bin, "-svg", pdf_filename, output_svg_path]
            r = subprocess.run(cmd_svg, capture_output=True, text=True)
            svg_ok = r.returncode == 0 and os.path.exists(output_svg_path)
            if not svg_ok:
                print(f"[tex_to_md] pdftocairo failed for {output_svg_path} "
                      f"(exit code {r.returncode}): {(r.stderr or '')[-500:]}")

        # 3. pdf2svg フォールバック
        if not svg_ok and shutil.which("pdf2svg"):
            cmd_svg = ["pdf2svg", pdf_filename, output_svg_path]
            r = subprocess.run(cmd_svg, capture_output=True, text=True)
            svg_ok = r.returncode == 0 and os.path.exists(output_svg_path)
            if not svg_ok:
                print(f"[tex_to_md] pdf2svg failed for {output_svg_path} "
                      f"(exit code {r.returncode}): {(r.stderr or '')[-500:]}")

        # 4. dvisvgm フォールバック
        if not svg_ok and shutil.which("dvisvgm"):
            cmd_svg = ["dvisvgm", "--pdf", "--no-fonts", "-o", output_svg_path, pdf_filename]
            r = subprocess.run(cmd_svg, capture_output=True, text=True)
            svg_ok = r.returncode == 0 and os.path.exists(output_svg_path)
            if not svg_ok:
                print(f"[tex_to_md] dvisvgm failed for {output_svg_path} "
                      f"(exit code {r.returncode}): {(r.stderr or '')[-500:]}")

        if not svg_ok:
            print(f"[tex_to_md] Failed to convert PDF to SVG for {output_svg_path} "
                  f"(no SVG backend succeeded)")

        return svg_ok
    except Exception as e:
        print(f"[tex_to_md] Error compiling TikZ to SVG for {output_svg_path}: {e}")
        return False
    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

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

    # \cref/\eqref の表示番号を、ラベル名にある数字ではなく実際の自動採番位置
    # から求めるための対応表。後段の replace_ref_links で使用する。
    eq_numbers = compute_eq_numbers(raw_tex)

    # 図を単体で（別ドキュメントとして）コンパイルする際に必要な、外部で定義された
    # マクロ／設定だけを拾う（詳細は extract_global_macro_defs() のdocstring参照）。
    macro_defs = extract_global_macro_defs(raw_tex)

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

        # 6. \begin{enumerate} / \begin{description} / \begin{itemize} は MathJax の TeX 表示用に完全保持する

        # 7. align / align* / gather / gather* 数式ブロック置換
        for math_env in list(soup.find_all(['align', 'align*', 'gather', 'gather*', 'eqnarray', 'eqnarray*', 'equation', 'equation*'])):
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
            # \label は除去しない: 後段の _promote_math_labels が $$...$$ 内の
            # \label を自前の <span id> アンカーへ変換してから MathJax に渡すため、
            # ここで消すと該当ラベルへのハイパーリンクが宛先の無いリンクになる。

            if left_expr:
                return f"\n$$\n{left_expr} \\begin{{cases}}\n{body}\n\\end{{cases}}\n$$\n"
            else:
                return f"\n$$\n\\begin{{cases}}\n{body}\n\\end{{cases}}\n$$\n"

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
        md_body = re.sub(r'\\begin\{(align\*?|gather\*?|equation\*?)\}(.*?)\\end\{\1\}', r'\n$$\n\\begin{\1}\2\\end{\1}\n$$\n', md_body, flags=re.DOTALL)

    # physics パッケージ \mqty マクロの標準 LaTeX 行列環境への変換
    md_body = re.sub(r'\\mqty\((.*?)\)', r'\\begin{pmatrix}\1\\end{pmatrix}', md_body, flags=re.DOTALL)
    md_body = re.sub(r'\\mqty\[(.*?)\]', r'\\begin{bmatrix}\1\\end{bmatrix}', md_body, flags=re.DOTALL)
    md_body = re.sub(r'\\mqty\{(.*?)\}', r'\\begin{matrix}\1\\end{matrix}', md_body, flags=re.DOTALL)

    # 見出しと見映えの最終整頓
    md_content = re.sub(r'\\begin\{table\}[^}\n]*|\\end\{table\}|\\centering|\\begin\{center\}|\\end\{center\}|\\endtabular', '', md_body)
    
    # \shadowbox{...} のアンラップ
    md_content = re.sub(r'\\shadowbox\{([^}]*)\}', r'\1', md_content)
    md_content = re.sub(r'\\shadowbox\{', '', md_content)

    # フォント・スペーシング・再定義関連不要マクロの完全削除
    md_content = re.sub(r'\\renewcommand\s*\{?\\[a-zA-Z]+\}?\s*(\[[^\]]*\])?\s*\{[^}]*\}', '', md_content)
    md_content = re.sub(r'\\renewcommand\s*\{?[^}\n]+\}?\s*\{[^}]*\}', '', md_content)
    md_content = re.sub(r'\\fontsize\{[^}]*\}\{[^}]*\}', '', md_content)
    md_content = re.sub(r'\\selectfont|\\normalsize|\\noindent|\\vspace\{[^}]*\}|\\hspace\{[^}]*\}|\\pagestyle\{[^}]*\}', '', md_content)

    # \textbf の Markdown 化
    md_content = re.sub(r'\\textbf\{([^{}]+)\}', r'**\1**', md_content)
    # **AAAA****BBBB** や **AAAA** **BBBB** の自動結合 (**AAAABBBB**)
    md_content = re.sub(r'\*\*([^*]+)\*\*\s*\*\*([^*]+)\*\*', r'**\1\2**', md_content)

    # 見出しセクションの整形
    md_content = re.sub(r'\{\\bf\s*\\?\[解\\?\]\}|\*\*\[解\]\*\*|\\\[解\\\]|(?<!#)\s*【解】', r'\n\n## 【解】\n\n', md_content)
    md_content = re.sub(r'\{\\bf\s*\\?\[解説\\?\]\}|\*\*\[解説\]\*\*|\\\[解説\\\]|(?<!#)\s*【解説】', r'\n\n## 【解説】\n\n', md_content)
    md_content = re.sub(r'\{\\bf\s*\\?\[方針\\?\]\}|\*\*\[方針\]\*\*|\\\[方針\\\]|(?<!#)\s*【方針】', r'\n\n## 【方針】\n\n', md_content)

    # リスト環境 (\begin{enumerate}, \begin{description}, \begin{itemize}) の HTML/Markdown 番号付きリスト変換 (Issue #509)
    def convert_enumerate_to_md_list(m):
        block = m.group(2)
        items = re.split(r'\\item\s*', block)
        res = []
        count = 1
        for it in items:
            it = it.strip()
            if not it:
                continue
            # 残存する項目オプションラベル [(1)] や [(イ)] 等のストリップ
            it = re.sub(r'^\[\s*\(?.*?\)?\s*\]\s*', '', it)
            res.append(f"{count}.  {it}")
            count += 1
        return "\n\n" + "\n\n".join(res) + "\n\n"

    md_content = re.sub(r'\\begin\{(enumerate|description|itemize)\}(.*?)\\end\{\1\}', convert_enumerate_to_md_list, md_content, flags=re.DOTALL)

    # ディスプレイ数式 \[ ... \] の \begin{align*} ... \end{align*} への統一
    md_content = re.sub(r'\\\[\s*(.*?)\s*\\\]', r'\n$$\n\\begin{align*}\n\1\n\\end{align*}\n$$\n', md_content, flags=re.DOTALL)

    # 冒頭・単独の空の中括弧 {} や不要記号の除去
    md_content = re.sub(r'^\s*\{\}\s*$', '', md_content, flags=re.MULTILINE)
    md_content = re.sub(r'^\s*\{\}\s*', '', md_content, flags=re.MULTILINE)

    # 明示的な TeX 見出し \paragraph{...} / \subparagraph{...} の変換。
    # 場合分けの見出しには \subparagraph{$0\le x\le\dfrac{1}{2}$の時} のように
    # 引数中にネストした {} を含むことが多く、単純な [^}]+ では最初の '}' で
    # 切れてしまうため、_extract_braced で中括弧の対応を数えながら切り出す。
    def _convert_heading_command(text, command, heading_prefix):
        pattern = re.compile(r'\\' + command + r'\*?\s*\{')
        out = []
        i = 0
        while True:
            m = pattern.search(text, i)
            if not m:
                out.append(text[i:])
                break
            out.append(text[i:m.start()])
            braced, end = _extract_braced(text, m.end() - 1)
            inner = braced[1:-1]
            out.append(f'\n\n{heading_prefix} {inner}\n\n')
            i = end
        return ''.join(out)

    md_content = _convert_heading_command(md_content, 'subparagraph', '####')
    md_content = _convert_heading_command(md_content, 'paragraph', '###')

    # --------------------------------------------------------------------------
    # 数式ブロック内 \label{...} の自前アンカー化
    # --------------------------------------------------------------------------
    # MathJax (tags:'ams') は \label{eq:1} を "mjx-eqn:eq:1" のような、
    # バージョン依存かつラベルによっては自動連番 ("mjx-eqn:2" 等) にフォール
    # バックする非公開の内部IDに変換してしまい、下で生成する #eq:1 形式の
    # リンクとは一致しない。MathJax のID生成に依存せず、$$...$$ ブロックの
    # 直前に自前の <span id="..."> アンカーを差し込み、\label 自体は数式内
    # から除去する。
    def _promote_math_labels(text):
        block_re = re.compile(r'\$\$\n.*?\n\$\$\n', re.DOTALL)

        def process_block(m):
            block = m.group(0)
            labels = re.findall(r'\\label\{([^}]+)\}', block)
            if not labels:
                return block
            block_clean = re.sub(r'\\label\{[^}]+\}', '', block)
            anchors = ''.join(f'<span id="{lbl}"></span>' for lbl in labels)
            return anchors + block_clean

        return block_re.sub(process_block, text)

    md_content = _promote_math_labels(md_content)

    # --------------------------------------------------------------------------
    # 数式参照 (\eqref, \ref, \cref) の Markdown アンカーリンク化処理
    # --------------------------------------------------------------------------
    # \eqref{lbl} -> [(1)](#lbl) や \ref{lbl} -> [(1)](#lbl) への動的変換。
    # \cref{eq:1,eq:2} のような複数ラベル一括参照はカンマ区切りで別々の
    # リンクに分解する（そのまま繋げると #eq:1,eq:2 という実在しない
    # 1つのIDへのリンクになってしまうため）。
    # ただし $$...$$ ブロック（\begin{align} 等の生の LaTeX）内の \cref は、
    # \text{} などの数式の一部として使われている場合があり、Markdown の
    # [..](#..) リンク構文をそのまま埋め込むと KaTeX/MathJax が丸ごとパース
    # 失敗してブロック全体が未レンダリングの生テキストになってしまう。
    # そのためブロック内ではリンク化せず番号だけのプレーンテキストにする。
    def replace_ref_links(m, in_math=False):
        raw_lbls = [l.strip() for l in m.group(2).split(',') if l.strip()]

        def one(lbl):
            # ラベル名の書式 (eq:N, 素の数字, 1a など) によらず、実際の自動採番
            # 位置を計算済みの eq_numbers を最優先で使う。これに無ければ
            # 数式ラベルではない（図表ラベル等）とみなし、名前ベースの
            # 従来ロジックにフォールバックする。
            if lbl in eq_numbers:
                label = f'(式{eq_numbers[lbl]})'
            elif 'eq' in lbl:
                print(f"[tex_to_md] WARNING: no computed number for label '{lbl}' in {tex_path}; "
                      f"falling back to label-name digit (may be wrong)")
                label = f'(式{lbl.split(":")[-1]})'
            elif 'fig' in lbl:
                num = lbl.split(':')[-1]
                label = f'図{num}'
            elif 'tab' in lbl:
                num = lbl.split(':')[-1]
                label = f'表{num}'
            else:
                label = lbl
            if in_math:
                return label
            return f'[{label}](#{lbl})'

        return ','.join(one(lbl) for lbl in raw_lbls)

    REF_RE = re.compile(r'\\(eqref|ref|cref)\{([^}]+)\}')
    MATH_BLOCK_RE = re.compile(r'\$\$\n.*?\n\$\$', re.DOTALL)

    def _convert_refs(text, in_math):
        return REF_RE.sub(lambda m: replace_ref_links(m, in_math=in_math), text)

    non_math_parts = MATH_BLOCK_RE.split(md_content)
    math_parts = MATH_BLOCK_RE.findall(md_content)
    rebuilt = [_convert_refs(non_math_parts[0], in_math=False)]
    for part, block in zip(non_math_parts[1:], math_parts):
        rebuilt.append(_convert_refs(block, in_math=True))
        rebuilt.append(_convert_refs(part, in_math=False))
    md_content = ''.join(rebuilt)
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

def _convert_one_task(task):
    """process_all_src の各ファイル1件分の変換を実行するワーカー関数。
    ProcessPoolExecutor に渡すため、引数は pickle 可能な単純な値のみ
    （tex_path, output_md_path, frontmatter, public_img_dir_rel,
    output_svg_dir のタプル）にしてある。"""
    tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir = task
    print(f"Converting Clean: {tex_path} -> {output_md_path}")
    convert_tex_clean(tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir)
    return tex_path


def process_all_src():
    src_root = "src"
    dest_root = "web/src/content/solutions"

    tasks = []
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
                    tasks.append((tex_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir))

    # 各ファイルの変換（TikZ図があれば LuaLaTeX コンパイルを含む）は他のファイルと
    # 完全に独立しているため、ProcessPoolExecutor で並列化する。compile_tikz_to_svg
    # は図ごとに tempfile.mkdtemp() で個別の一時ディレクトリを使うため、
    # 複数プロセスから同時に呼んでも衝突しない。
    #
    # as_completed でループしつつ future.result() を呼ぶことで、逐次版と同じ
    # 「どれか1件でも例外が出たら即座に全体を失敗させる」挙動を保つ
    # （例外を握りつぶして変換漏れに気づけなくなることを避ける）。
    max_workers = os.cpu_count() or 4
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(_convert_one_task, t) for t in tasks]
        for future in as_completed(futures):
            future.result()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        target_path = sys.argv[1]
        parts = os.path.normpath(target_path).split(os.sep)
        if len(parts) >= 6:
            # src/titech/zenki/2000/1/problem.tex
            uni, category, year, q_num = parts[1], parts[2], parts[3], parts[4]
            file = parts[5]
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
            dest_root = "web/src/content/solutions"
            filename = f"{uni}-{category}-{year}-{q_num}-{type_str}.md"
            output_md_path = os.path.join(dest_root, filename)
            public_img_dir_rel = f"/Univ_EntranceExam_Math_Collection/images/tikz/{uni}/{category}/{year}/{q_num}"
            output_svg_dir = os.path.join("web", "public", "images", "tikz", uni, category, year, q_num)
            print(f"Pinpoint Converting: {target_path} -> {output_md_path}")
            convert_tex_clean(target_path, output_md_path, frontmatter, public_img_dir_rel, output_svg_dir)
            print("Pinpoint Conversion Finished!")
    else:
        process_all_src()
