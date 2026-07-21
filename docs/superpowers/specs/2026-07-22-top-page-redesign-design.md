# Top Page Redesign & Category Routing Design Spec

## 1. 概要 (Overview)
Webポータル（Astro）のトップページ（`/`）を再設計し、大学・区分（東大・東工大・京大 × 前期・後期 の全6カテゴリ）のカード選択画面に変更します。
Astro の View Transitions（`<ClientRouter />`）を活用し、カード選択からカテゴリ別一覧ページ（`/category/[university]/[category]`）への滑らかでシームレスな遷移を実現します。
さらに、カテゴリ別一覧ページにリアルタイム検索バーを追加し、年度や大問番号による高速なインクリメンタルサーチを提供します。

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
- **Hero Header**: ポータルのタイトル、サブタイトル。
- **6大カテゴリ・カードグリッド (2x3 or 3x2)**:
  - 各カードには大学ロゴ/イニシャル、大学名、区分名（前期/後期）、収録問題数バッジ、ブランドアクセントカラーを配置。
  - `transition:name={`card-${univId}-${catId}`}` を付与。

### 3.3 `src/pages/category/[university]/[category].astro` (カテゴリ別一覧ページ & 検索バー)
- **パンくずリスト**: `トップ ( / )` ➔ `[大学名]` ➔ `[区分名]`
- **ヘッダーセクション**: 選択された大学・区分のタイトルとブランドバッジ (`transition:name`)。
- **リアルタイム検索バー (新規機能)**:
  - カテゴリヘッダー直下にインプットフィールドを設置（例：「年度や大問番号で検索... 例: 1995, 第1問」）。
  - クライアントサイド JavaScript によるリアルタイム絞り込み。
  - 一致する問題がない年度カードの自動非表示、および「検索結果なし」メッセージの動的表示。
- **年度別・問題カード一覧**: 該当カテゴリの問題を年度ごとにグループ化してカード表示。

### 3.4 `src/pages/solutions/[...slug].astro` (問題・解答詳細)
- 既存の解答詳細表示を維持。
- パンくずリストを拡張し、`トップ` ➔ `[大学・区分一覧]` ➔ `[問題名]` へのナビゲーションを提供。

---

## 4. UI/UX & デザイン仕様 (Aesthetics)
- **Dark Mode Glassmorphism**: `#07090e` 背景 + `rgba(15, 23, 42, 0.65)` のグラデーションとぼかし背景 (`backdrop-filter: blur(12px)`).
- **リアルタイム検索 UI**:
  - ガラスモルフィズム調のインプット枠 + 🔍 アイコン + クリアボタン（`×`）。
  - 入力フォーカス時のネオン発光アニメーション (`box-shadow: 0 0 15px rgba(96, 165, 250, 0.3)`).
- **大学別アクセントカラー**:
  - 東京大学: クリムゾン・ブライトブルー (`#ef4444` / `#3b82f6`)
  - 東京工業大学: エメラルドグリーン (`#10b981`)
  - 京都大学: ディープバイオレット/アメジスト (`#8b5cf6`)

---

## 5. テスト & 事前検証手順 (Verification Protocol)
1. `export PATH="$HOME/.nvm/versions/node/v22.16.0/bin:$PATH" && cd web && npm run build` によるビルドエラーチェック。
2. カテゴリページでの検索入力によるリアルタイム絞り込みの動作確認。
