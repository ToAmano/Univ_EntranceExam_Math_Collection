# 東大前期 1961–2014 監査台帳

## 範囲と方法

`src/utokyo/zenki` の54年度316問題ディレクトリを対象とする。静的スキャンの実行日は2026-10-27（米国中部時間）。入力のSHA-256と全16候補は [static-report.json](static-report.json) に保存した。16件は省略表現・旧番号の機械的候補であり、問題の確定判定ではない。

原稿・problem.tex・solution.tex・TikZ・進捗状態は監査で変更しない。手書きPDFの物理ページ対応、解答PDFの全ページ、Web表示、原稿との数式照合、独立した証明検算を別々の確認状態として扱う。画像監査の作業パケットは `/tmp/utokyo-zenki-1961/packet2`、ローカルAIの候補は `/tmp/utokyo-zenki-1961/review` にある。これらの一時ファイルは永続的な証拠ではないため、確定した指摘はIssueへ記録する。

## Issueの整理

文字起こしが完成していた [#423](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/423)、[#478](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/478)、[#479](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/479) は、対応コミットをコメントしてcloseした。行列・一次変換の解答作成Issue14件と1999年第2問の論証Issue #778は、解答の欠落または未解決の指摘が現存するためopenを維持する。

## 1961年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。原稿全7ページを通覧し、各問題のTeX本文と結論を照合・独立検算した。一時コピーのPDFは第1・2・3・5・6問で各1ページ生成し、全ページを表示確認。第4問は末尾の余分な `\end{multicols}` によりコンパイル失敗。Web実表示は全問未確認。

| 問 | 原稿物理ページ | PDF | 指摘 |
|---|---:|---|---|
| 1 | 2 | 1ページ確認 | [#977](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/977)：出発時刻 `t=0` の扱いは要判断 |
| 2 | 3 | 1ページ確認 | [#978](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/978)：`f(0.1)` の記号が原稿と異なる |
| 3 | 4 | 1ページ確認 | [#979](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/979)：底面半径の分母が原稿と異なる |
| 4 | 5 | 生成失敗 | [#976](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/976)：未対応の環境終端と誤字 |
| 5 | 6 | 1ページ確認 | [#980](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/980)：図中ラベルの重なり |
| 6 | 7 | 1ページ確認 | [#981](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/981)：極値条件の誤記と積分上端の表示 |

1961年度はWeb表示と第4問の修正後PDFが未確認であり、監査完了とはしない。

## 1962年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。第1・2・4問は一時コピーで解答PDFを生成し、全ページ（第1・4問は各1ページ、第2問は3ページ）を表示した。第3・5・6問は現在の原稿からPDFを生成できない。第1・4問は手書きとTeXの結論を照合し、独立計算でも確認済み。第6問は接線の交点と面積の式を独立計算で検算したが、手書き照合と生成図の目視は未実施。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 1ページ確認 | 対数の底による場合分けと結論 `1<a<b` または `b<a<1` を確認。確定指摘なし |
| 2 | 3 | 3ページ確認 | [#985](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/985)：複数の等式が不成立。最終答案は独立計算で一致 |
| 3 | 4 | 生成失敗 | [#982](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/982)：未定義コマンドと垂足の座標誤記。最終値 `tan θ=3` は独立計算で一致 |
| 4 | 5 | 1ページ確認 | 望遠和と `|r|` の場合分けを確認。確定指摘なし |
| 5 | 6 | 生成失敗 | [#983](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/983)：未定義コマンドに加え、辺長の答えに不可能な値。体積の最大値4は一致 |
| 6 | 7 | 生成失敗 | [#984](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/984)：旧図入力のエラー。接線交点・面積の数値検算は一致 |

1962年度は第3・5・6問の生成PDF、手書きとの詳細照合、全問のWeb実表示が未確認であり、監査完了とはしない。

## 1963年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。第2問は生成PDF全3ページ、第3問は全2ページを表示確認。第1・4・5・6問の `solution.tex` は旧 `jarticle` 形式で LuaLaTeX の生成が停止する。これらは既存の形式移行Issue [#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593) に列挙されており、PDF・Webの表示確認を保留した。手書き物理2・3・4・6・7ページと対応TeXを拡大照合した。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で生成失敗 | [#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)。手書きとの式・結論照合および独立検算では `4<c<√34` が一致。PDF・Webは未確認 |
| 2 | 3 | 全3ページ確認 | [#987](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/987)：図1の指定長と描画座標が不一致。面積 `4+2π/3` は独立計算で一致 |
| 3 | 4 | 全2ページ確認 | [#988](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/988)：面積公式の説明に誤り。最終和 `Ha²/[2(a+b)]` は検算で一致 |
| 4 | 5 | 旧形式で生成失敗 | [#989](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/989)：四面体の体積式で `S` の意味が不一致。最終値は一致 |
| 5 | 6 | 旧形式で生成失敗 | [#990](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/990)：面積等式・積分指数が原稿から崩れている。最終値は一致 |
| 6 | 7 | 旧形式で生成失敗 | [#991](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/991)：係数決定の式が崩れている。最終値 `n=3` は一致 |

1963年度は旧形式4問のPDF、Web全問、第4問の原稿細部照合などが未確認であり、監査完了とはしない。

## 1964年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。原稿全ページを表示し、各問のTeX本文と主な式・結論を照合した。6問すべての `solution.tex` が旧 `jarticle` 形式で、一時コピーで各問を LuaLaTeX 実行するといずれも `This file needs format pLaTeX2e` で停止した。形式移行は [#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)。第5問の現存するWeb HTMLには `\input{macros}` と `oframed` 環境が生で残り、この広い影響を #593 に追記した。全問のブラウザー実表示と生成PDF全ページは未確認。

| 問 | 原稿物理ページ | 独立検算・指摘 |
|---|---:|---|
| 1 | 2 | Vièteの関係から `a³+b³+c³=z³+3yz+3x` を確認。確定指摘なし。PDFは旧形式で生成失敗；公開Webの旧形式命令は [#1247](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1247) に記録 |
| 2 | 3 | 内分点の係数比較で `P=(-6,3)`、`m:n=2:1` を確認。確定指摘なし。PDFは旧形式で生成失敗；公開Webの旧形式命令は [#1248](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1248) に記録 |
| 3 | 4 | [#992](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/992)：手書きの立体・断面図が欠落。断面積 `350 cm²` は検算で一致 |
| 4 | 5 | [#995](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/995)：手書きの座標図が欠落。面積 `3/5` は検算で一致 |
| 5 | 6 | [#994](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/994)：増減表とWeb本文の表示不良。最小距離と `a=3^{3/4}` は検算で一致 |
| 6 | 7 | [#993](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/993)：判別式の符号・端点条件が原稿と異なり、現在の証明が不成立。最終の最大・最小の組は独立計算で一致 |

1964年度は全問の生成PDFとブラウザー実表示が未確認であり、監査完了とはしない。

## 1965年度

年度別手書きPDFは3ページ。物理1ページは表紙と第1・3〜6問の**答えの概要メモ**、物理2ページだけに第2問の途中計算と図があり、物理3ページはほぼ空白。したがって第3〜6問は詳細な手書き原稿との逐語照合ができない。第1・2問の生成PDFは各2ページで全ページを表示し、第2問の原稿も拡大照合した。第3〜6問は旧 `jarticle` 形式で、現行LuaLaTeXのPDF生成を保留（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。全問のブラウザー実表示は未確認。

| 問 | 手書きの根拠 | PDF | 指摘・確認結果 |
|---|---|---|---|
| 1 | 物理1ページの答えメモ | 全2ページ確認 | [#1245](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1245)：公開Webではベン図2点のSVGが404、図番号が逆順で `\quad` も生表示。PDF上の図と割合 `48%,10%,5%,2%` は独立検算で一致 |
| 2 | 物理2ページの詳細原稿 | 全2ページ確認 | [#1000](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1000)：途中式に未定義の変数 `A`。標高1954mは一致 |
| 3 | 物理1ページの答えメモのみ | 旧形式で未生成 | [#996](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/996)：交点の条件を緩めている。最大面積 `2/3` は一致 |
| 4 | 物理1ページの答えメモのみ | 旧形式で未生成 | `k=√2−1` の場合分けとPの位置を独立検算。確定指摘なし；公開Webの旧形式命令は [#1249](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1249) に記録 |
| 5 | 物理1ページの答えメモのみ | 旧形式で未生成 | [#997](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/997)：未定義命令・変数。接線3本は独立検算で一致 |
| 6 | 物理1ページの答えメモのみ | 旧形式で未生成 | [#998](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/998)：円錐体積の因子が逆。最終体積 `2π/3` は一致 |

1965年度は第3〜6問の詳細な原資料がなく、PDF・Webも未確認のため監査完了とはしない。

## 1966年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。第1〜4問は旧 `jarticle` 形式で現行LuaLaTeXのPDF生成を保留（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。第5問は生成PDF全2ページ、第6問は全3ページを表示確認した。手書き第5・6問にあるのは新課程の解答だけで、旧課程の途中式は原稿照合できないため、独立計算で検証した。全問のブラウザー実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で未生成 | [#1001](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1001)：式の変数誤記と解答の大幅な欠落。手書きの答えは `(a,b)=(3.1,1.6)` |
| 2 | 3 | 旧形式で未生成 | [#1002](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1002)：写像の最初の等式が逆。最終の2直線は検算で一致 |
| 3 | 4 | 旧形式で未生成 | [#1003](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1003)：問題文の回転方向が未確定の可能性、問題図の座標も条件と不一致。公式原題の確認待ち |
| 4 | 5 | 旧形式で未生成 | [#1004](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1004)：関数の符号・単調性・値が原稿から崩れている。最終整数5は一致 |
| 5 | 6 | 全2ページ確認 | [#1005](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1005)：旧課程の最終答案に負号がなく、許される `a+b` の範囲が変わる。新課程は原稿と一致 |
| 6 | 7 | 全3ページ確認 | [#1006](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1006)：旧課程の折り返し条件の証明に不成立の等式。最終直線と新課程の確率は一致 |

1966年度は旧形式4問の生成PDF、旧課程2問の手書き詳細原稿、ブラウザー実表示が未確認であり、監査完了とはしない。

## 1967年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。全ページを表示し、各問の手書き本文・式・図を現行TeXと照合した。第1・3・4問は旧 `jarticle` 形式で、現行LuaLaTeXのPDF生成を保留（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。第2問は生成PDF全2ページ、第5・6問は各3ページを表示確認した。第5・6問の手書きには新課程の解答のみがあり、旧課程の証明は独立計算で検証した。全問のブラウザー実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で未生成 | [#1007](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1007)：`x=0` の確認が欠落し、`n=1` で偽となる厳密不等号を使用。主張は真 |
| 2 | 3 | 全2ページ確認 | [#1008](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1008)：図の `z` 軸と点Aの座標ラベルが重なる。高度1000mは手書き・独立計算と一致 |
| 3 | 4 | 旧形式で未生成 | [#1009](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1009)：`c,s` の定義欠落、増減表の命令誤記、再掲問題文の誤字。最大面積 `3√3/4` は一致 |
| 4 | 5 | 旧形式で未生成 | 手書きの3図に対応する図入力3点は存在。回転・伸縮変換から面積 `2√3π/3` を独立検算。確定指摘なし；公開Webの旧形式命令は [#1250](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1250) に記録 |
| 5 | 6 | 全3ページ確認 | 新課程の接点・面積 `2√e/3−1` は手書きと一致。旧課程の接点条件から `a=−3,1,3/2` を独立検算。確定指摘なし |
| 6 | 7 | 全3ページ確認 | 新課程の完全順列数9から確率 `1/320` は手書きと一致。旧課程の漸化式・極限 `A₀A=4` を独立検算。確定指摘なし |

1967年度は旧形式3問の生成PDF、旧課程2問の手書き詳細原稿、全問のブラウザー実表示が未確認であり、監査完了とはしない。

## 1968年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。手書き全ページと各問のTeX本文・結論を照合し、主な式を独立検算した。6問すべての解答が旧 `jarticle` 形式で、現行LuaLaTeXでの生成PDFおよびWeb実表示は未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。

| 問 | 原稿物理ページ | 指摘・確認結果 |
|---|---:|---|
| 1 | 2 | [#1011](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1011)：`sin²t` の原始関数の係数が誤り。定積分と最終値 `α=−1` は一致 |
| 2 | 3 | [#1012](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1012)：斜面の法線の符号が誤り、手書きの立体図も欠落。角 `π/3` は一致 |
| 3 | 4 | [#1010](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1010)：二次式の `a≠0` を落とし、座標軸・除外直線を取り違える。**結論が変わる** |
| 4 | 5 | 円盤断面の半径平方 `2−2z²+z⁴` と体積 `46π/15` は手書き・独立計算と一致。確定指摘なし；公開Webの旧形式命令は [#1251](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1251) に記録 |
| 5 | 6 | 奇三次式の係数条件を検算し `P(x)=4x³+x` は手書きと一致。確定指摘なし；公開Webの旧形式命令は [#1252](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1252) に記録 |
| 6 | 7 | 単調性による不等式、`2^{200}` の桁数・最上位、常用対数の範囲を手書きと照合。確定指摘なし；公開Webの旧形式命令は [#1253](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1253) に記録 |

1968年度は全問の生成PDFとブラウザー実表示が未確認であり、監査完了とはしない。

## 1969年度

`src/utokyo/zenki/1969/handwritten_tex.tex` には、東大紛争のため前期入試が実施されなかった旨のコメントがある。この年度には問題ディレクトリ、手書きPDF、解答TeXが存在しないため、問題単位の監査対象はない。

## 1970年度

問題は4問で、手書きPDF物理1ページが表紙、第1〜4問は物理2〜5ページに各1問。原稿全ページと各問題・解答TeXを照合し、主な式・結論を独立検算した。第1〜3問は旧 `jarticle` 形式で生成PDFを未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。第4問は一時コピーから解答PDF全2ページを生成・表示確認した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で未生成 | [#1013](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1013)：冒頭の `a^n=1` は誤りで、正しくは `a^6=1`。ヘッダの年度・問題番号も空欄。結論は一致 |
| 2 | 3 | 旧形式で未生成 | [#1016](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1016)：解答ファイルで再掲された問題文の「貨幣」が「効果」に変化。確率は手書き・独立計算と一致 |
| 3 | 4 | 旧形式で未生成 | [#1014](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1014)：手書きの関数図が文字 `a` だけに置換され、増減表の命令も壊れている。最小速度 `15/4 m/s` は一致 |
| 4 | 5 | 全2ページ確認 | [#1015](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1015)：到達領域の答えに `X` の条件がなく結論が広すぎる。生成図では噴出口と軌道の高さが不一致、ラベルも重なる。(1)(2)の結論は一致 |

1970年度は旧形式3問の生成PDFと全問のWeb実表示が未確認であり、監査完了とはしない。

## 1971年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。原稿全ページと6問の問題・解答TeXを照合し、主要な式と結論を独立検算した。6問すべてが旧 `jarticle` 形式のため、現行LuaLaTeXの生成PDFとWeb実表示は未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。

| 問 | 原稿物理ページ | 指摘・確認結果 |
|---|---:|---|
| 1 | 2 | [#1017](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1017)：手書きの `c=cos t,s=sin t` が消え、距離と距離の二乗の記号を混同。最小1・最大2と時刻は一致 |
| 2 | 3 | [#1018](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1018)：問題の「以下」を「未満」に強めて証明。元の条件でも `2−x>nε²` は導ける |
| 3 | 4 | 平方完成を独立検算し、最小にする `(a,b)=(24,−10)` は手書きと一致。確定指摘なし；公開Webの旧形式命令は [#1254](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1254) に記録 |
| 4 | 5 | [#1019](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1019)：導関数と参照の誤記、増減表の命令誤記。奇数次1根・偶数次0根の結論は一致 |
| 5 | 6 | [#1020](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1020)：`Q` の添字と平均平方距離の定数項に誤り。極限 `1+a²+b²` と原点で最小の結論は一致 |
| 6 | 7 | [#1021](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1021)：両解法の最終式に未定義の `n` が残り、補助数列・和の範囲も不整合。正答 `(2k−1)/3^k` は手書きと独立計算で一致 |

1971年度は全問の生成PDFとWeb実表示が未確認であり、監査完了とはしない。

## 1972年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。原稿全ページと6問の問題・解答TeXを照合し、主要な式・結論を独立検算した。第1・5問は旧 `jarticle` 形式で生成PDFを未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。第2・3・4・6問は一時コピーで各2ページの解答PDFを生成し、全ページを表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で未生成 | [#1022](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1022)：二次不等式の向きが逆。面積 `13π+75√3` は一致 |
| 2 | 3 | 全2ページ確認 | [#1023](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1023)：TikZの具体値が問題の `|AB|=1` と求めた角・辺長を満たさない。最終の3組は一致 |
| 3 | 4 | 全2ページ確認 | [#1026](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1026)：問題図の円と直線が外接せず交差し、解答には垂足の添字不一致と `R'` の欠落。極限 `R` は一致 |
| 4 | 5 | 全2ページ確認 | 有理関数の微分・増減・漸近線と実根数を手書き・独立計算で確認。確定指摘なし |
| 5 | 6 | 旧形式で未生成 | [#1024](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1024)：積分下端の `0` が `o` に変化、初期条件 `u(0)=0` も崩れる。`h(x)=−x` は一致 |
| 6 | 7 | 全2ページ確認 | [#1025](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1025)：表の倍率が逆で `17/32=0.531` も不成立。最適地点と確率 `17/32` は一致 |

1972年度は旧形式2問の生成PDFと全問のWeb実表示が未確認であり、監査完了とはしない。

## 1973年度

手書きPDF物理1ページは表紙、2ページは空白、第1〜6問は物理3〜8ページに各1問。手書き全ページと6問の問題・解答TeXを照合し、主要な式・結論を独立検算した。6問すべて旧 `jarticle` 形式のため、現行の生成PDFとWeb実表示は未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。

| 問 | 原稿物理ページ | 指摘・確認結果 |
|---|---:|---|
| 1 | 3 | [#1027](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1027)：冒頭に未定義の `\1` があり、手書きの `c=cos θ, s=sin θ` の定義が欠落。8秒、最大 `√15 a`・最小 `√13 a` は一致 |
| 2 | 4 | 0・1・2の個数から `f_k` を表す計算は手書き・独立計算と一致。確定指摘なし；公開Webの旧形式命令は [#1255](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1255) に記録 |
| 3 | 5 | `a` の4区間での `V(a)` を確認。最小値 `1/2`、そのとき `a=1/2` は手書きと一致。確定指摘なし；公開Webの旧形式命令は [#1256](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1256) に記録 |
| 4 | 6 | [#1028](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1028)：解答内の再掲問題文で `S∩T(P)` が `S∩P(P)` に、面積条件の「1/2以上」が「1/2」に変化。解法と面積 `2(1−log 2)` は原題に対して正しい |
| 5 | 7 | [#1029](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1029)：二次不等式の向きが逆で、積分記法にも余分な `dx`。導関数 `2(t²−1)log t/(1+t²)²` は一致 |
| 6 | 8 | 放物線の係数と接線勾配 `(2v−u)/u` は手書き・独立計算と一致。確定指摘なし；公開Webの旧形式命令は [#1257](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1257) に記録 |

1973年度は全問の生成PDFとWeb実表示が未確認であり、監査完了とはしない。

## 1974年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。手書き全ページと6問の問題・解答TeXを照合し、主要な式・結論を独立検算した。第3問は一時コピーから解答PDF全1ページを生成・表示確認。ほかの5問は旧 `jarticle` 形式のため現行の生成PDFを未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で未生成 | [#1030](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1030)：第(3)問の最終行が `f_4(n)` のままで、問われた `f_{100}(n)` を答えていない。値の集合 `{0,1,5,6}` は一致 |
| 2 | 3 | 旧形式で未生成 | 中点の高さを相加相乗平均で最小化する計算と2つの座標は手書き・独立計算と一致。確定指摘なし |
| 3 | 4 | 全1ページ確認 | [#1031](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1031)：生成した解答図では元の問題図の寸法表示が欠け、自動文字起こしの要確認表示も残る。座標の結論は一致 |
| 4 | 5 | 旧形式で未生成 | [#1032](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1032)：再掲問題文と `g` の極限式に転記ミスがあり、商の極限の扱いも補足が必要。`a=1` は一致 |
| 5 | 6 | 旧形式で未生成 | [#1033](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1033)：**第(1)問の横座標の答えが `3cos³θ` となり誤り**。正しくは `4cos³θ`。導関数・弧長の途中計算も不成立。第(2)(3)問の結論は一致 |
| 6 | 7 | 旧形式で未生成 | [#1034](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1034)：優勝確率と比較式の演算子が転記で変化。3つの設問の結論は手書き・独立計算と一致 |

1974年度は旧形式5問の生成PDFと全問のWeb実表示が未確認であり、監査完了とはしない。

## 1975年度

手書きPDF物理1ページは表紙、第1〜6問は物理2〜7ページに各1問。手書き全ページと6問の問題・解答TeXを照合し、主要な式・結論を独立検算した。第1・5・6問は一時コピーから解答PDFを生成し、それぞれ全3・2・2ページを表示確認。第2・3・4問は旧 `jarticle` 形式で生成PDFを未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 全3ページ確認 | [#1035](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1035)：第1図の `x`,`y` が本文の定義と逆。要確認表示も残る。3場合の長さ比較と `C` から24の点という結論は一致 |
| 2 | 3 | 旧形式で未生成 | `x=−1,1` による条件と恒等式の係数比較を検算。`(k,l,m,n)=(1,1,0,1)` は手書きと一致。確定指摘なし；公開Webの旧形式命令は [#1258](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1258) に記録 |
| 3 | 4 | 旧形式で未生成 | 接点の範囲と面積の最大化を検算。`(a,b)=(1,3)`、面積 `9/2` は手書きと一致。確定指摘なし；公開Webの旧形式命令は [#1259](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1259) に記録 |
| 4 | 5 | 旧形式で未生成 | [#1036](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1036)：**一般項 `θ_n` の最終式が初項を満たさない**。正しくは `π/2−π/2^(n+1)`。極限 `π/2` は一致 |
| 5 | 6 | 全2ページ確認 | [#1037](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1037)：問題図の球の配置が条件に反し、積分区間の向きと記号・解説の等号にも誤り。共通体積と無限和の最終値は手書き・独立計算と一致 |
| 6 | 7 | 全2ページ確認 | [#1038](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1038)：期待値の計算が後方の別式を参照。遷移確率、期待値 `3−2(5/6)^n`、極限3は一致 |

1975年度は旧形式3問の生成PDFと全問のWeb実表示が未確認であり、監査完了とはしない。

## 1976年度

手書きPDF物理1ページは表紙、第1問は2ページ、第2問は3–4ページ、第3・4・5問は5・6・7ページ、第6問は8ページ。ただし第3・5問の旧課程と第6問の手書き解答本文は確認できず、その部分は原題と独立計算で検証した。第3〜6問は一時コピーから解答PDFを生成し、全4・4・3・4ページを表示確認。第1・2問は旧 `jarticle` 形式で生成PDFを未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で未生成 | [#1039](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1039)：`f(0)=2c` は誤りで正しくは0。体積の最大条件と `r,l` の結論は一致 |
| 2 | 3–4 | 旧形式で未生成 | [#1040](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1040)：**1回以上左折する条件を落とし、到達範囲を境界込みの菱形としている**。頂点などは到達不能で、最終領域が広すぎる |
| 3 | 5（新課程のみ） | 全4ページ確認 | [#1041](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1041)：第1図の中心間距離と旧課程の円Bまでの距離評価が誤る。新課程の最小・最大距離と旧課程の円弧長は独立計算と一致 |
| 4 | 6 | 全4ページ確認 | [#1042](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1042)：`f(α)` の微分を負と書きながら正と結論し、別解の代数にも符号誤り。図の上端数値と近接目盛も要修正。軌跡の式は一致 |
| 5 | 7（新課程のみ） | 全3ページ確認 | 円柱側面の積分 `4π/3+2√3` と、旧課程の面積 `e^{2t}/2−2e^t+2t+3/2` を独立検算。確定指摘なし。旧課程は手書きとの照合不可 |
| 6 | 8（見出しのみ） | 全4ページ確認 | [#1043](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1043)：旧課程の仮定で `f''` を `f'` とし、二次因子への代入では `2αβ` が欠落。結論は独立計算と一致。手書きとの照合不可 |

1976年度は旧形式2問の生成PDF、全問のWeb実表示、手書きがない課程の原稿照合が未確認であり、監査完了とはしない。

## 1977年度

手書きPDFは全8ページ。物理1ページが表紙、第1・2問は物理2・3ページ、第3問は物理4〜5ページ、第4〜6問は物理6〜8ページ。第5・6問の手書き原稿には新課程の解法だけがあり、旧課程の詳細は独立検算した。第1問は旧 `jarticle` 形式で、現行方式のPDF・Web表示は未確認（[#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593)）。第2〜6問の生成PDFは全1・6・2・4・5ページを表示した。第5問の問題PDF全1ページも表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 旧形式で未生成 | 手書きの最小値 `M(1/4)=1/4` は解答TeXの結論と一致。増減と2曲線の交点を独立検算。旧形式の移行・表示確認は未了；公開Webの旧形式命令は [#1260](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1260) に記録 |
| 2 | 3 | 全1ページ確認 | [#1044](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1044)：本文の「下図」に対応する図がない。有理性の同値関係は独立検算で一致 |
| 3 | 4〜5（全体は原稿あり） | 全6ページ確認 | [#1045](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1045)：**第(1)問で含まれない下端を含めており、値域の結論が変わる**。領域 `C` の向き、半径と境界の距離、別の領域条件にも誤記。第(2)問の下端は独立計算と一致 |
| 4 | 6 | 全2ページ確認 | [#1046](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1046)：軌跡の後半2円弧の接続点は `8−a` だが、手書きとTeXの式は `6+a`。図は正しい。体積 `π{12(a−1)²+40/3}` と最小値は独立計算と一致 |
| 5 | 7（新課程のみ） | 全4ページ確認 | 新課程の行列成分と軌跡 `x²+y²=25` から `(-3,-4)` を除く結論は手書き・独立計算と一致。旧課程の円周角と5弧の構成も独立検算。確定指摘なし。問題PDFの図も確認 |
| 6 | 8（新課程のみ） | 全5ページ確認 | [#1047](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1047)：旧課程の凹凸表に未定義の `x₀`、新課程の交点存在条件にも説明不足。平面と交点は手書きと一致し、旧課程の変曲点2個／4個も独立検算で一致 |

1977年度は第1問の生成PDF、旧課程2問の手書き詳細原稿、全問のWeb実表示が未確認であり、監査完了とはしない。

## 1978年度

手書きPDFは全7ページ。物理1ページが表紙、第1〜6問は物理2〜7ページに各1問。原稿全ページと6問のTeXを照合し、主要な式・結論を独立検算した。第1〜6問の生成解答PDFは全2・2・3・2・1・3ページを表示した。問題図がある第1・6問の問題PDFも各全1ページを表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ、問題全1ページ確認 | [#1049](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1049)：問題図の円が指定された半径に接せず、太線の囲み領域も不完全。半径 `2√3−3` と面積は手書き・独立検算と一致 |
| 2 | 3 | 全2ページ確認 | [#1048](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1048)：`f(t)≤f(t+1)` の導出で不等号が逆。区分式とグラフは手書き・独立検算と一致 |
| 3 | 4 | 全3ページ確認 | [#1050](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1050)：**法線が1本の領域で、正の `y` の境界を誤って含む**。面積積分の上下も逆だが、最終値 `88√2/135` は一致 |
| 4 | 5 | 全2ページ確認 | [#1051](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1051)：`A²` の右上成分と `u` の極限式に誤り。`A^n` と極限の最終答案は独立検算と一致 |
| 5 | 6 | 全1ページ確認 | [#1246](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1246)：公開Webで等分点間の長さの式がMathJaxの二重添字エラーになり、式全体が生TeX表示。PDF上の図は良好で、余弦定理と区分求積法による極限 `(-a²+3b²+3c²)/6` は手書きと一致 |
| 6 | 7 | 解答全3ページ、問題全1ページ確認 | [#1052](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1052)：問題図の接線配置、解答図の開端点、最大面積の証明の根拠を要修正。`f=max{g,h}` と極値 `√3/9`, `4/27` は一致 |

1978年度は全問のWeb実表示が未確認であり、監査完了とはしない。

## 1979年度

手書きPDFは全8ページ。物理1ページが表紙、第1〜5問は物理2〜6ページ、第6問は物理7〜8ページ。第1問の手書き解答は空欄で、解答作成Issue [#436](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/436) を維持する。第2〜6問は手書き原稿とTeXを照合し、主要な式・結論を独立検算した。第2〜6問の生成解答PDFは全2・1・2・2・3ページを表示確認。問題図がある第2・6問の問題PDFも各全1ページを表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2（解答は空欄） | 解答の実質的な内容なし | [#436](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/436) をopenのまま維持。`solution.tex` も空欄の旨を記したコメントのみ |
| 2 | 3 | 解答全2ページ、問題全1ページ確認 | [#1054](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1054)：問題図の母線が球を横切り、接円と一致しない。`K` と `D` のラベルも逆。解答の体積 `2π(11−6√3)/3` は手書き・独立計算と一致 |
| 3 | 4 | 解答全1ページ確認 | [#1053](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1053)：周期性の証明中で代入の順序が2か所入れ替わる。最終的な合同類 `a≡−1,0,2 mod 4` は手書き・独立計算と一致 |
| 4 | 5 | 解答全2ページ確認 | [#1055](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1055)：2円の式が改行されず連結表示され、図のラベルも近接。最大値 `2(4−√6)/3` と最小値 `2/3` は手書き・独立計算と一致 |
| 5 | 6 | 解答全2ページ確認 | [#1056](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1056)：参照した図が最終答案の後、単独ページに配置。独立積分では `S(t)=t²(2t+3)/{12(t+1)³}`、極限 `1/6` で手書きと一致 |
| 6 | 7〜8 | 解答全3ページ、問題全1ページ確認 | 複素数の漸化式と相似比の別解を独立検算。`P_6=(a²/(a²+1)², a/(a²+1))` と収束点 `(a²/(a⁴+3a²+1), a(a²+1)/(a⁴+3a²+1))` は手書きと一致。確定指摘なし |

1979年度は第1問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1980年度

手書きPDFは全7ページ。物理1ページが表紙、第1〜6問は物理2〜7ページに各1問。第3問の手書き解答は空欄で、`solution.tex` も未解答のプレースホルダー。既存の解答作成Issue [#442](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/442) に再確認結果を追記し、Openを維持した。第1・2・4・5・6問は手書き原稿とTeXを照合し、主要な式・結論を独立検算した。生成解答PDFは順に全2・2・2・1・3ページを表示確認した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ確認 | [#1057](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1057)：内側の正三角形の辺 `r` を `AB'` と定義し、後の `AB'=p+r` と矛盾。メネラウスの対象名と余弦定理の区切りも要修正。`BB'`・`PB'` と面積条件の解 `(7−√21)/14` は手書きと一致 |
| 2 | 3 | 解答全2ページ確認 | [#1058](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1058)：切断円を三角形 `NAB` の外接円と誤認し、本文で半径を2倍に記述。図と弧長の計算は正しく、合計 `(1/2+2√6/9)π` は手書きと一致。最終式だけがPDF2ページ目に孤立 |
| 3 | 4（解答は空欄） | 解答プレースホルダー | [#442](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/442) をOpenのまま維持。手書き原稿とTeXの双方に解答がない |
| 4 | 5 | 解答全2ページ確認 | [#1059](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1059)：`sin 2t` を `sin(t/2)` とし、`g'(p)` の三次項を次行で二次とする。結論の最大値 `k²/16+2` と区分された最小値は手書き・独立計算と一致 |
| 5 | 6 | 解答全1ページ確認 | [#1060](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1060)：初期条件の説明で `p₀(1)=1` と誤記。正四面体の模式図も底辺と側辺が異なる座標を使用。漸化式と最終答案は手書きと一致 |
| 6 | 7 | 解答全3ページ確認 | [#1061](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1061)：辺 `OA` 上の点の `x` 座標に負号があり、直後の等式は成立しない。**証明の修正が必要**。面積の最終式は手書き・独立積分と一致 |

1980年度は第3問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1981年度

手書きPDFは全9ページ。物理1ページが表紙、第1〜3問は物理2〜4ページ、第4問は物理6ページ、第5問は物理7ページ、第6問は物理8〜9ページ。物理5ページには第4問周辺のメモがある。原稿と全6問のTeXを照合し、主要な式・結論を独立検算した。第1〜6問の生成解答PDFは全1・2・2・2・3・7ページを表示確認。第5問の問題PDF全1ページも表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全1ページ確認 | [#1063](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1063)：`k=2` では積が空積なのに奇数因子 `k+1` で除外しており、論証が欠ける。組合せの中間式にも階乗の括弧不足。最終組 `(n,k)=(6,3)` は独立数え上げと一致 |
| 2 | 3 | 解答全2ページ確認 | [#1062](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1062)：**最終答案の期待値が3倍大きい**。原稿・TeXともに `√3/36×(3/2+6+3/2)` を `3√3/4` とするが、正しくは `√3/4`。216通りを独立列挙して確認。図の直角位置と `A₆` ラベルも要修正 |
| 3 | 4 | 解答全2ページ確認 | [#1064](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1064)：端点では法線上の係数 `s=0` なのに `s>0` と断言。領域図が最終答案の後、単独ページに配置。面積 `1/3` は手書き・独立積分と一致 |
| 4 | 6（5はメモ） | 解答全2ページ確認 | [#1065](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1065)：手書きでは正しい `z²tan²α=x²+y²` が、TeXの式(3)では `z²=·tan²α=x²+y²` と破損。個数と `z` の結論は独立計算と一致 |
| 5 | 7 | 解答全3ページ、問題全1ページ確認 | [#1066](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1066)：正n角錐の展開図で側面辺が等しくない。手書きは体積の平方に相当する多項式を微分するが、TeXは同じ式を `V'` とする。最終体積と極限は一致 |
| 6 | 8〜9 | 解答全7ページ確認 | [#1067](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1067)：判別式の不等号、`g/h` の混同、`a=0` の係数比較に複数の矛盾があり、**場合分けの証明を修正する必要がある**。最終的な係数領域と最小化結果 `f(x)=1−x²`, `I=6` は独立検算と一致 |

1981年度は全問のWeb実表示が未確認のため、監査完了とはしない。

## 1982年度

手書きPDFは全7ページ。物理1ページが表紙、第1〜6問は物理2〜7ページに各1問。第1問の手書き解答は空欄で、`solution.tex` も未解答のコメントのみ。既存の解答作成Issue [#449](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/449) に再確認結果を追記し、Openを維持した。第2〜6問は手書き原稿とTeXを照合し、主要な式・結論を独立検算した。生成解答PDFは全3・3・1・1・1ページを表示確認。第3・4問の問題PDFも各全1ページを表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2（解答は空欄） | 解答プレースホルダー | [#449](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/449) をOpenのまま維持。手書き原稿とTeXの双方に解答がない |
| 2 | 3 | 解答全3ページ確認 | 接球する正四面体の辺長 `2√2`、面までの距離 `√3/3`、4個の球冠の体積から `8π/3(1−4√3/9)` を独立検算。手書きと一致し、確定指摘なし |
| 3 | 4 | 解答全3ページ、問題全1ページ確認 | [#1068](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1068)：問題図で `AB≠1` かつ `C∉AB`。解答の直線式と `|MC|²` の展開にも誤記があり、含まれない端点を最大値と呼ぶ。最終的な角度・長さの範囲は独立計算と一致 |
| 4 | 5 | 解答全1ページ、問題全1ページ確認 | [#1069](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1069)：加速度の途中式で分母の次数が過大。次行と最終答案 `max|α|=V²` は正しい |
| 5 | 6 | 解答全1ページ確認 | [#1070](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1070)：切断面の記号を `l`/`k`/`y` と混用し、断面図は `k>1/3` で上辺の傾きが逆。体積 `7/4` は独立積分と一致 |
| 6 | 7 | 解答全1ページ確認 | [#1071](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1071)：`r_n` の漸化式と一般項の添字が誤り、極限記号が式に連結表示。極限 `p,r→1/6, q→2/3` は手書き・独立計算と一致 |

1982年度は第1問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1983年度

手書きPDFは全7ページ。物理1ページが表紙、第1〜6問は物理2〜7ページに各1問。第1問の手書き解答は空欄で、`solution.tex` も未解答のコメントのみ。既存の解答作成Issue [#450](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/450) に再確認結果を追記し、Openを維持した。第2〜6問は手書き原稿とTeXを照合し、主要な式・結論を独立検算した。生成解答PDFは全1・3・2・2・4ページを表示確認。第3〜5問の問題PDFも各全1ページを表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2（解答は空欄） | 解答プレースホルダー | [#450](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/450) をOpenのまま維持。手書き原稿とTeXの双方に解答がない |
| 2 | 3 | 解答全1ページ確認 | [#1072](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1072)：**最終答案 `a_n=2^n` は初項 `a_1=1` と矛盾**。正しくは `a_n=2^{n−1}`。手書きは正しく、集合和の独立列挙でも確認 |
| 3 | 4 | 解答全3ページ、問題全1ページ確認 | [#1073](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1073)：問題図の直線 `ℓ` が点 `A` を通らず、別解の等号成立条件も `t≥0` の制約と未整合。最短距離の区分式は手書き・独立計算と一致 |
| 4 | 5 | 解答全2ページ、問題全1ページ確認 | [#1074](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1074)：問題図の軸平行な正方形が領域 `D` からはみ出す。解答の3候補と切り替わり点は手書き・独立計算と一致 |
| 5 | 6 | 解答全2ページ、問題全1ページ確認 | 正四角錐の断面と内接円から `R=πt²(1−t²)/2≤π/8` を検算。手書きと一致し、確定指摘なし |
| 6 | 7 | 解答全4ページ確認 | [#1075](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1075)：平面 `H` の図示が線のみで、切断面の変数と積分の原始関数の符号にも誤り。体積 `π/2` は手書き・独立計算と一致 |

1983年度は第1問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1984年度

手書きPDFは全8ページ。物理1ページが表紙、第1・2問は物理2・3ページ、第3問は物理4〜5ページ、第4〜6問は物理6〜8ページ。原稿と全6問のTeXを照合し、主要な式・結論を独立検算した。生成解答PDFは全2・2・2・2・2・4ページを表示確認。第1・5問の問題PDFも各全1ページを表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ、問題全1ページ確認 | [#1076](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1076)：問題図の円板が原点に接せず、底面積と点から平面までの距離の式に誤記。影の輪郭 `x²+(y−√2)²=2` と体積 `2π(2√2−1)/3` は手書き・独立計算と一致 |
| 2 | 3 | 解答全2ページ確認 | [#1077](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1077)：図の原点が曲線・接点・円の座標系からずれ、極限計算にも余分な `1`。極限 `0,1` は手書き・独立計算と一致 |
| 3 | 4〜5 | 解答全2ページ確認 | [#1078](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1078)：別解の帰納法で和の `+` が欠落し、(2)の十分性の論証が逆向き。主解法は微分値による必要十分性を正しく示す |
| 4 | 6 | 解答全2ページ確認 | 水平切断の内外半径は `q` と `√(q²+p²)`、断面積 `πp²`。積分した体積 `√3π/48` は手書き・独立計算と一致。確定指摘なし |
| 5 | 7 | 解答全2ページ、問題全1ページ確認 | [#1079](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1079)：途中計算の `1/p`、`1/(p−1)` などは `p=0,1` で未定義。最終確率は独立の分岐過程計算と一致 |
| 6 | 8 | 解答全4ページ確認 | `U:y≤−(x−2a)²+2b` として3つの集合条件を独立に確認。最終領域 `0<a<2`, `max{a²,(a−2)²}≤b<2(a−1)²+2` は手書きと一致し、確定指摘なし |

1984年度は全問のWeb実表示が未確認のため、監査完了とはしない。

## 1985年度

手書きPDFは全6ページ。物理1ページは表紙、第1〜3問は物理2〜4ページ、第5・6問は物理5・6ページ。第4問の手書き解答はなく、TeXも未解答のプレースホルダーであるため、既存の解答作成Issue [#456](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/456) に再確認結果を追記してOpenを維持した。第1・2・3・5・6問は手書き原稿とTeXを照合し、主要な式・結論を独立検算した。生成解答PDFは全2・2・3・2・5ページを表示確認。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ確認 | [#1080](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1080)：増減表の関数名が `g` になっており、表と最終答案がPDFで分離。最大値 `π/3`、`a=2√3/3` は手書き・独立計算と一致 |
| 2 | 3 | 解答全2ページ確認 | [#1081](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1081)：垂足 `S` を `Q` と誤記。交点数による場合分けと最終結論は手書き・独立計算と一致 |
| 3 | 4 | 解答全3ページ確認 | [#1082](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1082)：**反射点を求める中点条件と垂直条件の2式が誤り**、図3の注記が重なり、空の解説見出しが残る。体積 `4t⁴/[3(1+t²)²]` は正しい条件と行列式から独立検算し、手書きと一致 |
| 4 | 解答なし | 未解答プレースホルダー | [#456](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/456) をOpenのまま維持。手書きPDFは第3問の次が第5問で、この問の解答はない |
| 5 | 5 | 解答全2ページ確認 | [#1083](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1083)：**有限和の式が誤り、その右辺の極限も次行と矛盾**。最終値 `1` は正しい等比級数計算・手書きと一致 |
| 6 | 6 | 解答全5ページ確認 | 断面積の式を内側三角形・3辺の帯・円弧に分けて再計算し、積分値 `4(10/3+√3)π−4(1+2√3/3)` は手書き・独立計算と一致。確定指摘なし |

1985年度は第4問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1986年度

手書きPDFは全7ページ。第1〜6問は物理2〜7ページの手書き原稿、TeX、生成解答PDF全2・4・4・3・3・5ページを照合し、面積・法線ベクトル・解の極値・確率・円錐の体積を独立検算した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ確認 | [#1085](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1085)：図1のcaptionは最大配置と書くが実際の図は最大でない。`S` と `max_b S` の混同、`c/a` の誤記と図2の横軸不整合、図3の点名重なりも指摘。最大値 `1` と達成条件は手書き・独立計算と一致 |
| 2 | 3 | 解答全4ページ確認 | [#1086](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1086)：積分の途中で `sin²θ` を `cos²θ` と誤記。変換後の原点表記と図4の配置も指摘。最終面積 `5π/3−1` は円の重なり面積から独立計算し、手書きと一致 |
| 3 | 4 | 解答全4ページ確認 | [#1087](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1087)：図1で問題文の `B` を `A` と表示し、長さ `√(17/18)` のベクトルを「単位」と誤記。式参照・見出し・語句も指摘。最終範囲 `0≤|y|≤(1+√17)/6` は独立計算・手書きと一致 |
| 4 | 5 | 解答全3ページ確認 | [#1088](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1088)：大きい解 `z` を未定義の `Z` と混用し、見出しも旧形式。最小値 `(27+3√15)/11`、最大値 `(11+2√19)/3` は領域の端点関数から独立検算し、手書きと一致 |
| 5 | 6 | 解答全3ページ確認 | [#1089](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1089)：**第1問で除外する履歴の組合せ数を `C(n−1,k−1)` と誤り、次行では `C(n−1,k)` として計算**。第2問の終了時の添字も逆。最終確率式は小さい `n,k` の履歴列挙と一致 |
| 6 | 7 | 解答全5ページ確認 | [#1090](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1090)：最初の円錐の高さを `DH` と誤記。傾斜角の適用範囲、式参照、用語、見出しも指摘。楕円の半径と半量条件から得る `m=(2^(2/3)−1)/(2^(2/3)+1)` は手書き・独立計算と一致 |

1986年度は全問のWeb実表示が未確認のため、監査完了とはしない。

## 1987年度

手書きPDFは全9ページ。物理1ページは表紙、第1問は物理2ページに見出しのみで解答がなく、TeXも未対応プレースホルダー。既存の解答作成Issue [#463](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/463) に再確認結果を追記し、Openを維持した。第2〜6問は物理3〜9ページの手書き原稿、TeX、生成解答PDF全2・3・2・2・2ページを照合し、接線条件・接平面・面積・体積・不等式・確率を独立検算した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2（解答は空欄） | 未対応プレースホルダー | [#463](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/463) をOpenのまま維持。手書き原稿・TeXとも解答がない |
| 2 | 3 | 解答全2ページ確認 | [#1091](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1091)：解答見出しが旧形式。接線のパラメータ表示と `(x−t)²(x−1/t²)` の因数分解を独立に確認し、唯一の共有点となる `(a,b)=(3/2,3/4)` は手書きと一致 |
| 3 | 4〜5 | 解答全3ページ確認 | [#1092](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1092)：主解法の見出しと別解内の呼称が旧形式。接平面・面積式から最小値 `3+2√2` を独立検算し、手書きと一致 |
| 4 | 6 | 解答全2ページ確認 | [#1093](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1093)：断面積の式の末尾に余分な改行があり、PDFに空の式番号 `(7)` が出る。見出しも旧形式。体積 `π(t²−1)²/3+2π/3` と最小値 `2π/3` は独立積分・手書きと一致 |
| 5 | 7 | 解答全2ページ確認 | [#1094](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1094)：**帰納法で積の非負性を説明する二つの不等号が逆向き**。手書きは正しい向き。別解の交換法と小さい数列の全列挙で結論は確認済み |
| 6 | 8〜9 | 解答全2ページ確認 | [#1095](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1095)：助詞の重複と旧形式の見出し。`p₃=1/3`, `p₄=11/18`, 極限 `−log 2` は `n=1〜6` の列挙と手書きに一致 |

1987年度は第1問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1988年度（進行中）

手書きPDFは全7ページ。物理1ページは表紙、第1問は物理2ページに見出しのみで解答がなく、TeXも「(解答なし)」のプレースホルダー。既存の解答作成Issue [#466](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/466) に再確認結果を追記し、Openを維持した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全3ページを照合し、射影面積の極値を独立検算した。第3問は物理4ページの手書き原稿、TeX、生成解答PDF全4ページを照合し、3解条件の反例を独立に確認した。第4問は物理5ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、最終条件を独立検算した。第5問は物理6ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、影の円弧長を独立検算した。第6問は物理7ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、体積最大値を独立検算した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2（解答は空欄） | 未解答プレースホルダー | [#466](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/466) をOpenのまま維持。手書き原稿・TeXとも解答がない |
| 2 | 3 | 解答全3ページ確認 | [#1096](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1096)：射影面積を符号付き法線内積で求める箇所に未定義ベクトルと角の説明不足、問題文の誤字もある。最小値 `√2/4`、最大値 `1/2` は独立計算・手書きと一致 |
| 3 | 4 | 解答全4ページ確認 | [#1097](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1097)：**3解条件が実際には1解の点を含む**。`P=(-1/2,1/2)` が反例。手書きの条件式も同じ誤りを含むが、最終斜線図は狭い領域を示す。見出しの旧形式も同Issueに記録 |
| 4 | 5 | 解答全1ページ確認 | [#1098](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1098)：ベクトル和の添字と列ベクトル組版の誤り、「格子点」の不正確な呼称、図1のラベル重なり、旧見出しを指摘。最終条件 `0<s≤1` または `b<s/[a(s−1)]` は独立計算・手書きと一致 |
| 5 | 6 | 解答全2ページ確認 | [#1099](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1099)：角の変数 `θ` を途中で `t` と表記し、参照式番号も誤る。図1 caption と実際の図の内容の不一致、旧見出しも指摘。影の円弧長 `4π` は独立計算・手書きと一致 |
| 6 | 7 | 解答全2ページ確認 | [#1100](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1100)：図1の一般点 `A` が `OA=1` を満たさない。図2の `[cite: 7]` 残存、本文の主語と旧見出しも指摘。最大体積 `9√3` は独立計算・手書きと一致 |

1988年度は第1問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1989年度（進行中）

手書きPDFは全9ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全3ページを照合し、主解法と別解3本を確認した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、面積比の極限を独立検算した。第3問は物理4〜5ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、反復写像の条件を独立検算した。第4問は物理6ページの手書きメモと物理7ページの解法2本、TeX、生成解答PDF全2ページを照合し、答えを整数演算で独立検算した。第5問は物理8ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、円筒殻の導出と積分を独立検算した。第6問は物理9ページの手書き原稿、TeX、生成解答PDF全3ページを照合し、小さいパラメータで全列挙した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全3ページ確認 | [#1101](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1101)：別解の式参照、旧見出し、重複文を指摘。結論 `k>2` は独立計算・手書きと一致 |
| 2 | 3 | 解答全2ページ確認 | [#1102](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1102)：見出しの旧形式を指摘。面積比の極限 `2` は独立計算・手書きと一致 |
| 3 | 4〜5 | 解答全2ページ確認 | [#1103](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1103)：見出しと数式内の句点を指摘。`q=6±2√5` は独立計算・手書きと一致 |
| 4 | 6（メモ）・7（解法2本） | 解答全2ページ確認 | [#1104](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1104)：**非整数への合同式、途中の等式、奇数乗和の因数分解が誤り**。手書きの別解にも奇数乗和をすべて正符号で展開した箇所がある。200桁・末尾9は整数演算で独立検算済み |
| 5 | 8 | 解答全2ページ確認 | [#1105](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1105)：円筒殻の評価区間と微分可能性の説明、図1の `x=1` 欠落、旧見出しを指摘。体積 `π` は独立計算・手書きと一致 |
| 6 | 9 | 解答全3ページ確認 | [#1106](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1106)：別解で境界 `n=2k` を除外、`3n` の誤字、図1の小さい注釈と旧見出しを指摘。確率式は許容37組の全列挙と手書きに一致 |

1989年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 1990年度（進行中）

手書きPDFは全9ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、極限を独立検算した。第2問は物理3〜4ページの手書き原稿、TeX、生成解答PDF全3ページを照合し、三次関数の極値と不等式を独立検算した。第3問は物理5ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、切断面の周長と正方形の寸法を独立検算した。第4問は手書き物理6ページが空欄で、TeXも未解答プレースホルダー。既存の解答作成Issue [#475](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/475) に再確認結果を追記し、Openを維持した。第5問は物理7ページのメモと8ページの解答、TeX、生成解答PDF全3ページを照合し、菱形と円の接線条件を独立検算した。第6問は物理9ページの手書き原稿、TeX、生成解答PDF全3ページを照合し、確率を出目の全列挙で独立検算した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ確認 | [#1107](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1107)：**`a_n→0` は誤答で、正しくは `+∞`**。手書き・独立計算は `+∞`。比の極限 `1/√2` は正しい。図1のラベル重なりと変形式の誤記も指摘 |
| 2 | 3〜4 | 解答全3ページ確認 | [#1108](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1108)：導関数の係数3と極値の符号を誤る。図1のラベル重なりも指摘。`h=4x³−3x` と絶対値不等式の結論は手書き・独立検算と一致 |
| 3 | 5 | 解答全2ページ確認 | [#1109](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1109)：図2と図4で六角形の `t` と `1−t` の割当てが逆。連続した通過の説明不足と旧見出しも指摘。周長3・外接正方形の一辺約0.966は独立検算と一致 |
| 4 | 6（解答は空欄） | 未解答プレースホルダー | [#475](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/475) に手書き・TeXとも空欄であることを追記し、Openを維持 |
| 5 | 7（メモ）・8（解答） | 解答全3ページ確認 | [#1110](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1110)：菱形の中心と内接円の中心が一致する根拠、量化表現、旧見出しを指摘。条件 `1/a²+1/b²=1` は手書きと独立検算に一致 |
| 6 | 9 | 解答全3ページ確認 | [#1111](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1111)：図1の細かな注釈、事象の出目個数の説明、旧見出しを指摘。(1) `8/215`、(2) `11/30≤α≤37/90` は手書きと全列挙に一致 |

1990年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。第4問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1991年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、状態遷移の漸化式を独立検算した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全3ページを照合し、影の面積を独立検算した。第3問は物理4ページの手書き原稿、TeX、生成解答PDF全5ページを照合し、三次方程式の根と `f(p)` の増減・曲率を独立検算した。第4問は物理5ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、多項式の微分恒等式を独立検算した。第5問は物理6ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、格子点から直線までの最小距離を独立検算した。第6問は物理7ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、積分と求めた関数の十分性を独立検算した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全1ページ確認 | [#1112](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1112)：図2の自己ループの表示、本文の主語、旧見出しを指摘。確率 `p_n=(1−(−1/3)^(n−1))/4` は手書きと独立計算に一致 |
| 2 | 3 | 解答全3ページ確認 | [#1113](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1113)：主解法の `t,s`、別解の `d₀` が未定義。図3・4の例示寸法の不整合、図3の目盛りの密集、旧見出しも指摘。面積 `ab{πc²+4(c+1)(3c+1)}` は手書きと独立計算に一致 |
| 3 | 4 | 解答全5ページ確認 | [#1114](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1114)：**`0<p<2` の `f'(p)` の符号が逆で論証が矛盾し、`f''(p)` の係数も誤る**。場合分けの変数、図2の紛らわしい目盛り、旧見出しも指摘。最小値 `−3` とグラフの形は手書き・独立検算に一致 |
| 4 | 5 | 解答全2ページ確認 | [#1115](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1115)：帰納法と別解の式参照先、旧見出しを指摘。`p'_n=nq_{n−1}`, `q'_n=−np_{n−1}` は手書き・独立検算に一致 |
| 5 | 6 | 解答全1ページ確認 | [#1116](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1116)：**距離式の分母から平方根が消え、各直線の最小距離とその最大値を混同**。図1の円半径も不正確。答え `√29/58` は手書き・独立検算に一致 |
| 6 | 7 | 解答全2ページ確認 | [#1117](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1117)：**階差和の総和・公比の式が誤り、極限の正値性も誤る**。図1は条件を満たさない関数で描かれている。最終の `f(x)=64x⁻⁵/15` は手書き・代入検算に一致 |

1991年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 1992年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、最適な `b` と四辺形の面積を独立検算した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、格子点の個数と三角形の面積を独立検算した。第3問は物理4ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、二つの不等式の等号条件を独立検算した。第4問は物理5ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、展開図の曲線と斜線領域を複数の角度で独立検算した。第5問は物理6ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、弧長と接線方向を独立検算した。第6問は物理7ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、期待値を独立検算した。全問のWeb実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ確認 | [#1118](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1118)：**(1) の面積 `S₂` の明示式に係数の誤りがあり、手書き・直接計算と不一致**。`S₁` の等式、面積分割の三角形名、増減表、図のラベル重なりも指摘。最適な `b=(a−1)/log a` と (2) の極限 `1` は正しい |
| 2 | 3 | 解答全2ページ確認 | [#1119](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1119)：**図1が実際には1個しかない内部格子点を5個と誤描画**。方向ベクトルを自然数成分に限定し、一般の三角形を扱えていない。結論の奇数性と面積が8の倍数であることは独立検算と一致 |
| 3 | 4 | 解答全2ページ確認 | [#1120](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1120)：**下界評価で `2` が `1` に変わり、印刷された途中式は `17/3` にしかならない**。球面を「円」と呼ぶ誤記、旧見出しも指摘。二つの不等式と等号条件は手書き・独立計算に一致 |
| 4 | 5 | 解答全2ページ確認 | [#1121](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1121)：判別式の平方根は `|cosθ|` であり、二つの根の符号対応が途中で入れ替わる説明が不足。図2の点ラベルの重なり、図1の凡例の色、旧見出しも指摘。展開図の領域は手書き・独立計算に一致 |
| 5 | 6 | 解答全2ページ確認 | [#1122](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1122)：**導関数の第一項が4倍、弧長の平方完成も誤り、関数値と傾きを混同**。最終の `t²=2(x³/3−1/x+2/3)` と `t=√(17/3)` は手書き・独立計算に一致 |
| 6 | 7 | 解答全2ページ確認 | [#1123](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1123)：確率比の正規化、必要条件の主語、旧見出しを指摘。(1) チョキのみ、(2) `(5/14,3/7,3/14)` は手書き・独立検算に一致 |

1992年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 1993年度（進行中）

手書きPDFは全9ページ。第1問は物理2〜3ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、極限値を独立検算した。第2問は物理4ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、数列の剰余周期を独立検算した。第3問は物理5〜6ページの手書き原稿、TeX、生成解答PDF全6ページを照合し、軌跡の式と接続点を独立検算した。第4問は物理7ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、平方完成と最小値を独立検算した。第5問は物理8ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、各桁の遷移と独立な場合の極限値を検算した。第6問は物理9ページの手書き原稿、TeX、生成解答PDF全4ページを照合し、速度の極値と自己交点を独立検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2〜3 | 解答全2ページ確認 | [#1124](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1124)：**TeXの極限値 `8/3` は誤り。手書き原稿で訂正済みの正しい値は `8`**。対称性による場合の限定、問題文にない `D` の正座標条件、旧見出しも指摘 |
| 2 | 4 | 解答全1ページ確認 | [#1125](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1125)：(1) の帰納法で「同値」を「両方成立」と誤記した2箇所、帰納仮定の説明、旧見出しを指摘。答えの `12` の倍数は手書き・独立計算に一致 |
| 3 | 5〜6 | 解答全6ページ確認 | [#1126](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1126)：**二つの異なる境界との交点計算を連立式に見せる途中式、領域図の曲線・塗りのはみ出し**。領域名と楕円の焦点名、双曲線図のラベル重なり、旧見出しも指摘。最終軌跡の式・接続点は手書き・独立計算に一致 |
| 4 | 7 | 解答全2ページ確認 | [#1127](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1127)：最小化する組の唯一性を平方完成から明示すること、偶奇の記法、旧見出しを指摘。`(p,q)` と最小値の式は手書き・独立計算に一致 |
| 5 | 8 | 解答全1ページ確認 | [#1128](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1128)：**5桁の確率を掛けるには桁間の独立性が必要だが問題文に明記されていない**。図の低コントラスト、旧見出しも指摘。独立な場合の極限値は手書き・独立計算に一致 |
| 6 | 9 | 解答全4ページ確認 | [#1129](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1129)：**速度二乗の導関数が4分の1、自己交点の証明が全時刻を網羅せず、別解の変形式も不成立**。`cos t` の範囲の分数欠落、図のラベル重なり、旧見出しも指摘。最終の速さ・交点・速度ベクトルは手書き・独立計算に一致 |

1993年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示は未確認のため、監査完了とはしない。

## 1994年度（進行中）

手書きPDFは全10ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、主解法と別解の多項式恒等式を独立検算した。第2問は物理3〜4ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、三角関数の値と漸化式を独立検算した。第3問は物理5ページの手書き原稿、TeX、生成解答PDF全3ページを照合し、切断面積と体積を独立検算した。第4問は物理6ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、微分方程式と候補関数を独立検算した。第5問は物理7〜8ページの手書き原稿、TeX、生成解答PDF全2ページを照合し、確率と自然数制約下の最大点を独立検算した。第6問は物理9〜10ページの手書き原稿、TeX、生成解答PDF全5ページ・図全6点を照合し、距離の各場合と領域を独立検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ確認 | [#1130](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1130)：**主解法の $g'$ の正値性を示す恒等式で係数が `1/40` の代わりに `40`**。別解と最終結論は独立検算に一致。旧見出しも指摘 |
| 2 | 3〜4 | 解答全1ページ確認 | [#1131](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1131)：**`a+b` を `5/4` でなく `4/5` と記載し、漸化式への代入行で指数も欠落**。否定記号と旧見出しも指摘。有理性・整数性の結論は正しい |
| 3 | 5 | 解答全3ページ確認 | [#1132](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1132)：置換後の積分上端が `1` でなく `π/2` のまま。旧見出しも指摘。切断面積と体積 `4/45` は手書き・独立計算に一致 |
| 4 | 6 | 解答全2ページ確認 | [#1133](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1133)：**積分後の $g(x)$ から因子 $x$ が消え、$g$ と $f$ を取り違えて最終答案に飛ぶ**。積分の引数、$g$ で割る条件、旧見出しも指摘。最終の $f(x)=1/(1-x)^2$ 自体は正しい |
| 5 | 7〜8 | 解答全2ページ確認 | [#1134](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1134)：**$E$ の定義から係数2が落ち、二変数 $n,m$ を同じ $x$ に置き換えた不成立式**。最小化対象、表caption、旧見出しも指摘。最適点 `(1/6,1/5)` は手書き・独立計算に一致 |
| 6 | 9〜10 | 解答全5ページ・図6点確認 | [#1135](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1135)：**$Q$ の座標の符号誤記と、場合（ウ）の値域を過大に述べる箇所**。対称性の表現、式参照、旧見出しも指摘。最終の領域は手書き・独立計算に一致 |

1994年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示は未確認のため、監査完了とはしない。

## 1995年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、コーシー・シュワルツの不等式と等号条件を独立検算した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全1ページを照合し、二階微分と凸性を独立検算した。第3問は物理4ページの手書き原稿、TeX、生成解答PDF全1ページと図を照合し、漸化式と一般項を独立検算した。第4問は物理5ページの手書き原稿、TeX、生成解答PDF全2ページと図を照合し、偶奇別の最小値と142を独立検算した。第5問は物理6ページの手書き原稿、TeX、生成解答PDF全1ページと図を照合し、移動距離と確率を独立検算した。第6問は物理7ページの手書き原稿、TeX、生成解答PDF全2ページと図を照合し、三角形の面積と最小値を独立検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全1ページ確認 | [#1136](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1136)：L4の旧見出しを指摘。最小値 $\sqrt{3/2}$ と等号条件 $x=y/4$ は手書き・独立計算に一致 |
| 2 | 3 | 解答全1ページ確認 | [#1137](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1137)：**微分の中間式 `-tf(t)` と二階導関数 `f(t)` に自由変数が残る**。旧見出しも指摘。手書きの微分式と最終不等式は正しい |
| 3 | 4 | 解答全1ページ・図確認 | [#1138](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1138)：図の段間が狭く、下段の寸法ラベルが上段の図に入り込む。旧見出しも指摘。漸化式と一般項は正しい |
| 4 | 5 | 解答全2ページ・図確認 | [#1139](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1139)：極小点の注釈が候補点・曲線に重なる。式参照と旧見出しも指摘。偶奇別の最小値と142は正しい |
| 5 | 6 | 解答全1ページ・図確認 | [#1140](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1140)：**最終回に初めて南北移動する場合が証明から漏れ、範囲に未定義の文字もある**。旧見出しも指摘。最終確率は正しい |
| 6 | 7 | 解答全2ページ・図確認 | [#1141](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1141)：接線と漸近線のラベルが図の右上で重なる。旧見出しも指摘。面積 $S=ab$ と最小値は正しい |

1995年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示は未確認のため、監査完了とはしない。

## 1996年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページに見出しのみで解答がなく、TeXも「（解答なし）」のプレースホルダーである。既存の解答作成Issue [#492](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/492) に再確認結果を追記してOpenを維持した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全2ページ・図2点を照合し、仮定からの係数条件と根の位置を独立検算した。第3問は物理4ページの手書き原稿、TeX、生成解答PDF全4ページ・図7点を照合し、可視性を内積条件で独立検算した。第4問は物理5ページの手書き原稿、TeX、生成解答PDF全1ページと図を照合し、期待値の極限を独立検算した。第5問は物理6ページの手書き原稿、TeX、生成解答PDF全2ページ・図2点を照合し、体積保存式を独立検算した。第6問は物理7ページの手書き原稿、TeX、生成解答PDF全3ページ・図2点・表3点を照合し、領域と面積を独立検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2（見出しのみ） | 未解答 | [#492](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/492)：手書き・TeXとも解答がなく、解答作成待ち。Open維持 |
| 2 | 3 | 解答全2ページ・図2点確認 | [#1142](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1142)：**端点評価の連鎖不等式で `0>0` としている**。旧見出しも指摘。結論自体は正しい |
| 3 | 4 | 解答全4ページ・図7点確認 | [#1143](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1143)：**(2) の十分性の証明が飛躍し、図7の「見える」線分は球の内部を通る**。図1・5のラベル重なりと旧見出しも指摘。条件値は独立検算に一致 |
| 4 | 5 | 解答全1ページ・図確認 | [#1144](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1144)：**確率和の指数が添字 $l$ ではなく $n-1$ になっている**。場合分けの不等号と旧見出しも指摘。極限1、1/4は正しい |
| 5 | 6 | 解答全2ページ・図2点確認 | [#1145](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1145)：**候補関数が元の水面上昇を再現する十分性の確認がない**。座標・時刻・旧見出しも指摘。候補関数は正しい |
| 6 | 7 | 解答全3ページ・図2点・表3点確認 | [#1146](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1146)：**停留点の符号が逆の代入式と、別の関数 $f$ にすり替わる導関数・増減表**。場合分けの境界、図のラベル重なり、旧見出しも指摘。最終領域・最大面積は正しい |

1996年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。第1問の解答自体が未作成であり、全問のWeb実表示も未確認のため、監査完了とはしない。

## 1997年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全2ページ・図3点を照合し、正三角形の頂点、許容領域、面積の最大値を独立検算した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全3ページ・増減表・図を照合し、整数上の不等式を独立検算した。第3問は物理4ページの手書き原稿、TeX、生成解答PDF全2ページ・図2点を照合し、楕円の成立条件と極限を独立検算した。第4問は物理5ページの手書き原稿、TeX、生成解答PDF全2ページ・図3点を照合し、三角格子の頂点対応と反射回数を独立検算した。第5問は物理6ページの手書き原稿、TeX、生成解答PDF全3ページ・図3点を照合し、回転体積を二通りに独立検算した。第6問は物理7ページの手書き原稿、TeX、生成解答PDF全3ページ・図2点を照合し、共通接線の判別式と面積を独立検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ・図3点確認 | [#1147](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1147)：**図1の三角形が正方形外に出ており、重複した図3の $b$ 軸が斜めで開境界も実線**。頂点だけを最大値候補にする根拠と旧見出しも指摘。最終答案は正しい |
| 2 | 3 | 解答全3ページ・図・表確認 | [#1148](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1148)：**主解法の導関数で分母の二乗が落ち、増減表と符号が矛盾**。別解の重解の場合、負の $a$ の除外、図の線種・ラベル、旧見出しも指摘。最終範囲は正しい |
| 3 | 4 | 解答全2ページ・図2点確認 | [#1149](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1149)：**等式で定まる楕円の内部まで塗り、具体値に対する中心もずれる**。ラベル重なり、極限計算の説明、旧見出しも指摘。範囲と極限値は正しい |
| 4 | 5 | 解答全2ページ・図3点確認 | [#1150](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1150)：**図3の反射点の多くが三角格子の辺から外れる**。図の具体例と一般式の混同、コメントの頂点ラベル不一致、旧見出しも指摘。到達頂点と反射回数 `12k+3` は手書き・独立計算に一致 |
| 5 | 6 | 解答全3ページ・図3点確認 | [#1151](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1151)：**主解法の四分円の積分で係数2が抜け、示した値から結論が出ない**。図1・2のラベル重なりも指摘。最終体積は別解・独立計算に一致 |
| 6 | 7 | 解答全3ページ・図2点確認 | [#1152](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1152)：**非零解でない四次式の「2解」と記し、接点順序に必要な解の和を省く**。図1・2のラベル重なり、旧見出しも指摘。最終範囲・面積は手書き・独立計算に一致 |

1997年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 1998年度

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、TeX、生成解答PDF全2ページ・図と増減表を照合し、極大値と極小値の差を独立検算した。第2問は物理3ページの手書き原稿、TeX、生成解答PDF全3ページ・図2点を照合し、断面の格子点と極限値を独立検算した。第3問は物理4ページの手書き原稿、TeX、生成解答PDF全3ページ・2パネルの図を照合し、接円の半径と漸化式・極限を独立検算した。第4問は物理5ページの手書き原稿、問題文TeX、解答TeX、生成解答PDF全3ページ・図3点を照合し、整数値の個数を直接計数した。第5問は物理6ページの手書き原稿、TeX、生成解答PDF全4ページ・図2点を照合し、射影漸化式と境界角の極限を独立検算した。第6問は物理7ページの手書き原稿、TeX、生成解答PDF全4ページ・図4点を照合し、断面積積分を独立検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ・図と表確認 | [#1153](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1153)：旧見出しのみ。$a=\pm1$ は手書き・独立計算に一致 |
| 2 | 3 | 解答全3ページ・図2点確認 | [#1154](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1154)：**図2で非整数座標の点を格子点として描く**。退化する端点と旧見出しも指摘。極限 $8/3$ は手書き・直接計数・独立計算に一致 |
| 3 | 4 | 解答全3ページ・2パネル図確認 | [#1155](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1155)：**$q_n$ の定義が問題文と異なり、反復評価の厳密不等号は $n=1$ で偽**。極限式の対象欠落、図の値コメント・ラベル、旧見出しも指摘。正しい定義での結論は手書き・独立計算に一致 |
| 4 | 5 | 解答全3ページ・図3点確認 | [#1156](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1156)：**解答で関数の分母が問題文の3分の1になり、差分・判別式も不成立**。区間端点と図3の表記も指摘。最終個数 $26n+1$ は手書き・直接列挙に一致 |
| 5 | 6 | 解答全4ページ・図2点確認 | [#1157](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1157)：**成分式の参照がPDFで `??` となり、$x_{n+1}$ の係数変形も誤る**。条件の書式、図の代表点、末尾の孤立ページ、旧見出しも指摘。最終の収束範囲・極限は独立計算に一致 |
| 6 | 7 | 解答全4ページ・図4点確認 | [#1158](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1158)：対称領域の説明の不等号が逆、図3のcaptionが「および」で始まり、図2の目盛りが重なる。旧見出しも指摘。体積 $4(\sqrt2+1)-3\pi$ は手書き・独立計算に一致 |

1998年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 1999年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題文、TeX、生成解答PDF全2ページ・図2点を照合した。加法定理の両解法を独立に検算した。第2問は物理3ページの手書き原稿、問題文、TeX、生成解答PDF全2ページを照合し、一般項・不等式・極限を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、生成解答PDF全2ページ・図3点・表1点を照合し、64通りの導通状態を独立に列挙した。第4問は物理5ページの手書き原稿、問題・解答TeX、生成解答PDF全3ページ・図3点を照合し、円板の半径和を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、生成解答PDF全1ページを照合し、二項係数の2進評価と $m\le64$ の直接列挙を行った。第6問は物理7ページの手書き原稿、問題・解答TeX、生成解答PDF全1ページ・図1点を照合し、積分と下界を独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ・図2点確認 | [#1159](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1159)：**回転基底 $\vec q$ の角度が説明と成分表示で矛盾する**。旧見出しと数式中の丸数字も指摘。正しい回転角での加法定理は手書き・独立計算に一致 |
| 2 | 3 | 解答全2ページ確認 | [#778](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/778)を行番号付きで全面更新：**一般項の指数が手書きの $n$ から $n-1$ に変わり、そこから導く絶対値評価と後続の上下界が矛盾**。因数分解・変数定義・初期条件の表示も指摘。不等式と極限 $1/\log5$ 自体は正しい一般項から独立に確認 |
| 3 | 4 | 解答全2ページ・図3点・表1点確認 | [#1160](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1160)：図1の点名と端子ラベルが重なり、captionが問題にない「正四面体」を指定。旧見出しも指摘。両問の確率は手書き・全64状態の列挙に一致 |
| 4 | 5 | 解答全3ページ・図3点確認 | [#1161](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1161)：**円板Bの余弦定理の1行目が不成立で、図1の円板Bは共有点Pを通らない**。図の「球面」表記と旧見出しも指摘。最大値 $9/8$ は実現例・独立計算に一致 |
| 5 | 6 | 解答全1ページ確認 | [#1162](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1162)：**$k\ge3$ の場合だけを証明し、$k=1,2$ で $t>1$ の奇数を除外できない**。手書き原稿は $t\ge3$ と記す。最終形 $m=2^k-1$ は直接列挙・独立計算に一致 |
| 6 | 7 | 解答全1ページ・図1点確認 | [#1163](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1163)：接点で成り立たない厳密な接線不等式と、図のラベル重なりを指摘。積分値 $2(e^\pi-1)/5>8$ は手書き・独立計算に一致 |

1999年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2000年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、生成解答PDF全2ページ・図2点・増減表を照合し、接線条件と面積を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、生成解答PDF全3ページ・図2点を照合し、円周上の2点と垂線の足の複素数計算を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、生成解答PDF全3ページ・図1点・表2点を照合し、逆数漸化式と極限関数の微分を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、生成解答PDF全4ページ・図5点・表2点を照合し、各周期の衝突区間と重複を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、生成解答PDF全2ページ・図1点を照合し、1〜4桁の候補を全列挙した。第6問の手書き原稿は物理7ページが空欄で、TeXも解答未作成であることを確認した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ・図2点・増減表確認 | [#1164](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1164)：**面積の導関数に係数 $1/2$ が抜け、図1の頂点と目盛りが重なる**。最大面積 $\sqrt3\pi/9$ は独立計算に一致 |
| 2 | 3 | 解答全3ページ・図2点確認 | [#1165](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1165)：**円周上から $w=\alpha\beta$ を導く最終式の符号が逆で、図2の $OR$ が $PQ$ に直交しない**。$w\ne0$ の無根拠な断定と図1のラベル重なりも指摘。命題は独立計算で確認 |
| 3 | 4 | 解答全3ページ・図1点・表2点確認 | [#1166](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1166)：**逆数の導入前に必要な $q_k\ne0$ の背理法で仮定が逆**。表captionと図の $y=1$ 表示も指摘。極限関数と3曲線は独立計算に一致 |
| 4 | 5 | 解答全4ページ・図5点・表2点確認 | [#1167](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1167)：**非衝突の2条件が連立に見え、周期区間の重複から「一度だけ」を排除する論証が不足**。表の関数値、上端の誤記、図のラベル重なりも指摘。最終の2区間は独立計算に一致 |
| 5 | 6 | 解答全2ページ・図1点確認 | [#1168](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1168)：**構成図で例示の数字が塗りつぶされ、3つの手順見出しと線が重なる**。未定義の `S_{2000}`、区間上端の不等号、旧見出しも指摘。4桁1728個・2000番目8695は直接列挙に一致 |
| 6 | 7 | 手書き・TeXとも解答空欄 | 解答作成Issue [#770](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/770)をopen維持。数学・PDF監査は解答作成後に実施 |

2000年度は第1〜5問の手書き・TeX・生成PDF照合を終えた。第6問は解答作成待ち、全問のWeb実表示は未確認。2001年度以降の進捗は以下に記録する。

## 2001年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、生成解答PDF全2ページ・図3点を照合し、座標による外接球の中心・半径を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeXを照合し、現行TeXを隔離ディレクトリで再ビルドしたPDF全2ページを確認した。積分作用素を2次元の係数方程式に還元して必要十分条件を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図1点・増減表1点を照合し、面積と微分の符号を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図1点を照合し、初項・円の中心と半径・漸化式の不変式を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図3点を照合し、同量時の分岐を含む小さい有理数例132組を全探索した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・状態図1点を照合し、コインの出方を $n=1,\ldots,8$ まで全列挙した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 解答全2ページ・図3点確認 | [#1169](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1169)：**$|AR|$ の代入で $\sqrt3/2$ が $3/2$ に変わり、次行への等号が不成立**。切断面の説明、誤参照、図の記号衝突・ラベル重なりも指摘。最終半径 $\sqrt{13}/3$ は座標計算と手書きに一致 |
| 2 | 3 | 現行TeXから再ビルドした解答全2ページ確認 | [#1170](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1170)：**別解が解なしの場合を一意解と誤判定**。未定義の $k,A$、係数 $-2$ と $-4$ の混同、積分式の改行漏れも指摘。最終条件 $(b-2)^2\ne a^2$ と関数は独立計算に一致 |
| 3 | 4 | 再ビルドした解答全2ページ・図1点・増減表1点確認 | [#1171](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1171)：**図の $Q$ 座標と双曲線の式が重なり、$a(t)$ のラベルが一部分の面積を指すように見える**。増減表の極限表記・列指定と旧見出しも指摘。単調減少の結論は独立微分に一致 |
| 4 | 5 | 再ビルドした解答全2ページ・図1点確認 | [#1172](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1172)：**$b_n$ の定義が自己参照式になり、$b_1=1$ と誤記**。半径式の途中表示、逆数の正当化、図にない垂直二等分線への言及も指摘。中心 $1/2$ と半径 $\sqrt5/2$ は手書き・独立計算に一致 |
| 5 | 6 | 再ビルドした解答全2ページ・図3点確認 | [#1173](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1173)：**(2)の主証明で $3x>3/5$ を $S=1$ との矛盾とし、別解で $X$ 以外の総水量を $1-2x$ と取り違える**。合流時点の説明、存在しない $a_5$、誤参照、図のラベルも指摘。結論は手書きと、同量時分岐を含む132組の直接列挙に一致 |
| 6 | 7 | 再ビルドした解答全2ページ・状態図1点確認 | [#1174](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1174)：**$P_n,Q_n,X_n$ の事象が冒頭の定義と図・後続の証明で入れ替わる**。(3)の確率で $P$ と $Q$ の対応も逆。最終の同位置個数と平均は全出方の列挙に一致 |

2001年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2002年度（進行中）

手書きPDFは全8ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全1ページ・図1点を照合し、交点の二次方程式と境界値を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全1ページを照合し、余りの漸化式と最大公約数の不変性を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図2点を照合し、交円平面、距離条件、領域と体積を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図2点・表1点を照合し、直交条件と解の存在範囲を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・立体図2点を照合し、三角錐の面積・体積・極限値を独立に検算した。第6問は物理7ページの検討メモと物理8ページの完成稿、問題・解答TeX、再ビルドしたPDF全1ページを照合し、シャッフルの遷移と復元を独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全1ページ・図1点確認 | [#1175](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1175)：**図で左端と零点のラベル、区間表示が重なる**。開閉端点が同じ矢印に見えること、関数名と旧見出しの表記も指摘。最終の角度範囲は手書き・独立計算に一致 |
| 2 | 3 | 再ビルドした解答全1ページ確認 | [#1176](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1176)：**互いに素の同値が数式記号でなく斜体の `iff` と表示される**。余り比較の根拠と旧見出しも指摘。漸化式と結論は最大公約数の計算に一致 |
| 3 | 4 | 再ビルドした解答全2ページ・図2点確認 | [#1177](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1177)：**球の外部条件が $f(P)>0$ となり、交円平面の導出で球面方程式の定数項が抜ける**。3D図の平面パッチの2頂点も平面から外れ、切断図の半径矢印は外円に届かない。領域と体積 $19\pi/6<10$ は独立計算に一致 |
| 4 | 5 | 再ビルドした解答全2ページ・図2点・表1点確認 | [#1178](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1178)：**$g$ と $f$ を取り違え、除外点を「最小値」と表示**。図1のラベル重なりと旧見出しも指摘。結論 $a>1/2$ は手書き・独立計算に一致 |
| 5 | 6 | 再ビルドした解答全2ページ・立体図2点確認 | [#1179](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1179)：**$q_k>0$ は $k=0,n$ で偽**。図の点名・軸・注記の重なりと旧見出しも指摘。極限値 $\sqrt2\pi/48$ は手書き・独立計算に一致 |
| 6 | 7〜8 | 再ビルドした解答全1ページ確認 | [#1180](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1180)：シャッフル回数の添字 $t$ を $k$ と誤記。旧見出しも指摘。3回後の逆順と $2n$ 回後の復元は手書き・独立列挙に一致 |

2002年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2003年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全3ページ・図2点・増減表1点を照合し、許容される係数の範囲と積分の下界を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図2点を照合し、複素数の比、動点の軌跡と距離の最大位置を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全4ページ・図4点を照合し、断面積を直接積分して最終式と体積を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全1ページを照合し、漸化式の下1桁と整数部分を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・ベン図1点を照合し、確率式を全出目の列挙で独立に検算した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図4点を照合し、主解法と3別解の下界を独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全3ページ・図2点・増減表1点確認 | [#1181](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1181)：**別解で $a=3$ を誤って不成立とし、$h$ の端点値を $f$ のものと誤記**。主解法の参照先、図のラベル、旧見出しも指摘。主解法の値域 $I\ge4(11-4\sqrt3)/3$ は手書き・独立計算に一致 |
| 2 | 3 | 再ビルドした解答全3ページ・図2点確認 | [#1182](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1182)：**$|p|^2$ の係数196が脱落し、後続の等式も不成立**。円の特定の根拠不足、記号定義、旧見出しも指摘。$\angle APB=\pi/4$ と最大位置 $t=28$ は手書き・独立計算に一致 |
| 3 | 4 | 再ビルドした解答全4ページ・図4点確認 | [#1183](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1183)：**円錐の半径が半分、断面積の三角形面積・符号が途中で誤り、正しい最終式まで等号がつながらない**。体積積分の係数と図の角度表示も指摘。最終断面積・体積 $\pi-16/9$ は手書き・独立計算に一致 |
| 4 | 5 | 再ビルドした解答全1ページ確認 | [#1184](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1184)：問題文の $s_n$ を解答で $S_n$ と表記。周期の根拠と旧見出しも指摘。$\lfloor\beta^3\rfloor=-1$ と最終の1の位6は独立計算に一致 |
| 5 | 6 | 再ビルドした解答全2ページ・ベン図1点確認 | [#1185](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1185)：**ベン図の交差領域と外側の注記が読みにくい**。旧見出しも指摘。確率式・極限 $\log(5/6)$ は全出目の列挙と手書きに一致 |
| 6 | 7 | 再ビルドした解答全2ページ・図4点確認 | 指摘なし。主解法の $\pi^2>36(2-\sqrt3)>(3.05)^2$、別解1の折れ線による下界 $3.0955\ldots$、別解2の台形による下界 $3.1143\ldots$、別解3の余弦不等式による下界 $3.1058\ldots$ を独立計算で確認。図4の近接目盛りは拡大表示して判読可能と判断 |

2003年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2004年度（進行中）

手書きPDFは全8ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全2ページ・図1点を照合し、正三角形の辺長を座標で独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・表1点を照合し、平方数の下2桁と法10000での不可能性を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全4ページ・図3点・増減表1点を照合し、内サイクロイドの軌跡と面積を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図3点・増減表1点を照合し、解の個数と図に表示した交点を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図3点・増減表1点を照合し、球冠体積と方程式の根を独立に検算した。第6問は物理7〜8ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図2点を照合し、確率式を全操作列の列挙で独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全2ページ・図1点確認 | [#1186](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1186)：**別解で $a=\sqrt3p$ として絶対値が落ち、負の $p$ では等式不成立**。余分な括弧、空の式番号、旧見出しも指摘。最終値 $18/5$ は手書き・独立計算に一致 |
| 2 | 3 | 再ビルドした解答全2ページ・表1点確認 | [#1187](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1187)：**合同式の法100・10000が `(mod 1)00`・`(mod 1)0000` と分断表示**。代入先の誤参照、平方数の説明、旧見出しも指摘。命題は全剰余類の列挙に一致 |
| 3 | 4 | 再ビルドした解答全4ページ・図3点・増減表1点確認 | [#1188](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1188)：**面積 $T$ の係数が $25/7$ から $25/14$ になり、後の代入と矛盾**。三角形の点名、図の注記重なり、旧見出しも指摘。正しい $T$ と最終結果 $S_1=108\pi/5$, $S_2=392\pi/5$ は手書き・独立数値積分に一致 |
| 4 | 5 | 再ビルドした解答全3ページ・図3点・増減表1点確認 | [#1189](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1189)：**9個の解として図示した点が $f_1(x)=\alpha_i$ を満たさない**。数値例の根のずれと旧見出しも指摘。本文の解数 $1,5,9$ と帰納法による $3^n$ は手書き・独立検算に一致 |
| 5 | 6 | 再ビルドした解答全3ページ・図3点・増減表1点確認 | [#1190](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1190)：**$8/3.14<2.54$ は偽**。この誤った上界は手書きにもあり、TeX では不等号 `<=` がそのまま表示される。接触条件、定義域外の $V(0)$、旧見出しも指摘。正しい体積式と根 $r\approx1.48733$（四捨五入で1.5）は独立計算に一致 |
| 6 | 7〜8 | 再ビルドした解答全3ページ・図2点確認 | [#1191](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1191)：**数式の後に不要な `[O]` が表示され、遷移図は一部の矢印と確率表示が欠ける**。未定義の $d_0$ と旧見出しも指摘。主解法・別解の確率式は $n=0,\ldots,8$ の全操作列挙に一致 |

2004年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2005年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全2ページを照合し、高階微分と係数の一般項を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図2点を照合し、複素数の最大値を主解法・別解から独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図2点・増減表1点を照合し、導関数と反復列の収束を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全1ページを照合し、合同式の全剰余類を独立に列挙した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全1ページ・図1点を照合し、勝率を全カード列の列挙で独立に検算した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図2点を照合し、断面積と最終体積を独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全2ページ確認 | [#1192](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1192)：**第$n$次導関数を関数の$n$乗を表す $f^n(x)$ と誤表記**。旧見出しも指摘。漸化式と一般項 $a_n=(-1)^{n+1}n!h_n$, $b_n=(-1)^n n!$ は手書き・独立計算に一致 |
| 2 | 3 | 再ビルドした解答全2ページ・図2点確認 | [#1193](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1193)：**主解法の $|w|^2$ 恒等式と境界上の最大値計算が不成立**。手書きにも主要な式の誤りがある。別解は $|z_1z_2|\le25/16$ の等号を達成し、最終結論 $w=-25/16$ は正しい |
| 3 | 4 | 再ビルドした解答全2ページ・図2点・増減表1点確認 | [#1194](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1194)：**収束評価の厳密不等号が $n=0$ で不成立**。図2点の $y=1$ と $(1+e)/4$ のラベル重なりも指摘。$0\le f'(x)<1/2$ と $x_n\to1$ は手書き・独立検算に一致 |
| 4 | 5 | 再ビルドした解答全1ページ確認 | [#1195](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1195)：**$5^4\mid(a-1)$ の場合を除外せずに $5^4\mid a$ としている**。手書きにもこの論証の欠落がある。範囲内の唯一の解 $a=625$ は全剰余類の列挙に一致 |
| 5 | 6 | 再ビルドした解答全1ページ・図1点確認 | [#1196](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1196)：**$d\le k-c$ と $d>N-c$ の二者択一をコンマで並べている**。図の注記重なりと $a=N$ の場合の説明も指摘。勝率式は $N=1,\ldots,7$ の全カード列挙に一致 |
| 6 | 7 | 再ビルドした解答全3ページ・図2点確認 | [#1197](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1197)：**断面の $y,z$ の大小関係が文章と式で逆**。3D図の境界ラベル重なりも指摘。最終体積 $8(\sqrt2-4/3)r^3$ は独立断面積積分に一致 |

2005年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2006年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全2ページ・図2点を照合し、双曲線の判別式と単位円の長さの条件を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全1ページ・図1点を照合し、表示列の全列挙で確率式を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図1点を照合し、反射像を座標から独立に求め、存在条件を検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページを照合し、低い $y$ の全場合と無限列の漸化式を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図1点・増減表1点を照合し、数列の上界と極限を独立に検算した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図2点・増減表1点を照合し、逆関数の積分を数値積分で独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全2ページ・図2点確認 | [#1198](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1198)：**単位円の条件を3乗と誤記**。後出の式への誤参照、図1のラベル重なりも指摘。結論は手書き・独立計算に一致 |
| 2 | 3 | 再ビルドした解答全1ページ・図1点確認 | [#1199](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1199)：**問題文の $P_n$ を解答・図で $p_n$ と表記**。確率式と最終結果は全表示列の列挙に一致 |
| 3 | 4 | 再ビルドした解答全2ページ・図1点確認 | [#1200](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1200)：**図の $R$ が第2象限にあり題意と矛盾**。未定義の $t$、符号の誤推論、存在条件の確認漏れも指摘。最終値 $p=2$ は反射像の独立構成に一致 |
| 4 | 5 | 再ビルドした解答全2ページ確認 | [#1201](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1201)：**$y=3$ の場合分けで $x$ を $z$ と誤記**。場合番号と条件の参照先も指摘。解2組と無限列の構成は手書き・独立計算に一致 |
| 5 | 6 | 再ビルドした解答全3ページ・図1点・増減表1点確認 | [#1202](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1202)：**別解の厳密不等号が $n=1$ で不成立**。面積比較図の幅・面積・目盛りの不整合も指摘。極限 $0,1/2$ は手書き・独立計算に一致 |
| 6 | 7 | 再ビルドした解答全3ページ・図2点・増減表1点確認 | [#1203](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1203)：**微分途中式で $t^3$ を $t^2$ と誤記**。図2のラベル重なりも指摘。手書きの最終値は $+12$ だが TeX の $-12$ が正しい。数値積分と一致 |

2006年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2007年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全1ページを照合し、二項展開と係数の帰納法を独立に検証した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図2点を照合し、正弦定理・余弦定理・極限を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図2点を照合し、領域の上下界と端点を独立に検算した。第4問は物理5ページの手書き原稿が空白で、解答TeXと再ビルドしたPDF全1ページも「解答なし」となっていることを確認した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図3点を照合し、全コイン列の列挙で確率式を独立に検算した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図3点を照合し、面積評価の上下界を独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全1ページ確認 | [#1204](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1204)：**二項係数が脱落し、帰納法の係数式が不成立**。高次係数への過剰な整数仮定、数式の連結、帰納法の開始範囲も指摘。結論は正しい係数漸化式で独立に証明可能 |
| 2 | 3 | 再ビルドした解答全2ページ・図2点確認 | [#1205](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1205)：**最終式の等号欠落で答えが等式になっていない**。未展開の `sqrt`、余弦定理の点の添字、図2点の長さの不整合も指摘。極限 $(e-1)\sqrt{\pi^2+1}$ は手書き・独立計算に一致 |
| 3 | 4 | 再ビルドした解答全2ページ・図2点確認 | [#1206](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1206)：**図2の $a=\pm1/3$ の境界接続点を $b=1/3$ に誤配置**。補助線と解説の誤記も指摘。区分的な上下界と領域輪郭は独立検算に一致 |
| 4 | 5 | 再ビルドした解答全1ページの「解答なし」を確認 | 手書き原稿も空白。行列問題の新規解答作成は既存の [#771](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/771) で管理中。証明全体の監査は解答作成後に必要 |
| 5 | 6 | 再ビルドした解答全2ページ・図3点確認 | [#1207](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1207)：**$q_m$ の確率和で指数を $m$ に固定し、等号が不成立**。最後の裏の回数と図2の適用範囲も指摘。最終確率式は全コイン列の列挙に一致 |
| 6 | 7 | 再ビルドした解答全3ページ・図3点確認 | [#1208](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1208)：**別解の上界 $15/64$ と $1/2$ が実際の $\log2$ より小さく、論証が破綻**。比の誤設定と図3点の曲線式・ラベルの不整合も指摘。主解法の $24/35<\log2<17/24$ は正しい |

2007年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。ただし第4問は原稿・解答TeXとも空白であり、解答作成の [#771](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/771) が未完了。全問のWeb実表示も未確認のため、監査完了とはしない。

## 2008年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全3ページ・図3点を照合し、漸化式と共通領域の境界条件を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・状態遷移図2点を照合し、吸収までの確率を厳密な分数で独立に列挙した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全4ページ・図6点を照合し、断面半径と体積積分を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図2点・増減表2点を照合し、最小値を別法で検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全1ページを照合し、3進付値を独立に検算した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・増減表1点・曲線図1点を照合し、面積積分を独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全3ページ・図3点確認 | [#1209](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1209)：**傾きの比の式と不等号が誤り、共通領域の左側境界を誤って包含**。切片の単調性と添字の誤記も指摘。左境界は除外、右境界は包含、頂点は除外されることを独立に確認。左境界の誤包含は手書きにもある |
| 2 | 3 | 再ビルドした解答全2ページ・状態遷移図2点確認 | [#1210](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1210)：**最終場合分けが「偶数かつ1」と読め、$n=1$ の値を定義できない**。未定義の $A_k$ と式の重複も指摘。確率の結論は独立列挙に一致 |
| 3 | 4 | 再ビルドした解答全4ページ・図6点確認 | [#1211](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1211)：**断面半径の三平方の途中式が不成立**。垂直二等分面の誤同定、図1の形状、図4の垂線、別解の点名、図2のラベル重なりも指摘。最終体積 $5\sqrt6\pi/54$ は独立計算に一致 |
| 4 | 5 | 再ビルドした解答全3ページ・図2点・増減表2点確認 | [#1212](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1212)：**導関数と増減表で係数 $1/4$ が脱落**。図の定義域と配置も指摘。最小値は独立検算に一致 |
| 5 | 6 | 再ビルドした解答全1ページ確認 | [#1213](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1213)：**必要性の見出しが $Q\Rightarrow Q$ になり、$k=0$ も表現から漏れる**。未定義の $A$、反復数字の表記揺れ、重複語も指摘。3進付値の結論は独立検算に一致 |
| 6 | 7 | 再ビルドした解答全2ページ・増減表1点・曲線図1点確認 | [#1214](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1214)：**面積式に未定義の $y'OB_+$ が混入**。交点検証時の式参照と三角関数の注記も指摘。面積 $32/9$ は独立積分に一致 |

2008年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2009年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全1ページを照合し、二項係数の最大公約数と帰納法を独立に検算した。第2問は手書き原稿に「解答なし」のみ記され、解答TeXと再ビルドしたPDF全1ページも同じ状態であることを確認した。手書きPDFには第2問専用のページはない。第3問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図3点を照合し、多項係数から確率を独立に検算した。第4問は物理4ページの手書き原稿と物理5ページの検討メモ、問題・解答TeX、再ビルドしたPDF全4ページ・図4点を照合し、断面積と体積極限を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全1ページを照合し、関数の符号と小数の大小を独立に検算した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全6ページ・図6点を照合し、角度制約から時刻 $T$ の距離評価まで独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全1ページ確認 | [#1215](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1215)：**$k=1$ の帰納法開始に $a_m(0)$ を用いている**。偶数条件の記法も指摘。最終結論は独立検算に一致 |
| 2 | 専用ページなし（文字起こし原稿に「解答なし」） | 再ビルドした解答全1ページの「解答なし」を確認 | 行列問題の解答新規作成は既存の [#772](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/772) で管理中。証明全体の監査は解答作成後に必要 |
| 3 | 3 | 再ビルドした解答全2ページ・図3点確認 | [#1216](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1216)：**問題の白玉を図1・2で緑玉として描いている**。図3の「計8個確定」という表現も指摘。確率 $P_3/P_1=63/16$ は独立列挙に一致 |
| 4 | 4–5（5は検討メモ） | 再ビルドした解答全4ページ・図4点確認 | [#1217](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1217)：**体積積分・三角恒等式・上界評価の途中式に誤り**。図4の領域ラベル位置と積分上端の `pi` も指摘。$W(a)=2\pi/3$ と $\lim V(a)=2\pi/3$ は独立検算に一致 |
| 5 | 6 | 再ビルドした解答全1ページ確認 | [#1218](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1218)：**証明した符号条件でなく関数の定義式を2回誤参照**。重複した接続語も指摘。不等式の結論は独立検算に一致 |
| 6 | 7 | 再ビルドした解答全6ページ・図6点確認 | [#1219](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1219)：**和積公式の符号と分母係数が誤り、途中式が不成立**。角度の下界、時刻変数、第1図のベクトルの向きと移動距離、図6のラベル重なりも指摘。結論は独立検算に一致 |

2009年度は第1・3〜6問の手書き・TeX・生成PDF照合を終えた。第2問の解答は未作成で [#772](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/772) が開いている。全問のWeb実表示も未確認のため、監査完了とはしない。

## 2010年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全3ページ・図3点・増減表1点を照合し、体積の値域を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図3点を照合し、不等式の上界と下界を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図2点を照合し、遷移確率を有理数で独立列挙した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図4点を照合し、領域の面積を別法で独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図1点を照合し、条件を整数で独立列挙した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全5ページ・図7点を照合し、断面積を独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全3ページ・図3点・増減表1点確認 | [#1220](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1220)：**下界係数が誤り、表示された不等式が矛盾**。表の変数名、値域の十分性、図1のラベル重なりも指摘。結論 $0<V<\pi/27$ は独立検算に一致。下界係数の誤りは手書きにもある |
| 2 | 3 | 再ビルドした解答全3ページ・図3点確認 | [#1221](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1221)：**和の上界の添字が誤り、途中式が不成立**。図1・2の数値とラベルの不一致も指摘。不等式の最終結論は独立検算に一致。上界添字の誤りはTeX化時に発生 |
| 3 | 4 | 再ビルドした解答全3ページ・図2点確認 | 追加 Issue なし。遷移式と $P_{2n}(10)=\{1−4^{-n}\}/3$、$P_{4n}(6)=\{1−16^{-n}\}/5$ は独立列挙に一致。図の表示・ラベルも確認 |
| 4 | 5 | 再ビルドした解答全3ページ・図4点確認 | [#1222](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1222)：**等積変形の頂点の取り違えと、符号付き積分を普通の面積とする誤り**。高さの記法、図2のラベル重なりも指摘。最終面積 $2\log(y_2/y_1)$ は独立検算に一致 |
| 5 | 6 | 再ビルドした解答全2ページ・図1点確認 | [#1223](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1223)：**必要条件で得た候補8組の十分性が未証明**。角度条件、偏角の周期、6箇所の式参照も指摘。最終答えの8組は独立列挙に一致 |
| 6 | 7 | 再ビルドした解答全5ページ・図7点確認 | [#1224](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1224)：**ベクトルの係数展開と垂線長の等式が不成立**。長さの二乗の符号、相似比導出の飛躍、場合分け、式参照、図2のラベルも指摘。最大値 $3\sqrt6/8$ は独立検算に一致 |

2010年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2011年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドしたPDF全2ページ・図2点・増減表1点を照合し、面積と増減を独立に検算した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページを照合し、固定点の候補と有理数の場合の停止を独立に検算した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全2ページ・図1点を照合し、積分と極限を独立に検算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドしたPDF全3ページ・図3点を照合し、軌跡の範囲を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドした問題PDF全1ページ・解答PDF全3ページ・図2点を照合し、数え上げを全列挙で検算した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全4ページ・図5点を照合し、体積を別の積分順序で独立に検算した。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全2ページ・図2点・増減表1点確認 | [#1225](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1225)：**導関数の分母の次数が誤り**。図2のラベル重なりも指摘。最大となる $a=2−\sqrt3$ は独立検算に一致。導関数の誤りは手書きにもある |
| 2 | 3 | 再ビルドした解答全2ページ確認 | [#1226](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1226)：**不等式の二乗で $m$ の係数が誤り、表示行から整数範囲が導けない**。既約分母から任意の分母への説明も指摘。最終結論は独立検算に一致。係数誤りは手書きにもある |
| 3 | 4 | 再ビルドした解答全2ページ・図1点確認 | [#1227](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1227)：**極限用の展開式から対数記号が3箇所脱落**。最終極限 $-L$ は独立検算に一致。展開式はTeXで追加された箇所 |
| 4 | 5 | 再ビルドした解答全3ページ・図3点確認 | [#1228](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1228)：**判別式の係数が半分になり、図1で $Q$ と $R$ が逆**。式参照と変数名も指摘。最終軌跡は独立検算に一致。判別式の誤りは手書きにもある |
| 5 | 6 | 再ビルドした問題全1ページ・解答全3ページ・図2点確認 | [#1229](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1229)：**問題の設問番号が1,1,2にリセット**。解答の $w/W$ 混在も指摘。数え上げと総数 $(p+1)^3$ は独立列挙に一致 |
| 6 | 7 | 再ビルドした解答全4ページ・図5点確認 | [#1230](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1230)：**領域図と断面図のラベル重なり、断面の範囲指定の欠字**。体積 $17/18$ は別の積分順序で独立検算に一致 |

2011年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。全問のWeb実表示が未確認のため、監査完了とはしない。

## 2012年度（進行中）

手書きPDFは全6ページ（物理1ページは表紙）。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドした解答PDF全2ページ・図2点を照合し、元の領域で線分長の最大値を独立に検算した。第2問は物理4ページの手書き原稿、問題・解答TeX、再ビルドした問題・解答PDF各全1ページ・図2点を照合し、2歩遷移を独立に数え直した。第3問は物理5ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全3ページ・図2点を照合し、回転体の体積を独立に積分した。第4問は物理6ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全1ページを照合し、背理法の2つの主張を独立に検証した。第5・6問は行列問題で解答本文が未作成のため、既存の解答作成Issueで管理する。Web実表示は未確認。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全2ページ・図2点確認 | [#1231](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1231)：**領域の境界が `√2/3` から `√3/3` に変わり、長さ・微分の証明が不成立**。図の交点・ラベルも誤り。最終値 `√6/3` と `cosθ=√3/3` は元の問題に対する独立検算に一致。主要な矛盾は手書きにもある |
| 2 | 4 | 再ビルドした問題・解答各全1ページ・図2点確認 | [#1232](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1232)：**解答図が9部屋を再現せず、`P` が逆向きの部屋に置かれている**。2歩遷移の確率 `2/3,1/6` と最終式は独立計算に一致。図の不一致はTeX化時に発生 |
| 3 | 5 | 再ビルドした解答全3ページ・図2点確認 | [#1233](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1233)：**体積計算の途中で `π` と `1/2` 係数が脱落**。最終的な2つの体積と大小判定は独立積分に一致。2箇所ともTeX化時に発生 |
| 4 | 6 | 再ビルドした解答全1ページ確認 | 追加Issueなし。連続2整数と連続`n`整数の積について、互いに素性と区間に挟む背理法を独立に確認 |
| 5 | 解答原稿なし | 解答本文未作成 | [#773](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/773)：行列問題。現行 `solution.tex` は未対応の案内のみ |
| 6 | 解答原稿なし | 解答本文未作成 | [#774](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/774)：行列問題。現行 `solution.tex` は未対応の案内のみ |

2012年度は解答本文のある第1〜4問の手書き・TeX・生成PDF照合を終えた。第5・6問の解答作成と全問のWeb実表示は未確認。

## 2013年度（進行中）

手書きPDFは全7ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドした解答PDF全2ページ・図1点を照合し、6乗根を独立に確認した。第2問は物理3ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全2ページ・図1点・増減表1点を照合し、極値から共有点の個数を独立に数え直した。第3問は物理4ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全3ページ・図3点を照合し、確率の和を独立に計算した。第4問は物理5ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全2ページ・図1点を照合し、角度と3つの距離を独立に検算した。第5問は物理6ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全1ページを照合し、不等式の解集合と桁の構成を独立に確認した。第6問は物理7ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全4ページ・図5点を照合し、断面積と共通部分の体積を別の積分式から独立に検算した。公開Webの第1〜6問解答ページをブラウザーで開き、各ページの図・増減表または本文の代表箇所を目視した。第5問の末尾に残る `\bigskip` は #1237 に追記済み。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全2ページ・図1点確認 | [#1235](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1235)：**条件(i)の添字が6ではなくn**。図の右端ラベルも近接。最終的な原始6乗根の2組は独立検算に一致 |
| 2 | 3 | 再ビルドした解答全2ページ・図1点・増減表1点確認 | [#1234](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1234)：**正のaの下限が誤り、共有点3個になる値を答えから除外**。正しくは `2/(7π)<a<2/(3π)`。手書きは正しく、TeX化時に発生 |
| 3 | 4 | 再ビルドした解答全3ページ・図3点確認 | [#1236](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1236)：**部分和の添字と `B_n` の極限値が誤り、表示計算は結論の `16/27` にならない**。最終値は独立検算に一致。手書きは正しく、TeX化時に発生 |
| 4 | 5 | 再ビルドした解答全2ページ・図1点確認 | 追加Issueなし。等角120度と距離 `√7/7,2√7/7,4√7/7` は独立計算に一致 |
| 5 | 6 | 再ビルドした解答全1ページ確認 | [#1237](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1237)：**二次不等式の解の和集合を同時条件として表示**。正の解の範囲と99個の1の構成は独立検証に一致 |
| 6 | 7 | 再ビルドした解答全4ページ・図5点確認 | [#1238](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1238)：**断面積の対称性係数と積分の符号がともに誤り、偶然打ち消し合っている**。負の `k` の交点と図のラベル重なりも指摘。最終体積 `32√2/9` は独立検算に一致 |

2013年度は第1〜6問の手書き・TeX・生成PDF照合を終えた。公開Webの解答図・代表箇所は確認したが、全文・全画面幅の目視と問題ページの表示確認は未完了。

## 2014年度（進行中）

手書きPDFは全8ページ。第1問は物理2ページの手書き原稿、問題・解答TeX、現行TeXから再ビルドした解答PDF全2ページ・図1点を照合し、平行四辺形の面積と角度条件を独立に検算した。第2問は物理3・4ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全2ページ・図2点を照合し、確率の漸化式と平均値を独立に検算した。第3問は物理5ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全3ページ・図1点を照合し、判別式と積分を独立に検算した。第4問は物理6ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全3ページ・図3点を照合し、固定点の存在を独立に検証した。第5問は物理7ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全2ページを照合し、有限剰余列の論証を独立に検証した。第6問は物理8ページの手書き原稿、問題・解答TeX、再ビルドした解答PDF全3ページ・図4点を照合し、線分の到達領域を独立に検算した。公開Webの解答ページは第1〜6問をブラウザーで開き、解答図と本文末尾を目視した。第1問のcaptionの生TeX表示と図内ラベルの密集、第2問の状態図内ラベルの密集、第3問の原点ラベル重なりは既存Issueに含めた。

| 問 | 原稿物理ページ | PDF | 指摘・確認結果 |
|---|---:|---|---|
| 1 | 2 | 再ビルドした解答全2ページ・図1点確認 | [#1239](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1239)：**問題のQ・Rが解答の図とベクトル式で入れ替わる**。面積式と数値は独立検算に一致。点名の矛盾は手書きにもある |
| 2 | 3・4 | 再ビルドした解答全2ページ・図2点確認 | [#1240](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1240)：**平均確率の有限和で分母 `a+2` が1個脱落**。状態図のラベル重なりも指摘。最終極限 `1/(a+2)` は独立検算に一致 |
| 3 | 5 | 再ビルドした解答全3ページ・図1点確認 | [#1241](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1241)：**図の点名と積分変数変換後の関数名が不一致**。図の原点ラベルも重なる。最終積分 `21π/8` は独立検算に一致 |
| 4 | 6 | 再ビルドした解答全3ページ・図3点確認 | [#1242](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1242)：**補助関数の極大点と接線の作図が数式に不一致**。固定点の存在証明は独立検証で成立 |
| 5 | 7 | 再ビルドした解答全2ページ確認 | [#1243](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1243)：**背理法の差の符号が逆で表示証明が不成立**。帰納の根拠も修正が必要。結論は独立検証で成立 |
| 6 | 8 | 再ビルドした解答全3ページ・図4点確認 | [#1244](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1244)：**線分の範囲制約が欠け、途中の値域が過大**。場合分けの空区間と図の重なりも指摘。最終答案は独立検算に一致 |

2014年度は第1〜6問の手書き・TeX・生成PDF照合と、公開Webの解答図・本文末尾の目視を終えた。Webの全文・全画面幅の目視と問題ページの表示確認は未完了。

## 公開Webの構造検査（2026-10-29）

公開中の `utokyo-zenki-YYYY-Q-solution/` 316ページを取得し、HTTP応答と本文中に残る `\\begin{...}`・`\\label{...}` 等の生TeX命令を機械的に調べた。各ページの結果は [web-structural-report.json](web-structural-report.json) に保存した。**316ページすべてがHTTP 200**、**56ページに生TeX命令を検出**。そのうち54ページは1962〜1978年度に集中し、旧形式原稿と初期の変換不良に対応する。残る2ページは1991年第3問の増減表セルと1998年第5問の式ラベルで、既存Issue [#1114](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1114)、[#1157](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1157) に行番号つきで追記した。

この検査はHTML内の文字列と応答状態だけを調べた。数式の描画、図の可読性、全316ページの目視を確認したものではない。2014年第1〜6問は別途ブラウザーで表示し、解答本文末尾と該当する図を目視した。新規Issueのサイト上の一覧は前回ビルド時点で0件表示であり、最新状態はGitHubのIssueを参照する。

同じ316ページの `<img>` 参照先も取得し、結果を [web-image-asset-report.json](web-image-asset-report.json) に保存した。外部の閲覧数カウンターを除いた解答図では、**1965年第1問のベン図2点がHTTP 404**であり、[#1245](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1245) に記録した。ほかの解答図の画像URLはHTTP 200だった。この確認は画像ファイルの取得可否であり、内容の正しさや可読性の判定ではない。

本文の生TeX命令を `\` に続く英字列として広く探した結果は [web-raw-commands-report.json](web-raw-commands-report.json) に保存した。84ページで何らかの命令が見つかり、1991年以降の23問では既存の問題別Issueへ行番号つきで追記した。例として1996年第3問の `\triangle`、2003年第2問の `\bf`、2005年第3問の増減表のMathJaxエラー、2014年第1問のcaption内 `\texttt` がある。1990年第4問の `\null` は解答未作成のプレースホルダーに由来し、解答作成Issue [#475](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/475) で管理する。文字列検査は命令の見落としを減らすためのもので、描画品質の全件目視を代替しない。

MathJaxの典型的なエラーメッセージも316ページで探した。結果は [web-math-error-report.json](web-math-error-report.json)。該当した3問は、1977年第6問の凹凸表（[#1047](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1047)へ追記）、1978年第5問の二重添字（[#1246](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1246)を作成）、2005年第3問の増減表（[#1194](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1194)へ追記）である。

生TeXが見つかった初期年度のうち、問題別の指摘Issueがなかった旧形式14問は [#1247](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1247)〜[#1260](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1260) に分けた。各問の行には対応Issueを記載した。共通の形式移行は引き続き [#593](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/593) で管理する。
