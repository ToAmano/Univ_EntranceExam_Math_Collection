# 東大・京大・東工大 数学過去問解答ライブラリ

東大、京大、東工大の理系数学の過去問解答（手書きPDFおよびTeXによる高品質解答）を公開・管理するリポジトリです。

## 🌐 公開サイト (GitHub Pages)
最新の解答は以下のサイトでご覧いただけます。数式が高速で表示され、スマートフォンにも最適化されています。
👉 **[過去問解答サイトのURL（予定）](https://amano.github.io/Math-Solutions/)**

## 📂 リポジトリ構成

* `src/`: LaTeXによる解答ソース（マスターデータ）。大問フォルダ一体型で管理。
* `web/`: AstroによるWebサイトプロジェクト。

## 🛠️ ローカルでのビルド方法

### 1. Webサイトのローカル開発
```bash
cd web
npm install
npm run dev
```

### 2. PDF書籍のビルド (LuaLaTeX)
```bash
cd src/sample_todai/zenki/1990/1
# 個別ビルドは各フォルダにて行えます。
```
