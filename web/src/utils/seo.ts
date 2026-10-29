export interface BreadcrumbItemInput {
	name: string;
	url: string;
}

// パンくずリストの構造化データ。検索結果にパンくず(URL代わりの階層パス)を
// 表示させるための標準的な形式。最後の要素(現在ページ)はリンクが無い場合も
// あるが、BreadcrumbListのitem自体は常にURLを要求するため、呼び出し側で
// 現在ページのURLを渡す想定(リンクとして機能しなくてもitemとしては有効)。
export function buildBreadcrumbListJsonLd(items: BreadcrumbItemInput[]) {
	return {
		'@context': 'https://schema.org',
		'@type': 'BreadcrumbList',
		itemListElement: items.map((item, i) => ({
			'@type': 'ListItem',
			position: i + 1,
			name: item.name,
			item: item.url,
		})),
	};
}
