# TikZ ラベル近接検出の小規模評価

2026-11-20 の作業ツリーから4問・8図を一時ディレクトリで描画し、PDF と図画像を確認した。評価対象の TeX とハッシュは `audit/figure_cases.json` に記録した。元の原稿・既存 PDF・SVG は変更していない。

| 参照 Issue | 図 | 目視した状態 | 候補数 |
|---|---:|---|---:|
| [#1194](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1194) | 2 | 縦軸の `1` と `(1+e)/4` が両図で近接 | 3 |
| [#1458](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/1458) | 1 | 原点付近の `-1`、`O`、`6√2−8` が密集 | 4 |
| [#677](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/677) | 4 | 図4の報告済み重なりは現行図では解消 | 5 |
| [#980](https://github.com/ToAmano/Univ_EntranceExam_Math_Collection/issues/980) | 1 | 現行図に明瞭な文字接触なし | 3 |

陽性として固定した3組は3組とも検出した。対応済みの2問では計8候補が残り、拡大画像を確認した範囲ではラベル同士の修正対象はなかった。近接自体は検出しているので、この8件は「レビュー後に対応不要」として記録した。この8図だけでは一般的な検出率・誤検出率を推定できない。

PDF の文字抽出だけでは、別々の TikZ ノードを一つの文字列に結合する例があった。実装はコンパイル時の TikZ ノード領域を第一候補にし、取得できない場合の PDF 文字抽出は `partial` と表示する。既定の近接距離 6 pt は #1194 の非交差のラベル対（ノード領域間 5.824 pt）を含める値。点・空の座標など縦横とも4 pt未満の領域は候補から外した。

CLI は `report.json`、`report.md`、図全体の `figure-N.png` と候補周辺の `candidate-N-M.png` を出す。候補の画像は TeX の図全体の座標から PDF の画素位置へ変換して切り出す。#1458 の原点付近の候補画像を表示し、該当する文字が入ることを確認した。

TeX のログは長い行を折り返すため、ノード領域は一時ファイルへ直接書く。図の途中で `every node` の設定を上書きすると領域の記録が欠ける場合があるので、独立に数えたノード総数と領域の記録件数を照合し、欠落があれば `partial` と表示する。

評価の再実行例：

```bash
python3 audit/figure_audit.py --tex src/utokyo/zenki/2005/3/solution.tex --output /tmp/audit-2005-3
python3 audit/figure_audit.py --tex src/ukyoto/zenki/2012/3/solution.tex --output /tmp/audit-2012-3
python3 audit/figure_audit.py --tex src/titech/zenki/1988/3/solution.tex --output /tmp/audit-1988-3
python3 audit/figure_audit.py --tex src/utokyo/zenki/1961/5/solution.tex --output /tmp/audit-1961-5
python3 audit/figure_evaluate.py --report /tmp/audit-2005-3/report.json --report /tmp/audit-2012-3/report.json --report /tmp/audit-1988-3/report.json --report /tmp/audit-1961-5/report.json
```

対象のハッシュが変わったら、評価の正解組を現行図で再確認する。図の数学的条件、ラベルと線の交差、Web 表示、PDF の全ページの可読性は別途目視する。
