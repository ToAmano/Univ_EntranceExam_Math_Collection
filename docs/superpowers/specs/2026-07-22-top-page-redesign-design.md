# Top Page Redesign & Category Routing Design Spec

## 1. 概要 (Overview)
Webポータル（Astro）のトップページ（`/`）を再設計し、大学・区分（東大・東工大・京大 × 前期・後期 の全6カテゴリ）のカード選択画面に変更します。
Astro の View Transitions（`<ClientRouter />`）を活用し、カード選択からカテゴリ別一覧ページ（`/category/[university]/[category]`）への滑らかでシームレスな遷移を実現します。

---

## 2. カテゴリの定義 (Target 6 Categories)
トップページには以下の全6カテゴリをカードとしてグリッド表示します。

1. **東京大学 - 前期** (`university`: `todai` / `sample_todai`, `category`: `zenki`)
2. **東京大学 - 後期** (`university`: `todai` / `sample_todai`, `category`: `kouki`)
3. **東京工業大学 - 前期** (`university`: `titech` / `sample_titech`, `category`: `zenki`)
4. **東京工業大学 - 後期** (`university`: `titech` / `sample_titech`, `category`: `kouki`)
5. **京都大学 - 前期** (`university`: `kyodai` / `sample_kyodai`, `category`: `zenki`)
6. **京都大学 - 後期** (`university`: `kyodai` / `sample_kyodai`, `category`: `kouki`)

* データが未登録のカテゴリがある場合は、「準備中 (0問)」バッジを表示し、クリック時に準備中案内または空の一覧ページを表示します。

---

## 3. ページ構造 & ルーティング (Architecture & Routes)

### 3.1 `src/layouts/Layout.astro`
- Astro View Transitions (`import { ClientRouter } from 'astro:transitions';`) を `<head>` に導入。
- 全ページでの滑らかなクロスフェード／共通要素のモーフアニメーションに対応。

### 3.2 `src/pages/index.astro` (トップページ)
- **Hero Header**: ポータルのタイトル、サブタイトル、全コンテンツ共通のインタラクティブ検索バー。
- **6大カテゴリ・カードグリッド (2x3 or 3x2)**:
  - 各カードには大学ロゴ/イニシャル、大学名、区分名（前期/後期）、収録問題数バッジ、ブランドアクセントカラーを配置。
  - `transition:name={`card-${univId}-${catId}`}` を付与。
- **クイックリンク/最新更新**: 全体サマリや新着問題への直接リンク。

### 3.3 `src/pages/category/[university]/[category].astro` (カテゴリ別一覧ページ)
- **静的パス生成 (`getStaticPaths`)**: 6つの組み合わせ（`todai`/`titech`/`kyodai` x `zenki`/`kouki` + `sample_*` のエイリアス対応）を定義。
- **ヘッダーセクション**: 選択された大学・区分のタイトルとブランドバッジ。トップページカードと同名の `transition:name` を設定してモーフアニメーションを実現。
- **パンくずリスト**: `トップ ( / )` ➔ `[大学名]` ➔ `[区分名]`
- **年度別・問題カード一覧**: 該当カテゴリの問題（大問0の全体サマリ、大問1〜Nの問題・解答）を年度ごとにグループ化してアコーディオン/カード表示。

### 3.4 `src/pages/solutions/[...slug].astro` (問題・解答詳細)
- 既存の解答詳細表示を維持。
- パンくずリストを拡張し、`トップ` ➔ `[大学・区分一覧]` ➔ `[問題名]` へのナビゲーションを提供。

---

## 4. UI/UX & デザイン仕様 (Aesthetics)
- **Dark Mode Glassmorphism**: `#07090e` 背景 + `rgba(15, 23, 42, 0.65)` のグラデーションとぼかし背景 (`backdrop-filter: blur(12px)`).
- **大学別アクセントカラー**:
  - 東京大学: クリムゾン・ブライトブルー (`#ef4444` / `#3b82f6`)
  - 東京工業大学: エメラルドグリーン (`#10b981`)
  - 京都大学: ディープバイオレット/アメジスト (`#8b5cf6`)
- **マイクロアニメーション**: ホバー時のカード浮き上がり（`transform: translateY(-4px)`）、ボーダー発光、View Transitions によるシームレス移動。

---

## 5. テスト & 事前検証手順 (Verification Protocol)
1. `scratch/tex_to_md.py` 変換が正常であることを確認。
2. `cd web && npm run build` によるビルドエラーチェック。
3. ローカル開発サーバーまたはビルド後のページ遷移・View Transitions アニメーションの動作確認。
