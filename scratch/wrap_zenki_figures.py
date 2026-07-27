import re
import glob

CAPTIONS = {
    ("src/titech/zenki/1965/1/solution.tex", 0): "直線$l:y=-x+5$と点$A$，$B$，$C$，$P$の位置関係",
    ("src/titech/zenki/1965/3/solution.tex", 0): "$(\\alpha,\\beta)$平面における条件の図示",
    ("src/titech/zenki/1966/1/solution.tex", 0): "点$(X,Y)$の軌跡（円）の図示",
    ("src/titech/zenki/1966/2/solution.tex", 0): "④，⑤を満たす$(p,q)$，$(\\alpha,\\beta)$の図示",
    ("src/titech/zenki/1967/4/solution.tex", 0): "$S-C$の符号と$\\alpha$，$\\beta$の関係",
    ("src/titech/zenki/1968/1/solution.tex", 0): "$y=x^2-4x-1$のグラフ",
    ("src/titech/zenki/1968/1/solution.tex", 1): "$y=2x^2-6x-1$のグラフ",
    ("src/titech/zenki/1968/3/solution.tex", 0): "②を満たす$(\\alpha,\\beta)$の範囲（斜線部）",
    ("src/titech/zenki/1968/4/solution.tex", 0): "$1^\\circ$，$2^\\circ$の和集合となる領域（非斜線部）",
    ("src/titech/zenki/1969/2/solution.tex", 0): "四面体$ABCP$の辺の長さ",
    ("src/titech/zenki/1969/3/solution.tex", 0): "条件を満たす$(u,v)$の範囲（斜線部）",
    ("src/titech/zenki/1969/4/solution.tex", 0): "点列$\\vec a_n$の$\\vec\\beta$への収束の様子",
    ("src/titech/zenki/1969/5/solution.tex", 0): "$y=f(x)$のグラフの概形",
    ("src/titech/zenki/1970/2/solution.tex", 0): "楕円と焦点$F$，準線$l$の関係",
    ("src/titech/zenki/1970/4/solution.tex", 0): "角度の大小関係を示す図",
    ("src/titech/zenki/1971/2/solution.tex", 0): "条件④を満たす$(a,k)$の範囲",
    ("src/titech/zenki/1971/4/solution.tex", 0): "$1^\\circ$，$2^\\circ$の場合分けにおける$t$の範囲",
    ("src/titech/zenki/1971/4/solution.tex", 1): "$(u,v)$の軌跡の図示（斜線部）",
    ("src/titech/zenki/1972/5/solution.tex", 0): "接線$y=\\dfrac{1}{e}x$のグラフ",
    ("src/titech/zenki/1973/1/solution.tex", 0): "$q=3m+1$の場合の$p$の範囲",
    ("src/titech/zenki/1973/1/solution.tex", 1): "$q=3m-1$の場合の$p$の範囲",
    ("src/titech/zenki/1973/1/solution.tex", 2): "$q=-(3m+1)$の場合の$p$の範囲",
    ("src/titech/zenki/1973/5/solution.tex", 0): "回転体の体積を求めるための図",
    ("src/titech/zenki/1974/1/solution.tex", 0): "$y=x$と$y=f(x)$のグラフ",
    ("src/titech/zenki/1974/4/solution.tex", 0): "回転体の体積$V_1$，$V_2$を求めるための図",
    ("src/titech/zenki/1975/4/solution.tex", 0): "点$P$，$Q$，$R$，$T$，$U$の位置関係",
    ("src/titech/zenki/1976/3/solution.tex", 0): "点$P$の軌跡と$\\triangle OAB$の関係",
    ("src/titech/zenki/1978/3/solution.tex", 0): "点$P$，$P'$と直線$y=x$の関係",
    ("src/titech/zenki/1979/4/solution.tex", 0): "接線$\\ell_a$，$\\ell_c$の交点$R$",
    ("src/titech/zenki/1980/2/solution.tex", 0): "$\\triangle ABC$と点$D$の位置関係",
    ("src/titech/zenki/1980/3/solution.tex", 0): "$y=f(t)$のグラフの概形",
    ("src/titech/zenki/1981/2/solution.tex", 0): "点$T$が動く領域$D$（斜線部）",
    ("src/titech/zenki/1981/3/solution.tex", 0): "点$P$，$Q$，$R$の位置関係",
    ("src/titech/zenki/1981/4/solution.tex", 0): "$y=F(t)$のグラフの概形",
    ("src/titech/zenki/1982/1/solution.tex", 0): "円の配置と角$\\theta$",
    ("src/titech/zenki/1982/3/solution.tex", 0): "領域$D$の図示",
    ("src/titech/zenki/1982/4/solution.tex", 0): "面積$S$を求めるための図",
    ("src/titech/zenki/1983/2/solution.tex", 0): "条件を満たす領域の図示（斜線部）",
    ("src/titech/zenki/1983/5/solution.tex", 0): "面積$S(t)$を求めるための図形の分割",
    ("src/titech/zenki/1984/3/solution.tex", 0): "双曲線$C_1$，$C_2$と点$P_1$，$P_2$",
    ("src/titech/zenki/1984/5/solution.tex", 0): "曲線$y=\\tan x$，$y=\\cos x$と面積$T$",
    ("src/titech/zenki/1985/3/solution.tex", 0): "円$O_1\\sim O_5$の配置",
    ("src/titech/zenki/1986/4/solution.tex", 0): "$y=f(x)$，$y=g(x)$のグラフの概形",
    ("src/titech/zenki/1987/3/solution.tex", 0): "条件を満たす領域の図示（斜線部）",
    ("src/titech/zenki/1987/4/solution.tex", 0): "曲線$C$の概形と面積$S$",
    ("src/titech/zenki/1988/2/solution.tex", 0): "条件①を満たす$(a,b)$の範囲",
    ("src/titech/zenki/1989/1/solution.tex", 0): "求める領域の図示（斜線部）",
    ("src/titech/zenki/1990/5/solution.tex", 0): "面積$S$を求める領域の図示（斜線部）",
    ("src/titech/zenki/1991/3/solution.tex", 0): "点$A$，$B$，$C$，$D$，$E$の位置関係",
    ("src/titech/zenki/1991/4/solution.tex", 0): "条件を満たす$(a,b)$の範囲（斜線部）",
    ("src/titech/zenki/1992/1/solution.tex", 0): "$y=x+\\dfrac{k^2}{x}$のグラフ",
    ("src/titech/zenki/1992/4/solution.tex", 0): "$y=f_2(x)$，$y=f_3(x)$のグラフ",
    ("src/titech/zenki/1994/4/solution.tex", 0): "条件を満たす$(m,n)$の図示（黒丸）",
    ("src/titech/zenki/1997/1/solution.tex", 0): "条件を満たす$(a,b)$の領域（斜線部）",
    ("src/titech/zenki/1998/1/solution.tex", 0): "直線$2x+3y=12$と点$P$の関係",
    ("src/titech/zenki/1998/2/solution.tex", 0): "円$W$，$X$，$Y$，$Z$の配置",
}

