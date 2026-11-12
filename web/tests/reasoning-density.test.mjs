import assert from 'node:assert/strict';
import test from 'node:test';
import { groupSolutionsByPosition } from '../src/lib/reasoning-density.mjs';

test('solutions at the same integer position stay discoverable as a group', () => {
	const items = [
		{ id: 'a', equalities: 6, case_markers: 0 },
		{ id: 'b', equalities: 6, case_markers: 0 },
		{ id: 'c', equalities: 6, case_markers: 2 },
	];
	const groups = groupSolutionsByPosition(items);
	assert.equal(groups.length, 2);
	assert.deepEqual(groups[0].items.map((item) => item.id), ['a', 'b']);
	assert.deepEqual(groups[1].items.map((item) => item.id), ['c']);
	assert.equal(groups.reduce((total, group) => total + group.items.length, 0), items.length);
});
