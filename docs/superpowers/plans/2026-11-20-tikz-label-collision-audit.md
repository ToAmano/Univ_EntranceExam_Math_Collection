# TikZ Label Collision Audit Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** TikZ 図のラベル同士の交差・近接を、描画結果から根拠付きの監査候補として出す。

**Architecture:** 既存の TikZ 単体コンパイル経路を利用して一時 PDF を得る。PDF の文字位置をラベル候補にまとめ、交差・近接を判定する。Issue 由来の陽性例と正常例で評価してから、read-only の CLI として公開する。

**Tech Stack:** Python 3、LuaLaTeX、Poppler または MuPDF CLI、pytest。追加の Python 依存は評価結果が要求する場合だけ検討する。

**Spec:** `docs/superpowers/specs/2026-11-20-tikz-label-collision-audit-design.md`

## Global Constraints

- 原稿の TeX、既存 PDF・SVG、Issue を変更しない。一時生成物は `/tmp` に置く。
- 候補ゼロを監査合格と表現しない。コンパイル失敗・文字抽出失敗は `unavailable` として報告する。
- 見落としを減らすことを優先する。PDF 全ページと Web 用 SVG の目視手順は維持する。
- 一時コピーの TeX 実行は `audit/visual_prepare.py` と同様に `-no-shell-escape` と一時 `TEXMFCACHE` を使う。
- ユーザーの作業ツリーには既存の未コミット変更がある。既存変更を上書き・整理しない。

## Review Focus

- 数式の上下付き文字と分数が一つのラベルとして扱われること。Task 2 のテストで固定する。
- 近いが別の軸ラベルを検出し、同じラベル内の文字を自己衝突として出さないこと。Task 2・3 のテストで固定する。
- `node` が線上に置かれた場合も図番号と元の TeX ファイルへ戻れること。Task 1・4 のテストで固定する。
- 複数図・複数ページの候補を混同しないこと。Task 1・4 のテストで固定する。
- PDF 抽出に失敗した図を「問題なし」と表示しないこと。Task 2・4 のテストで固定する。

---

### Task 1: 評価集合と図ごとの一時 PDF

**Files:**
- Create: `audit/figure_cases.json` — 評価用の Issue、TeX、図番号、現行描画での陽性・正常の判断を保持。
- Create: `audit/figure_compile.py` — 既存の `scratch/tex_to_md.py` の図抽出・コンパイル処理を利用して、元ファイルを変えずに図ごとの PDF を一時出力。
- Modify: `scratch/tex_to_md.py` — 必要な場合だけ `compile_tikz_to_svg(..., output_pdf_path=None, work_dir=None)` を追加し、生成済みの一時 PDF を呼出側へコピーする。監査時の作業ディレクトリは `/tmp` 以下に指定し、既存の呼出結果は変えない。
- Test: `tests/audit/test_figure_compile.py`、既存の `tests/scratch/test_converter.py`。

**Interfaces:**
- `compile_figures(tex_path: Path, output_dir: Path) -> list[FigurePdf]`。`FigurePdf` は `source`, `figure_index`, `pdf_path`, `status`, `reason` を持つ。
- 図番号は TeX 中の順序に一致させる。失敗した図も結果から落とさない。

- [ ] **Step 1: 評価候補を確認する。** #1194・#1458・#677・#980 の対象図を現行の TeX から描画し、PDF・Web SVG を表示する。現行描画に重なりが残るものだけ陽性とし、正常例を追加する。結果と入力ハッシュを `audit/figure_cases.json` に記録する。先行試作の #1194 は「近接、外接矩形の交差なし」と確認済みだが、作業ツリーの内容を評価時に固定する。
- [ ] **Step 2: 失敗するテストを書く。** 複数図の順序、図番号、失敗図の保持、出力が一時ディレクトリ内に限られることを確認する。`compile_tikz_to_svg` の既存動作を回帰テストにする。
- [ ] **Step 3: テストを実行する。** `python3 -m pytest tests/audit/test_figure_compile.py tests/scratch/test_converter.py -q`。新テストの失敗を確認する。
- [ ] **Step 4: 最小実装を行う。** 既存の図抽出を重複実装せず再利用し、コンパイルごとに一時 PDF とログを保持する。失敗時は理由を戻す。
- [ ] **Step 5: 同じテストを実行する。** 全件 PASS を確認する。

### Task 2: PDF 文字領域の抽出とラベル候補の形成

**Files:**
- Create: `audit/figure_text.py` — MuPDF `stext` または Poppler `bbox-layout` の出力を読み、文字・行・領域を返す。
- Test: `tests/audit/test_figure_text.py` — 小さな固定 PDF と、数式・添字・分数・日本語ラベルを含む PDF。

**Interfaces:**
- `extract_labels(pdf_path: Path) -> list[LabelBox]`。`LabelBox` は `page`, `text`, `bbox_pt`, `components` を持つ。抽出不可は例外で伝える。
- ラベルのまとまりを PDF のブロックだけで決めず、文字の位置・大きさ・基線を利用する。分数の上下成分を分離したまま他ラベルと判定しない。

