import { getCollection } from 'astro:content';
import { univName, catName } from './labels';
import newsAuto from '../data/news-auto.json';

export type NewsItem = {
	date: string; // "YYYY-MM-DD"
	title: string;
	source: 'auto' | 'manual';
	href?: string;
};

type AutoEntryItem = {
	university: string;
	category: string;
	year: string;
	question: string;
	action: 'added' | 'updated';
};

type AutoEntry = {
	date: string;
	datetime: string;
	commit: string;
	subject: string;
	action: 'added' | 'updated' | 'mixed';
	items: AutoEntryItem[];
};

const ACTION_LABEL: Record<string, string> = {
	added: '追加しました',
	updated: '更新しました',
};

function questionListLabel(questions: string[]): string {
	const nums = questions
		.filter((q) => q !== '0')
		.sort((a, b) => parseInt(a, 10) - parseInt(b, 10));
	if (nums.length === 0) return '全体サマリ';
	return `第${nums.join(',')}問`;
}

/** 1コミット分のitemsを 大学+区分+年度+action ごとにまとめ、日本語の行に変換する */
function autoEntryToLines(entry: AutoEntry): string[] {
	const groups = new Map<string, AutoEntryItem[]>();
	for (const item of entry.items) {
		const key = `${item.university}|${item.category}|${item.year}|${item.action}`;
		const list = groups.get(key) || [];
		list.push(item);
		groups.set(key, list);
	}
	return Array.from(groups.entries()).map(([key, items]) => {
		const [university, category, year, action] = key.split('|');
		const qLabel = questionListLabel(items.map((i) => i.question));
		return `${univName(university)} ${catName(category)} ${year}年 ${qLabel}の解答を${ACTION_LABEL[action] || '更新しました'}`;
	});
}

/** 自動生成ニュース（src/**\/solution.tex の追加・更新）と手動お知らせをマージし、
 * 日付降順で返す。 */
export async function getMergedNews(): Promise<NewsItem[]> {
	const manual = await getCollection('news');
	const manualItems: NewsItem[] = manual.map((entry) => ({
		date: entry.data.date,
		title: entry.data.title,
		source: 'manual',
	}));

	const autoItems: NewsItem[] = (newsAuto as AutoEntry[]).flatMap((entry) =>
		autoEntryToLines(entry).map((title) => ({
			date: entry.date,
			title,
			source: 'auto' as const,
		}))
	);

	return [...manualItems, ...autoItems].sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
}
