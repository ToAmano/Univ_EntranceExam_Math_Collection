# このリポジトリでの検査・確認のコマンド（下書き）

汎用の工程は `SKILL.md`、図の確認手順は `references/figure-rules.md` の §11・§12。
ここには、このリポジトリで使う具体的なコマンド・スクリプトの注意・手本のファイルだけを書く。
文字起こしの固有手順は `local/transcription.md`。

---

## W1. lint

```bash
python3 scratch/lint_latex_style.py <file> [...]
python3 scratch/lint_latex_style.py --diff <file>   # 機械的な修正の差分を見る
python3 scratch/lint_latex_style.py --fix <file>    # 機械的な修正を書き込む
```

- `scratch/lint_latex_style.py` は入口だけで、本体はスキルの `scripts/lint_tex.py`（汎用）と `local/lint_local.py`（このリポジトリ固有の検査）。入口を使わずに `python3 skills/math-solution-tex/scripts/lint_tex.py --rules skills/math-solution-tex/local/lint_local.py <file>` と呼んでも同じ結果になる。
- 固有の検査：解答の見出し、proof 環境の見出し、`\documentclass[../../main.tex]{subfiles}`、問題文の読み込み（`\subfile{problem}`）、`problem.tex` の形式と `solution.tex` とのラベルの重複。年度のまとめ（`0/`）は余白の命令と `\qed` の検査から外す。
- 指摘の末尾の `[§N5.1]` などは規約の節番号。`python3 skills/math-solution-tex/scripts/rules.py --sec '[§N5.1]'` でその節を表示できる。
- 規則の出所と対応は `skills/rule-lint-map.md`。
- 引数なしならリポジトリ全体を走査して集計だけを表示する。
- CI（`.github/workflows/lint-tex.yml`）は、変更された `solution.tex` だけを検査する。pre-commit でも `--fix` 付きで動く。

## W2. 式変形の検算

```bash
python3 skills/math-solution-tex/scripts/check_math_steps.py <file> [...]
python3 skills/math-solution-tex/scripts/check_math_steps.py --tier A --json out.json src/*/*/*/*/solution.tex
```

- 依存：`python3 -m pip install -r skills/math-solution-tex/scripts/requirements.txt`
- 確度 A・B の読み方は `SKILL.md` の工程 5。

## W3. 図だけの差分の確認（figure §12）

```bash
python3 scratch/check_figure_only_diff.py <file>              # 作業ツリーのファイルを HEAD と比べる
python3 scratch/check_figure_only_diff.py --staged            # ステージした .tex をすべて調べる
python3 scratch/check_figure_only_diff.py --commit <commit>   # その commit で変わった .tex を調べる
python3 scratch/check_figure_only_diff.py --compare-two old.tex new.tex
```

- `scratch/check_figure_only_diff.py` は入口だけで、本体はスキルの `scripts/check_figure_only_diff.py`。
- ファイルを指定した場合、比較の基準はいつも `HEAD`（`--ref` はファイルを指定しないときに、変更されたファイルを探す基準として使われるだけ）。`PASS` なら図のブロック以外に差分がない。
- `FAIL` なら、表示された差分（図以外の変更）を元に戻し、`PASS` になるまで完了にしない。`AGENTS.md` でも必須にしている。
- 同じファイルに図以外の未 commit の変更（文字起こしなど）が残っていると、図の作業とは関係なく `FAIL` になる。その場合は先に図以外の変更を commit してから確かめるか、図の変更だけを入れた版を作って `--compare-two` で比べる。
- 図のブロックとして扱う古い記法：emath の `\begin{zahyou} ... \end{zahyou}`、`\begin{center}\includegraphics...\end{center}`、`figure` の中の `% TODO: 概要図` など。`zahyou` は今のプリアンブルでは未定義でビルドが止まるので、見つけたら TikZ に書き直す。

## W4. コンパイルと PDF の目視

```bash
cd src/{univ}/{cat}/{year}/{q}
latexmk -lualatex -interaction=nonstopmode -halt-on-error -outdir=<一時ディレクトリ> solution.tex
pdftoppm -png -r 90 <一時ディレクトリ>/solution.pdf <一時ディレクトリ>/page
```

- 一時ディレクトリはセッションの scratchpad か `mktemp -d` で作る。`solution.aux` などをリポジトリに残さない。
- 細部（ラベルの重なりなど）は、該当ページを 200〜250dpi で描画し、図の部分だけを切り出して見る（`pdftoppm -r 250 -f <p> -l <p> -x .. -y .. -W .. -H ..`）。

## W5. Web 表示の確認

```bash
python3 scratch/tex_to_md.py <file>          # 1ファイルだけ Markdown と TikZ の SVG を作る
python3 scratch/check_web_leaks.py <file>    # Web 版で TeX がそのまま出る箇所を探す（数秒）
```

- TikZ の SVG は `web/public/images/tikz/...` に出る。`rsvg-convert` などで画像にして目視する。
- `tikzpicture` を含まない `figure`（作図予定の TODO だけの図）は、今の `tex_to_md.py` では Web に生の TeX として出る。作図予定の図を残したまま公開しない。
- 変換コード（`scratch/tex_to_md.py` など）自体を直した場合の全件確認は `AGENT.md` 4節。

## W6. 手本の図（figure 付録 B）

2026-11-13 に今の figure-rules と照合し、食い違っていた4件の図を直した（図のブロックだけの変更。差分チェッカーで PASS を確認）。

| 用途 | ファイル | 照合の結果 |
|---|---|---|
| 座標グラフと座標軸への垂線 | `src/utokyo/zenki/2008/4/solution.tex` | 垂線を `densely dotted, thick, gray!70!black` に直した（中点 M への補助線は強調の赤の点線） |
| 不等式領域と複数パネル | `src/utokyo/zenki/1977/3/solution.tex` | 軸を `gray!80!black`、参考線・延長線・補助線を点線（線と同じ濃い色）に直した。図2・図4のラベルの重なりも直した |
| 立体の面・隠れ線 | `src/utokyo/zenki/2008/3/solution.tex` | 隠れ線を輪郭と同じ色の破線に、平面図の補助線を点線に直した。図1の「軸 $l$」と点 E のラベルの重なりも直した |
| 状態遷移 | `src/utokyo/zenki/2008/2/solution.tex` | 食い違いなし |
| 3D（tikz-3dplot の記法） | `src/titech/zenki/1985/2/solution.tex` | 視点を `{65}{115}`、`center` 環境を `\centering`、軸を `gray!80!black` に直した。図1の E・V のラベルの重なりも直した |
| 数式中の図形アイコン（figure §5.3） | `src/titech/zenki/1971/4/solution.tex` | アイコンは規約どおり。同じファイルのほかの図は `center` 環境と薄い `gray` の破線を使っているので、手本にしない |

## W7. 記法の規約の置き場所

- 汎用の記法は `references/notation-rules.md`、表は `references/table-rules.md`、このリポジトリ固有の記法（見出し、小問、subfiles、problem.tex など）は `local/notation.md`。
- `AGENT.md` 8.3.6 節は、これらへの案内だけになった。`AGENTS.md` には、主な規則の要約が残っている（食い違う場合は報告する）。
