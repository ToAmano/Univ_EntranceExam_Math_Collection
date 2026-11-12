/** Group recorded solutions that share the same two integer metrics. */
export function groupSolutionsByPosition(solutions) {
	const positions = new Map();
	for (const solution of solutions) {
		const key = `${solution.equalities}:${solution.case_markers}`;
		if (!positions.has(key)) {
			positions.set(key, {
				key,
				equalities: solution.equalities,
				caseMarkers: solution.case_markers,
				items: [],
			});
		}
		positions.get(key).items.push(solution);
	}
	return [...positions.values()].sort((a, b) =>
		a.caseMarkers - b.caseMarkers || a.equalities - b.equalities
	);
}