files = sorted(glob.glob("src/titech/zenki/*/*/solution.tex"))
files = [f for f in files if int(f.split('/')[3]) >= 1965]

wrapped_count = 0
for f in files:
    text = open(f, encoding="utf-8").read()
    fig_spans = [m.span() for m in re.finditer(r'\\begin\{figure\}.*?\\end\{figure\}', text, re.DOTALL)]

    def in_figure(pos):
        return any(s <= pos < e for s, e in fig_spans)

    center_blocks = list(re.finditer(r'\\begin\{center\}.*?\\end\{center\}', text, re.DOTALL))
    bare_centers = [cb for cb in center_blocks if '\\begin{tikzpicture}' in cb.group(0) and not in_figure(cb.start())]

    if not bare_centers:
        continue

    # 後ろから置換していく（前方のインデックスがずれないように）
    for i in reversed(range(len(bare_centers))):
        cb = bare_centers[i]
        key = (f, i)
        if key not in CAPTIONS:
            raise SystemExit(f"Missing caption for {key}")
        caption = CAPTIONS[key]
        block_text = cb.group(0)
        replacement = (
            "\\begin{figure}[htb]\n"
            + block_text
            + f"\n\\caption{{{caption}}}\n"
            + "\\end{figure}"
        )
        s, e = cb.span()
        text = text[:s] + replacement + text[e:]
        wrapped_count += 1

    open(f, "w", encoding="utf-8").write(text)

print(f"Wrapped {wrapped_count} figure blocks")
