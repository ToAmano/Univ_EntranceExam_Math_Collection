# 東大・東工大・京大 数学過去問解答ディレクトリ調査報告書

本ドキュメントは、以下の3つのディレクトリ内に分散している、大学入試数学（過去問解答）の「手書きPDF」および「TeXソースファイル」の配置状況を整理したものです。

1. **`Math-Solutions`** (本リポジトリ): `/Users/amano/works/research/Math-Solutions`
2. **`titech_kouki`**: `/Users/amano/works/research/titech_kouki`
3. **`homepage_solutions`**: `/Users/amano/works/research/homepage/docs/_pages/ent-ex/solutions`

---

## 1. 全体俯瞰（データ配置マップ）

各大学・試験区分ごとのデータがどこに存在するかをマッピングしました。

| 大学・区分 | 年度範囲 | 手書きPDFの場所 | TeXソースの場所 | 備考・ステータス |
| :--- | :--- | :--- | :--- | :--- |
| **東大 前期** | 1961-2014 | `homepage_solutions/東大前期_整理完了/` | `homepage_solutions/todai/todai-zenki/` | 一部年度（1965, 1970, 1976, 1982等）で大問欠落あり。TeXは未統合で大問ごとに散在。 |
| **東大 後期** | 1990-2007 | `titech_kouki/UtokyoKouki/.../handwriting_solutions/`<br>`homepage_solutions/東京後期_整理完了/` | `titech_kouki/UtokyoKouki/` | 手書きPDFは同内容（サイズ一致）。TeXは年度ごとに整理済み。 |
| **京大 前期** | 1961-2014 | `homepage_solutions/京都前期_整理完了/` | `homepage_solutions/kyodai/zenki/` | 手書きPDFは整理完了。TeXソースは未統合で大問ごとに散在。 |
| **京大 後期** | 1989-2006 | `Math-Solutions/京大_後期/`<br>`homepage_solutions/京都後期_整理完了/` | `titech_kouki/KyotoUKouki/` | 手書きPDFは一部バージョン違いの可能性（サイズが若干異なる）。TeXは年度ごとに整理済み。 |
| **東工大 前期** | 1961-2014 | 未確認（※1） | `homepage_solutions/toukou/toukou-zenki/` | 手書きPDFは見当たらず（※1）。TeXソース由来らしき小サイズPDFが `homepage_solutions` 内にある。 |
| **東工大 後期** | 1990-2011 | `Math-Solutions/東工大_後期/`<br>`homepage_solutions/TK_kouki/`<br>`homepage_solutions/東工後期_整理完了/` | `titech_kouki/TitechKouki/` | 手書きPDFが3箇所に重複。TeXは年度ごとに整理済み。 |

> [!NOTE]
> ※1: `Math-Solutions/README.md` には「東工大 理系数学 前期 1961-2013 完了」とありますが、今回調査した3ディレクトリの中に該当する「手書きPDF」は見当たりませんでした。`homepage_solutions/toukou/toukou-zenki/` にあるPDFは、サイズが100KB前後と非常に小さく、TeXコンパイル済みのPDFとみられます。

---

## 2. ディレクトリごとの詳細構造

### ① `Math-Solutions` (本リポジトリ)
手書きPDFの公開用リポジトリとして整備中のもの。現在は「後期試験」の手書きPDFのみが格納されています。

* **`京大_後期/`**: 18ファイル (`UK1989.pdf` 〜 `UK2006.pdf`)
* **`東工大_後期/`**: 22ファイル (`1990.pdf` 〜 `2011.pdf`)
* **`README.md`**: 東工大後期のPDFリンク表が作成されている。京大後期などは準備中。

### ② `titech_kouki` (TeX化の作業スペース)
「後期試験」のTeX化作業が非常に綺麗に整理されています。また、東大後期の手書きPDFもなぜかここに混入しています。

* **`KyotoUKouki/manuscript/`** (京大後期: 1989-2006)
  * `docs/problems/[年度]/`: 問題文TeXソース
  * `docs/solutions/[年度]/`: 解答TeXソース
  * `out/main.pdf`: 一括ビルドされたPDF
* **`TitechKouki/manuscript/`** (東工大後期: 1990-2011)
  * `docs/problems/` & `docs/solutions/`: 同上
  * `out/main.pdf`: 一括ビルドされたPDF
