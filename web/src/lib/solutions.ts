import type { CollectionEntry } from 'astro:content';

export type SolutionItem = CollectionEntry<'solutions'>;

/** 大問番号としてサマリ行（その年度の全体概要。実問題ではない）を表す値。 */
export const SUMMARY_QUESTION_ID = '0';

/** サマリ行（大問番号が '0'）かどうかを判定する。実問題数のカウントから除外するために使う。 */
export function isSummaryItem(item: SolutionItem): boolean {
	return item.data.question === SUMMARY_QUESTION_ID;
}

function questionKey(item: SolutionItem): string {
	return `${item.data.university}|${item.data.category}|${item.data.year}|${item.data.question}`;
}

/**
 * サマリを除外し、(university, category, year, question) でユニーク化した
 * 「実問題」のリストを返す。problem.tex と solution.tex が両方存在する問題を
 * 2件と数えてしまわないようにするため、ここで一本化する。
 */
export function getRealQuestions(items: SolutionItem[]): SolutionItem[] {
	const seen = new Set<string>();
	const result: SolutionItem[] = [];
	for (const item of items) {
		if (isSummaryItem(item)) continue;
		const key = questionKey(item);
		if (seen.has(key)) continue;
		seen.add(key);
		result.push(item);
	}
	return result;
}

/** 実問題数（サマリ除外・重複排除済み）を返す。表示用の件数はすべてこれを使う。 */
export function countRealQuestions(items: SolutionItem[]): number {
	return getRealQuestions(items).length;
}
