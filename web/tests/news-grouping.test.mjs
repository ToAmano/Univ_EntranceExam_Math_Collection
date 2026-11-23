import assert from 'node:assert/strict';
import test from 'node:test';
import {
	aggregateAutoNews,
	resolveNewsProblemHref,
	resolveNewsYearHref,
} from '../src/lib/news-grouping.mjs';

const item = (question, action = 'updated', year = '1962') => ({
	university: 'utokyo', category: 'zenki', year, question, action,
});
const entry = (date, ...items) => ({ date, items });

test('repeated commits for the same date and problem produce one displayed question', () => {
	const days = aggregateAutoNews([
		entry('2026-11-12', item('2')),
		entry('2026-11-12', item('2'), item('3')),
	]);
	assert.equal(days.length, 1);
	assert.deepEqual(days[0].items.map((question) => question.question), ['2', '3']);
	assert.deepEqual(days[0].groups[0].questions, ['2', '3']);
});

test('an added problem updated later that day remains an addition', () => {
	const days = aggregateAutoNews([
		entry('2026-11-12', item('2', 'updated')),
		entry('2026-11-12', item('2', 'added')),
	]);
	assert.equal(days[0].items[0].action, 'added');
	assert.equal(days[0].groups[0].action, 'added');
});

test('daily summaries and detailed groups keep distinct years and actions', () => {
	const days = aggregateAutoNews([
		entry('2026-11-13', item('1', 'updated', '1963')),
		entry('2026-11-12', item('2'), item('3'), item('1', 'added', '1964')),
	]);
	assert.deepEqual(days.map((day) => day.date), ['2026-11-13', '2026-11-12']);
	assert.equal(days[1].items.length, 3);
	assert.deepEqual(days[1].groups.map((group) => [group.year, group.action, group.questions]), [
		['1962', 'updated', ['2', '3']],
		['1964', 'added', ['1']],
	]);
});

test('a daily digest leads with a real question when a summary file changed too', () => {
	const days = aggregateAutoNews([
		entry('2026-11-12', item('0'), item('2')),
	]);
	assert.equal(days[0].lead.question, '2');
	assert.equal(days[0].items.length, 2);
});

test('resolveNewsProblemHref resolves existing solution, summary, year fallback, or undefined', () => {
	const slugs = new Set([
		'utokyo-zenki-1962-1-solution',
		'utokyo-zenki-1962-0-summary',
	]);
	const years = new Set([
		'utokyo/zenki/1962',
		'utokyo/zenki/1963',
	]);
	assert.equal(
		resolveNewsProblemHref({ university: 'utokyo', category: 'zenki', year: '1962', question: '1' }, slugs, years),
		'/solutions/utokyo-zenki-1962-1-solution/',
	);
	assert.equal(
		resolveNewsProblemHref({ university: 'utokyo', category: 'zenki', year: '1962', question: '0' }, slugs, years),
		'/solutions/utokyo-zenki-1962-0-summary/',
	);
	assert.equal(
		resolveNewsProblemHref({ university: 'utokyo', category: 'zenki', year: '1963', question: '2' }, slugs, years),
		'/problems/utokyo/zenki/1963/#q2',
	);
	assert.equal(
		resolveNewsProblemHref({ university: 'utokyo', category: 'zenki', year: '1999', question: '1' }, slugs, years),
		undefined,
	);
	assert.equal(resolveNewsYearHref('utokyo', 'zenki', '1962', years), '/problems/utokyo/zenki/1962/');
	assert.equal(resolveNewsYearHref('utokyo', 'zenki', '1999', years), undefined);
});
