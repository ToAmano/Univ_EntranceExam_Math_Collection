// JSON-LD構造化データ生成用のヘルパー。
// Astroのcontent collectionsが持つ生のMarkdownソース(entry.body)から、
// 数式や図のマークアップをなるべく取り除いた素のテキストを作る。
// 完全な変換(MathJaxレンダリング結果の反映等)は行わず、あくまで
// 検索エンジン向けの要約的なテキストを得ることが目的。
export function markdownToPlainText(markdown: string, maxLen = 3000): string {
	let text = markdown;

	// HTMLコメントを除去
	text = text.replace(/<!--[\s\S]*?-->/g, ' ');
	// figure/imgブロック(TikZ由来の図)を除去。キャプション文字列は図の説明として
	// 残したいので、<figcaption>の中身だけ救出してから残りのHTMLタグを剥がす。
	text = text.replace(/<figcaption>([\s\S]*?)<\/figcaption>/g, ' $1 ');
	text = text.replace(/<[^>]+>/g, ' ');
	// 見出し記号・箇条書き記号・強調記号を除去
	text = text.replace(/^#{1,6}\s*/gm, '');
	text = text.replace(/^[-*]\s+/gm, '');
	text = text.replace(/\*\*([^*]+)\*\*/g, '$1');
	// 空白類を1つに畳む
	text = text.replace(/\s+/g, ' ').trim();

	if (text.length > maxLen) {
		text = text.slice(0, maxLen) + '…';
	}
	return text;
}

export interface QAPageJsonLdInput {
	url: string;
	questionName: string;
	questionText: string;
	answerText: string;
}

export function buildQAPageJsonLd({ url, questionName, questionText, answerText }: QAPageJsonLdInput) {
	return {
		'@context': 'https://schema.org',
		'@type': 'QAPage',
		mainEntity: {
			'@type': 'Question',
			name: questionName,
			text: questionText,
			answerCount: 1,
			acceptedAnswer: {
				'@type': 'Answer',
				text: answerText,
				url,
			},
		},
	};
}

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
