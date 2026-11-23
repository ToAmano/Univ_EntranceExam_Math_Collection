/**
 * Resolve an internal route path for a single problem/summary item when a matching
 * generated page exists in `solutionSlugs` / `yearKeys`, returning undefined otherwise.
 */
export function resolveNewsProblemHref(item, availableSlugs, availableYears = new Set()) {
	const { university, category, year, question } = item;
	const yearKey = `${university}/${category}/${year}`;
	if (question === '0') {
		const summarySlug = `${university}-${category}-${year}-0-summary`;
		if (availableSlugs.has(summarySlug)) return `/solutions/${summarySlug}/`;
		if (availableYears.has(yearKey)) return `/problems/${university}/${category}/${year}/`;
		return undefined;
	}
	const solutionSlug = `${university}-${category}-${year}-${question}-solution`;
	if (availableSlugs.has(solutionSlug)) return `/solutions/${solutionSlug}/`;
	if (availableYears.has(yearKey)) return `/problems/${university}/${category}/${year}/#q${question}`;
	return undefined;
}

/** Resolve an internal year-overview route path if that year page exists. */
export function resolveNewsYearHref(university, category, year, availableYears) {
	if (availableYears.has(`${university}/${category}/${year}`)) {
		return `/problems/${university}/${category}/${year}/`;
	}
	return undefined;
}

/** Collapse commit-level news into unique problems on each displayed date. */
export function aggregateAutoNews(entries) {
	const byDate = new Map();
	for (const entry of entries) {
		if (!byDate.has(entry.date)) byDate.set(entry.date, new Map());
		const questions = byDate.get(entry.date);
		for (const item of entry.items) {
			const key = JSON.stringify([item.university, item.category, item.year, item.question]);
			const existing = questions.get(key);
			if (existing) {
				if (item.action === 'added') existing.action = 'added';
			} else {
				questions.set(key, { ...item });
			}
		}
	}
	return [...byDate].sort(([a], [b]) => b.localeCompare(a)).map(([date, questions]) => {
		const items = [...questions.values()];
		const groups = new Map();
		for (const item of items) {
			const key = JSON.stringify([item.university, item.category, item.year, item.action]);
			if (!groups.has(key)) {
				groups.set(key, {
					university: item.university, category: item.category,
					year: item.year, action: item.action, questions: [],
				});
			}
			groups.get(key).questions.push(item.question);
		}
		return {
			date,
			items,
			lead: items.find((item) => item.question !== '0') ?? items[0],
			groups: [...groups.values()].map((group) => ({
				...group,
				questions: group.questions.sort((a, b) => Number(a) - Number(b)),
			})),
		};
	});
}
