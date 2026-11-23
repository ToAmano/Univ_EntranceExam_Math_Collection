import { getCollection } from 'astro:content';
import { univName, catName } from './labels';
import newsAuto from '../data/news-auto.json';
import {
	aggregateAutoNews,
	resolveNewsProblemHref,
	resolveNewsYearHref,
} from './news-grouping.mjs';

export type NewsSegment = {
	text: string;
	href?: string;
};

export type NewsItem = {
	date: string; // "YYYY-MM-DD"
	title: string;
	source: 'auto' | 'manual';
	href?: string;
	segments?: NewsSegment[];
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

type RouteLookup = {
	slugs: Set<string>;
	years: Set<string>;
};

let routeLookupPromise: Promise<RouteLookup> | null = null;

async function getRouteLookup(): Promise<RouteLookup> {
	if (!routeLookupPromise) {
		routeLookupPromise = getCollection('solutions').then((entries) => {
			const slugs = new Set<string>();
			const years = new Set<string>();
			for (const entry of entries) {
				slugs.add(entry.slug);
				const { university, category, year, type } = entry.data;
				if (!university.startsWith('sample_') && /^\d{4}$/.test(year) && type === 'problem') {
					years.add(`${university}/${category}/${year}`);
				}
			}
			return { slugs, years };
		});
	}
	return routeLookupPromise;
}

/** Prepend Astro BASE_URL to root-relative internal news links. */
export function withNewsBaseUrl(href: string, baseUrl: string): string {
	if (/^https?:\/\//.test(href)) return href;
	if (!href.startsWith('/')) return href;
	if (baseUrl && href !== baseUrl && !href.startsWith(`${baseUrl}/`)) {
		return `${baseUrl}${href}`;
	}
	return href;
}

function questionListLabel(questions: string[]): string {
	const nums = questions
		.filter((q) => q !== '0')
		.sort((a, b) => parseInt(a, 10) - parseInt(b, 10));
	if (nums.length === 0) return '全体サマリ';
	return `第${nums.join(',')}問`;
}

function detailedAutoNews(lookup: RouteLookup): NewsItem[] {
	return autoDays.flatMap((day) => day.groups.map((group) => {
		const nums = group.questions
			.filter((q) => q !== '0')
			.sort((a, b) => parseInt(a, 10) - parseInt(b, 10));
		const baseLabel = `${univName(group.university)} ${catName(group.category)} ${group.year}年`;
		const suffix = `の解答を${ACTION_LABEL[group.action]}`;
		const yearHref = resolveNewsYearHref(group.university, group.category, group.year, lookup.years);
		const segments: NewsSegment[] = [];

		if (nums.length === 0) {
			const summaryHref = resolveNewsProblemHref(
				{ university: group.university, category: group.category, year: group.year, question: '0' },
				lookup.slugs,
				lookup.years,
			);
			segments.push({ text: `${baseLabel} 全体サマリ`, href: summaryHref });
		} else if (nums.length === 1) {
			const qHref = resolveNewsProblemHref(
				{ university: group.university, category: group.category, year: group.year, question: nums[0] },
				lookup.slugs,
				lookup.years,
			);
			segments.push({ text: `${baseLabel} 第${nums[0]}問`, href: qHref });
		} else {
			segments.push({ text: baseLabel, href: yearHref });
			segments.push({ text: ' ' });
			nums.forEach((q, idx) => {
				if (idx > 0) segments.push({ text: '・' });
				const qHref = resolveNewsProblemHref(
					{ university: group.university, category: group.category, year: group.year, question: q },
					lookup.slugs,
					lookup.years,
				);
				segments.push({ text: `第${q}問`, href: qHref });
			});
		}
		segments.push({ text: suffix });

		return {
			date: day.date,
			title: `${baseLabel} ${questionListLabel(group.questions)}${suffix}`,
			source: 'auto' as const,
			href: segments.find((seg) => seg.href)?.href,
			segments,
		};
	}));
}

function dailyAutoNews(lookup: RouteLookup): NewsItem[] {
	return autoDays.map((day) => {
		const first = day.lead;
		const rest = day.items.length - 1;
		const actions = new Set(day.items.map((item) => item.action));
		const action = actions.size > 1 ? 'mixed' : first.action;
		const leadLabel = `${univName(first.university)} ${catName(first.category)} ${first.year}年 ${questionListLabel([first.question])}`;
		const leadHref = resolveNewsProblemHref(first, lookup.slugs, lookup.years);
		const suffix = `の解答を${ACTION_LABEL[action]}`;
		const segments: NewsSegment[] = [{ text: leadLabel, href: leadHref }];
		if (rest > 0) {
			segments.push({ text: ' ' });
			segments.push({ text: `ほか${rest}件`, href: `/news/#${day.date}` });
		}
		segments.push({ text: suffix });

		return {
			date: day.date,
			title: `${leadLabel}${rest ? ` ほか${rest}件` : ''}${suffix}`,
			source: 'auto' as const,
			href: leadHref,
			segments,
		};
	});
}

async function mergeWithManual(autoItems: NewsItem[]): Promise<NewsItem[]> {
	const manual = await getCollection('news');
	const manualItems: NewsItem[] = manual.map((entry) => ({
		date: entry.data.date,
		title: entry.data.title,
		source: 'manual',
		href: entry.data.href,
		segments: [{ text: entry.data.title, href: entry.data.href }],
	}));

	return [...manualItems, ...autoItems].sort((a, b) => (a.date < b.date ? 1 : a.date > b.date ? -1 : 0));
}

/** Full archive: daily groups by university, exam, year and action. */
export async function getMergedNews(): Promise<NewsItem[]> {
	const lookup = await getRouteLookup();
	return mergeWithManual(detailedAutoNews(lookup));
}

/** Home page: one digest per date, alongside untouched manual announcements. */
export async function getRecentNews(): Promise<NewsItem[]> {
	const lookup = await getRouteLookup();
	return mergeWithManual(dailyAutoNews(lookup));
}
