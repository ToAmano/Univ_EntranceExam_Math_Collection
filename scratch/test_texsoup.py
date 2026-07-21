import os
import re
from TexSoup import TexSoup

def process_tex_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_tex = f.read()

    # 1. プリアンブルや不要なドキュメント枠を取り出す
    if '\\begin{document}' in raw_tex:
        m = re.search(r'\\begin\{document\}(.*?)\\end\{document\}', raw_tex, re.DOTALL)
        if m:
            raw_tex = m.group(1)

    # 不要なプリアンブル命令をクリーンアップ
    raw_tex = re.sub(r'\\rhead\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\setcounter\{[^}]*\}\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\begin\{oframed\}\s*\\input\{[^}]+\}\s*\\end\{oframed\}', '', raw_tex)
    raw_tex = re.sub(r'\\setlength\{[^}]*\}\{[^}]*\}', '', raw_tex)
    raw_tex = re.sub(r'\\begin\{multicols\}\{\d+\}', '', raw_tex)
    raw_tex = re.sub(r'\\end\{multicols\}', '', raw_tex)
    raw_tex = re.sub(r'\\newpage', '', raw_tex)
    raw_tex = re.sub(r'\\vspace\{[^}]*\}', '', raw_tex)

    # 2. TexSoup で構文木 AST を作成
    soup = TexSoup(raw_tex)

    # 3. \cref ノードの置換
    for cref in list(soup.find_all('cref')):
        if cref.args:
            target = str(cref.args[0]).strip('{}')
            if 'fig:' in target:
                cref.replace_with(f'$\\ref{{{target}}}$')
            else:
                cref.replace_with(f'$\\eqref{{{target}}}$')

    # 4. figure 環境（TikZ図）の置き換え
    fig_count = 1
    for fig in list(soup.find_all('figure')):
        caption_node = fig.find('caption')
        label_node = fig.find('label')
        
        caption_text = str(caption_node.args[0]).strip('{}') if caption_node and caption_node.args else ''
        label_id = str(label_node.args[0]).strip('{}') if label_node and label_node.args else f'fig_{fig_count}'
        
        # HTML figure タグに置換
        fig_html = f'\n<figure id="{label_id}">\n  <img src="IMAGE_PATH_HERE/fig_{fig_count}.svg" />\n  <figcaption>{caption_text}</figcaption>\n</figure>\n'
        fig.replace_with(fig_html)
        fig_count += 1

    # 5. \begin{enumerate} ノードの置換（設問リスト番号）
    for enum in list(soup.find_all('enumerate')):
        items = enum.find_all('item')
        list_md = []
        for i, item in enumerate(items, 1):
            # itemのテキストコンテンツを取得
            item_text = str(item).replace('\\item', '').strip()
            list_md.append(f"{i}.  {item_text}")
        enum.replace_with('\n\n' + '\n\n'.join(list_md) + '\n\n')

    # 6. align / align* ノードの置換
    for align in list(soup.find_all(['align', 'align*'])):
        env_name = align.name
        # 内部テキスト
        body = []
        for child in align.contents:
            body.append(str(child))
        align_str = ''.join(body).strip()
        align.replace_with(f'\n$$\n\\begin{{{env_name}}}\n{align_str}\n\\end{{{env_name}}}\n$$\n')

    return str(soup)

if __name__ == '__main__':
    print("--- 1995/1/solution.tex (後半部分) ---")
    sol_md = process_tex_file('src/sample_titech/kouki/1995/1/solution.tex')
    print(sol_md[1300:])
