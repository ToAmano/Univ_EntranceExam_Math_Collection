import re
import glob

files = sorted(glob.glob("src/titech/zenki/*/*/solution.tex"))
files = [f for f in files if int(f.split('/')[3]) >= 1965]

changed = []
for f in files:
    text = open(f, encoding="utf-8").read()
    orig = text

    # 1. 句読点: 全角「．」「，」に統一
    text = text.replace('。', '．').replace('、', '，')

    # 2. \begin{proof}[X]...\end{proof} -> {\bf [X]} ... (見出しのみ、end は除去)
    text = re.sub(r'\\begin\{proof\}\s*\[([^\]]*)\]', r'{\\bf [\1]}', text)
    text = re.sub(r'\\end\{proof\}', '', text)

    # 3. equation/equation* -> align*
    text = re.sub(r'\\begin\{equation\*?\}', r'\\begin{align*}', text)
    text = re.sub(r'\\end\{equation\*?\}', r'\\end{align*}', text)

    # 4. \[ ... \] -> align* ( \\[len] のような行送り指定と衝突しないよう
    #    直前が \ でない \[ のみを対象にする。事前にカウント・非ネストを確認済み)
    text = re.sub(r'(?<!\\)\\\[', r'\\begin{align*}', text)
    text = re.sub(r'\\\]', r'\\end{align*}', text)

    if text != orig:
        open(f, "w", encoding="utf-8").write(text)
        changed.append(f)

print(f"Changed {len(changed)} / {len(files)} files")
