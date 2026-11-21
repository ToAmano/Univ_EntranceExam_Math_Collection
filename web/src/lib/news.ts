import { getCollection } from 'astro:content';
import { univName, catName } from './labels';
import newsAuto from '../data/news-auto.json';
import { aggregateAutoNews } from './news-grouping.mjs';

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

type AutoDay = {
	date: string;
	items: AutoEntryItem[];
	lead: AutoEntryItem;
	groups: Array<{
		university: string;
		category: string;
		year: string;
		action: 'added' | 'updated';
		questions: string[];
	}>;
};

const ACTION_LABEL: Record<string, string> = {
	added: '追加しました',
	updated: '更新しました',
	mixed: '追加・更新しました',
};

const autoDays = aggregateAutoNews(newsAuto as AutoEntry[]) as AutoDay[];

function questionListLabel(questions: string[]): string {
	const nums = questions
		.filter((q) => q !== '0')
		.sort((a, b) => parseInt(a, 10) - parseInt(b, 10));
	if (nums.length === 0) return '全体サマリ';
	return `第${nums.join(',')}問`;
}

function detailedAutoNews(): NewsItem[] {
	return autoDays.flatMap((day) => day.groups.map((group) => ({
		date: day.date,
		title: `${univName(group.university)} ${catName(group.category)} ${group.year}年 ${questionListLabel(group.questions)}の解答を${ACTION_LABEL[group.action]}`,
		source: 'auto' as const,
	})));
}

function dailyAutoNews(): NewsItem[] {
	return autoDays.map((day) => {
		const first = day.lead;
		const rest = day.items.length - 1;
		const actions = new Set(day.items.map((item) => item.action));
		const action = actions.size > 1 ? 'mixed' : first.action;
		return {
			date: day.date,
			title: `${univName(first.university)} ${catName(first.category)} ${first.year}年 ${questionListLabel([first.question])}${rest ? ` ほか${rest}件` : ''}の解答を${ACTION_LABEL[action]}`,
			source: 'auto' as const,
		};
	});
}

async function mergeWithManual(autoItems: NewsItem[]): Promise<NewsItem[]> {
	const manual = await getCollection('news');
	const manualItems: NewsItem[] = manual.map((entry) => ({
		date: entry.data.date,
		title: entry.data.title,
		source: 'manual',
	}));

	return [...manualItems, ...autoItems].sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
}

/** Full archive: daily groups by university, exam, year and action. */
export async function getMergedNews(): Promise<NewsItem[]> {
	return mergeWithManual(detailedAutoNews());
}

/** Home page: one digest per date, alongside untouched manual announcements. */
export async function getRecentNews(): Promise<NewsItem[]> {
	return mergeWithManual(dailyAutoNews());
}
