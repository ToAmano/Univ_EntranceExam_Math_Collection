import test from 'node:test';
import assert from 'node:assert/strict';
import {
	readSolutionMetrics,
	getCategoryMeta,
	buildProblemUrl,
} from '../src/lib/solution-metrics.mjs';

test('readSolutionMetrics handles missing or invalid file gracefully', () => {
	const nonExistent = readSolutionMetrics('/path/to/definitely/nonexistent.json');
	assert.equal(nonExistent.available, false);
	assert.equal(nonExistent.data, null);
});

test('readSolutionMetrics loads valid snapshot file', () => {
	// The real generated file exists in web/src/data/solution-metrics.json
	const res = readSolutionMetrics();
	assert.equal(res.available, true);
	assert.ok(res.data);
	assert.equal(res.data.schema_version, 1);
	assert.ok(res.data.overall.valid_solutions > 500);
	assert.ok(Array.isArray(res.data.rankings.longest));
	assert.ok(Array.isArray(res.data.rankings.shortest));
	assert.ok(Array.isArray(res.data.by_field));
	assert.ok(res.data.by_field_by_category);
	assert.ok(Array.isArray(res.data.by_field_by_category.overall));
	assert.ok(Array.isArray(res.data.categories.utokyo_zenki.by_field));
	assert.ok(Array.isArray(res.data.by_era));
});

test('getCategoryMeta returns correct labels and colors', () => {
	const utokyoZenki = getCategoryMeta('utokyo_zenki');
	assert.equal(utokyoZenki.label, '東大前期');
	assert.ok(utokyoZenki.color);

	const ukyotoKouki = getCategoryMeta('ukyoto_kouki');
	assert.equal(ukyotoKouki.label, '京大後期');

	const unknown = getCategoryMeta('unknown_cat');
	assert.equal(unknown.label, 'unknown_cat');
});

test('buildProblemUrl generates standard normalized URLs', () => {
	const baseUrl = '/Univ_EntranceExam_Math_Collection/';
	const item = {
		univ: 'utokyo',
		exam: 'zenki',
		year: 1981,
		question: '6',
	};
	const url = buildProblemUrl(baseUrl, item);
	assert.equal(
		url,
		'/Univ_EntranceExam_Math_Collection/solutions/utokyo-zenki-1981-6-solution/'
	);
});
