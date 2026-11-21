const CATEGORIES = [
	{ id: 'utokyo-zenki', label: '東大 前期', university: 'utokyo', category: 'zenki' },
	{ id: 'utokyo-kouki', label: '東大 後期', university: 'utokyo', category: 'kouki' },
	{ id: 'ukyoto-zenki', label: '京大 前期', university: 'ukyoto', category: 'zenki' },
	{ id: 'ukyoto-kouki', label: '京大 後期', university: 'ukyoto', category: 'kouki' },
	{ id: 'titech-zenki', label: '東工大 前期', university: 'titech', category: 'zenki' },
	{ id: 'titech-kouki', label: '東工大 後期', university: 'titech', category: 'kouki' },
];

export function buildTopicExplorer(entries, problemTypes, baseUrl) {
	const problemSlugs = new Map();
	for (const entry of entries) {
		if (entry.data.type === 'problem') {
			const { university, category, year, question } = entry.data;
			problemSlugs.set(`${university}/${category}/${year}/${question}`, entry.slug);
		}
	}
	return CATEGORIES.map((category) => {
		const decades = new Map();
		for (const entry of entries) {
			const data = entry.data;
			if (data.type !== 'solution' || data.university !== category.university || data.category !== category.category || !/^\d{4}$/.test(data.year)) continue;
			const year = Number(data.year);
			const decade = Math.floor(year / 10) * 10;
			if (!decades.has(decade)) decades.set(decade, new Map());
			const years = decades.get(decade);
			if (!years.has(year)) years.set(year, []);
			const key = `${data.university}/${data.category}/${data.year}/${data.question}`;
			const problemSlug = problemSlugs.get(key);
			years.get(year).push({
				question: data.question,
				tags: data.tags ?? [],
				kind: problemTypes[key] ?? 'unclassified',
				problemHref: problemSlug ? `${baseUrl}/solutions/${problemSlug}/` : null,
				solutionHref: `${baseUrl}/solutions/${entry.slug}/`,
			});
		}
		return {
			...category,
			decades: [...decades].sort(([a], [b]) => b - a).map(([decade, years]) => ({
				decade,
				years: [...years].sort(([a], [b]) => b - a).map(([year, questions]) => ({
					year,
					questions: questions.sort((a, b) => Number(a.question) - Number(b.question)),
				})),
			})),
		};
	});
}
