import assert from 'node:assert/strict';
import test from 'node:test';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { parseSolutionOrigins, readSolutionOrigins, isPostHighschoolSolution } from '../src/lib/solution-origins.mjs';

test('marks solutions from yearFrom onward and explicit IDs as post-highschool while honoring exclude', () => {
	const config = parseSolutionOrigins({
		rules: { post_highschool_year_from: 2015 },
		post_highschool: ['utokyo/zenki/1995/2'],
		exclude: ['titech/zenki/2016/3'],
	});

	assert.equal(isPostHighschoolSolution({ university: 'titech', category: 'zenki', year: '2015', question: '1', type: 'solution' }, config), true);
	assert.equal(isPostHighschoolSolution({ university: 'titech', category: 'zenki', year: '2026', question: '5', type: 'solution' }, config), true);
	assert.equal(isPostHighschoolSolution({ university: 'utokyo', category: 'zenki', year: '1995', question: '2', type: 'solution' }, config), true);
	assert.equal(isPostHighschoolSolution({ university: 'utokyo', category: 'zenki', year: '1995', question: '1', type: 'solution' }, config), false);
	assert.equal(isPostHighschoolSolution({ university: 'titech', category: 'zenki', year: '2016', question: '3', type: 'solution' }, config), false);
});

test('ignores summaries, problems, and non-digit years', () => {
	const config = parseSolutionOrigins({ rules: { post_highschool_year_from: 2015 } });
	assert.equal(isPostHighschoolSolution({ university: 'titech', category: 'zenki', year: '2023', question: '0', type: 'summary' }, config), false);
	assert.equal(isPostHighschoolSolution({ university: 'titech', category: 'zenki', year: '2023', question: '1', type: 'problem' }, config), false);
	assert.equal(isPostHighschoolSolution({ university: 'titech', category: 'zenki', year: 'sample', question: '1', type: 'solution' }, config), false);
});

test('reads YAML file from disk cleanly', () => {
	const dir = mkdtempSync(join(tmpdir(), 'math-origins-'));
	try {
		const yamlPath = join(dir, 'solution_origins.yaml');
		writeFileSync(yamlPath, 'rules:\n  post_highschool_year_from: 2015\npost_highschool:\n  - ukyoto/zenki/2001/4\nexclude: []\n');
		const config = readSolutionOrigins(yamlPath);
		assert.equal(isPostHighschoolSolution({ university: 'ukyoto', category: 'zenki', year: '2001', question: '4', type: 'solution' }, config), true);
		assert.equal(isPostHighschoolSolution({ university: 'ukyoto', category: 'zenki', year: '2001', question: '3', type: 'solution' }, config), false);
	} finally {
		rmSync(dir, { recursive: true, force: true });
	}
});