* **`UtokyoKouki/manuscript/`** (東大後期: 1990-2007)
  * `docs/problems/` & `docs/solutions/`: 同上
  * `docs/handwriting_solutions/`: **東大後期の手書きPDF** (`東大1990.pdf` 〜 `東大2007.pdf`)
  * `out/main.pdf`: 一括ビルドされたPDF

### ③ `homepage_solutions` (HP公開用データ置き場)
過去にWebサイト上で公開されていた（または現在公開中の）データ群。前期・後期、手書き・TeXが入り乱れており、最も散らかっています。

* **手書きPDF（整理完了フォルダ群）**:
  * `京都前期_整理完了/` (`京都1961.pdf` 〜 `京都2014.pdf` 計54本)
  * `京都後期_整理完了/` (`京都1989.pdf` 〜 `京都2006.pdf` 計18本)
  * `東京後期_整理完了/` (`東大1990.pdf` 〜 `東大2007.pdf` 計18本)
  * `東大前期_整理完了/` (`東大1961.pdf` 〜 `東大2014.pdf` 計53本 ※一部欠落あり)
  * `東工後期_整理完了/` (`TK1990.pdf` 〜 `TK2011.pdf` 計22本)
  * `TK_kouki/` (`1990.pdf` 〜 `2011.pdf` 計22本)
* **TeXソース / バラPDF**:
  * `todai/todai-zenki/[年度]/[大問]/`: 東大前期の大問ごとのTeXソースとPDF。
  * `kyodai/zenki/[年度]/`: 京大前期の大問ごとのデータ。
  * `toukou/toukou-zenki/t[年度]/`: 東工大前期のPDFファイル群（一部TeXソースあり）。

---

## 3. データの重複とバージョン差異の懸念

手書きPDFにおいて、同じ年度のものが複数箇所に存在し、ファイルサイズが異なっているものが一部見受けられます。

1. **東工大 後期（1990-2011）**:
   * `Math-Solutions/東工大_後期/` 内の `1990.pdf` (1,480.8 KB) と `homepage_solutions/TK_kouki/` 内の `1990.pdf` (1,480.8 KB) は同一。
   * しかし、`homepage_solutions/東工後期_整理完了/` 内の `TK1990.pdf` (2,128.5 KB) はサイズが異なります。解像度やスキャン設定の異なる別バージョンが存在する可能性があります。
2. **京大 後期（1989-2006）**:
   * `Math-Solutions/京大_後期/` 内の `UK1989.pdf` (6,791.4 KB) と `homepage_solutions/京都後期_整理完了/` 内の `京都1989.pdf` (8,956.4 KB) はサイズが異なります。こちらも比較・整理が必要です。
3. **東大 後期（1990-2007）**:
   * `titech_kouki/UtokyoKouki/.../handwriting_solutions/東大1990.pdf` (1,503.9 KB) と `homepage_solutions/東京後期_整理完了/東大1990.pdf` (1,503.9 KB) は同一です。

---

## 4. 今後の整理・統合に向けた提案

この過去問解答リポジトリを正式に公開・整備するために、以下のアクションを提案します。

```mermaid
graph TD
    subgraph 収集・整理
        H[homepage_solutions] -->|整理完了PDFをコピー| M[Math-Solutions リポジトリ]
        T[titech_kouki] -->|東大後期PDFをコピー| M
    end
    subgraph リポジトリ構成案
        M --> M1[前期手書きPDF]
        M --> M2[後期手書きPDF]
        M --> M3[TeXソース]
    end
```

### アクションプラン
1. **手書きPDFの「Math-Solutions」への一元集約**
   * `homepage_solutions/京都前期_整理完了` と `東大前期_整理完了` から、前期の手書きPDFを本リポジトリにコピーし、`京大_前期` `東大_前期` ディレクトリを新設して格納する。
   * `titech_kouki` に入っている東大後期手書きPDFを本リポジトリの `東大_後期` に移行する。
   * 重複している京大後期・東工大後期の手書きPDFについて、内容（画質や書き込み）を比較し、より良い方を残す。
2. **TeXソースの整理と統合**
   * 現在 `titech_kouki` で綺麗に管理されている後期のTeXソースコード群を、本リポジトリに `TeX/` などのディレクトリを作って移管する。
   * 前期のバラバラになっているTeXソース（大問ごとのフォルダ）を、後期と同様のフォルダ構成（年度ごと）に整理し直して統合する。
3. **READMEেরアップデート**
   * 集約したPDFファイルへのリンクをREADMEに追記し、「準備中」のステータスを順次「完了」に更新する。