- [ ] **Step 1: 失敗するテストを書く。** 同一数式の添字・分数は一候補、離れた目盛りは別候補、空の PDF・壊れた XML は明示的失敗、と固定する。
- [ ] **Step 2: `python3 -m pytest tests/audit/test_figure_text.py -q` で失敗を確認する。**
- [ ] **Step 3: `extract_labels` を実装する。** 先行試作では Poppler の `bbox-layout` に XML 不正例が出たため、MuPDF `stext` を先に検証する。採用した抽出器・版を結果に残す。文字がアウトラインのみで取得できないときは推測しない。
- [ ] **Step 4: 同じテストを実行し、全件 PASS を確認する。**

### Task 3: 交差・近接判定と精度評価

**Files:**
- Create: `audit/figure_collision.py` — 領域間距離・交差量の判定と候補の重複統合。
- Create: `audit/figure_evaluate.py` — `figure_cases.json` に対する候補一覧、陽性の検出率、正常例の候補数を出す。
- Test: `tests/audit/test_figure_collision.py`。

**Interfaces:**
- `find_candidates(labels: list[LabelBox], proximity_pt: float) -> list[Collision]`。`Collision` は2ラベル、ページ、交差量または最短距離、候補位置を持つ。
- `evaluate(cases: list[Case], results: list[FigureResult]) -> Evaluation`。Issue 番号だけで正解扱いせず、現行描画で確認した具体的なラベル対を照合する。

- [ ] **Step 1: 失敗するテストを書く。** 実交差、数 pt の近接、離れたラベル、同一ラベル内の文字、別ページ、同じ2ラベル対の重複を確認する。
- [ ] **Step 2: `python3 -m pytest tests/audit/test_figure_collision.py -q` で失敗を確認する。**
- [ ] **Step 3: 判定と評価を実装する。** 近接閾値は評価集合の結果で選び、根拠とともに既定値を記録する。評価では陽性の見落としを先に確認する。
- [ ] **Step 4: 実例で評価する。** 再現した陽性の全件検出と、正常図1枚あたり候補3件以下を初版の目標とする。陽性ごとの検出可否、正常図の候補数、候補の原因を報告する。目標に届かない場合は Task 4 に進む前に、設計案の TikZ ノード領域方式を一時コピーで試し、方式を選び直す。
- [ ] **Step 5: テストを実行し、評価結果をレビューする。** `python3 -m pytest tests/audit/test_figure_collision.py -q`。

### Task 4: read-only CLI と根拠画像

**Files:**
- Create: `audit/figure_audit.py` — `--tex`, `--output`, `--proximity-pt` を受け、図ごとの JSON、Markdown、候補の切り出し画像を生成。
- Create: `tests/audit/test_figure_audit.py`。
- Modify: `docs/audit/visual.md` — 実行例と候補の読み方、PDF・SVG 目視との関係を記載。

**Interfaces:**
- `python3 audit/figure_audit.py --tex src/.../solution.tex --output /tmp/figure-audit-...`。出力先は新規または空のディレクトリ。
- `report.json` は各図の `ready`/`unavailable`、候補、入力ハッシュ、使用した抽出器を記録する。`report.md` は図・ページ・TeX パス・候補画像へのリンクを持つ。

- [ ] **Step 1: 失敗する CLI テストを書く。** 複数図、対象外の出力先、コンパイル失敗、抽出失敗、候補ゼロ、元 TeX と既存 SVG が不変、を確認する。
- [ ] **Step 2: `python3 -m pytest tests/audit/test_figure_audit.py -q` で失敗を確認する。**
- [ ] **Step 3: CLI と画像出力を実装する。** PDF の位置から 200–250 dpi の切り出し画像を作り、候補対を図示する。出力失敗は `unavailable` に記録する。
- [ ] **Step 4: `python3 -m pytest tests/audit/test_figure_audit.py tests/audit/test_figure_compile.py tests/audit/test_figure_text.py tests/audit/test_figure_collision.py tests/scratch/test_converter.py -q` を実行する。** 全件 PASS を確認する。
- [ ] **Step 5: 評価集合を CLI で再実行し、PDF 全ページと Web SVG を目視する。** 報告に陽性の検出率、正常図の候補数、未検出・抽出不可の内訳を記す。合格判定はしない。

## 実装後の判断

PDF 文字方式の精度が足りない場合、既存の CLI を無理に合格判定へ拡張しない。ノード領域方式の比較結果を提示してから検出器を差し替える。`audit/visual_prepare.py` との統合と CI 定期実行は、単独 CLI の品質と実行時間が分かった後の別作業とする。

## 実行時の判断（2026-11-20）

- Ruling: PDF 文字抽出は別々のノード `$A$`・`$B$` を `AB` に結合し、陽性を見落としたため、TikZ ノード領域を第一候補にした。PDF 文字ブロックだけの結果は `partial` と記録する。ノード追跡が特殊な TikZ マクロに効かない可能性が残る。
- Ruling: 既存の `scratch/tex_to_md.py` はこの環境で `yaml` 依存を読み込めなかったため、監査 CLI は独立の一時コンパイルを使う。既存の変換処理に手を加えない代わりに、プリアンブルが将来ずれる可能性がある。コンパイル不能な図は `unavailable` と記録する。
- Ruling: `docs/audit/visual.md` は作業開始時から未追跡の既存ファイルだったため編集せず、新しい評価記録に CLI の使い方を記載した。
- Ruling: 図の途中の `every node/.style` 上書きで領域の記録が消えるため、TikZ 内部のノード総数を別に数え、記録数と一致しない図を `partial` とする。特殊なマクロでノード数の計測自体が変わる可能性は残る。
