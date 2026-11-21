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
