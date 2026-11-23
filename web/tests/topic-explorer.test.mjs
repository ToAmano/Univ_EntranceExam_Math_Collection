import assert from 'node:assert/strict';
import test from 'node:test';
import { buildTopicExplorer } from '../src/lib/topic-explorer.mjs';

test('groups each question by category, decade and year with its tags, format and page link', () => {
	const entries = [
		{ slug: 'utokyo-zenki-2001-2-solution', data: { type: 'solution', university: 'utokyo', category: 'zenki', year: '2001', question: '2', tags: ['数列', '極限'] } },
		{ slug: 'utokyo-zenki-2001-2-problem', data: { type: 'problem', university: 'utokyo', category: 'zenki', year: '2001', question: '2' } },
		{ slug: 'utokyo-zenki-2001-1-solution', data: { type: 'solution', university: 'utokyo', category: 'zenki', year: '2001', question: '1', tags: ['整数'] } },
	];
	const result = buildTopicExplorer(entries, { 'utokyo/zenki/2001/2': 'mixed', 'utokyo/zenki/2001/1': 'proof' }, '/site');
	assert.deepEqual(result[0].decades[0].years[0].questions.map((q) => q.question), ['1', '2']);
	assert.deepEqual(result[0].decades[0].years[0].questions[1], {
		question: '2', tags: ['数列', '極限'], kind: 'mixed',
		yearProblemsHref: '/site/problems/utokyo/zenki/2001/#q2',
		solutionHref: '/site/solutions/utokyo-zenki-2001-2-solution/',
	});
});

test('shows missing classifications and links to the solution when no problem page exists', () => {
	const entries = [{ slug: 'x', data: { type: 'solution', university: 'ukyoto', category: 'kouki', year: '1999', question: '1' } }];
	const result = buildTopicExplorer(entries, {}, '');
	const question = result.find((c) => c.id === 'ukyoto-kouki').decades[0].years[0].questions[0];
	assert.deepEqual(question.tags, []);
	assert.equal(question.kind, 'unclassified');
	assert.equal(question.yearProblemsHref, null);
	assert.equal(question.solutionHref, '/solutions/x/');
});

test('excludes sample pages without a four-digit exam year', () => {
	const entries = [{ slug: 'sample', data: { type: 'solution', university: 'ukyoto', category: 'kouki', year: 'sample', question: '1' } }];
	const result = buildTopicExplorer(entries, {}, '');
	assert.deepEqual(result.find((c) => c.id === 'ukyoto-kouki').decades, []);
});
