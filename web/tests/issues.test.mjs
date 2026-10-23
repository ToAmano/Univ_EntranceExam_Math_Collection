import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { readIssueIndex, problemIssues } from '../src/lib/issues.mjs';

const repo = 'ToAmano/Univ_EntranceExam_Math_Collection';
const row = (number, state = 'open') => ({ number, state, title: `Issue ${number}`, url: `https://github.com/${repo}/issues/${number}` });
const data = { university: 'titech', category: 'zenki', year: '1985', question: '3', type: 'solution' };
function withSnapshot(value, fn) {
  const dir = mkdtempSync(join(tmpdir(), 'math-issues-'));
  try {
    const file = join(dir, 'issues.json');
    if (value !== undefined) writeFileSync(file, typeof value === 'string' ? value : JSON.stringify(value));
    return fn(readIssueIndex(file));
  } finally { rmSync(dir, { recursive: true, force: true }); }
}
const snapshot = () => ({ schema_version: 1, repo, generated_at: '2026-10-21T22:00:00Z', rejected: [], problems: {
  'titech/zenki/1985/3': [row(3), row(1, 'closed'), row(2)],
  'utokyo/zenki/1985/3': [row(4)],
} });

test('both page types use the same exact problem and only open Issues', () => withSnapshot(snapshot(), index => {
  const solution = problemIssues(index, data);
  const problem = problemIssues(index, { ...data, type: 'problem' });
  assert.deepEqual(solution, problem);
  assert.deepEqual(solution.issues.map(i => i.number), [2, 3]);
  const query = new URL(solution.searchUrl).searchParams.get('q');
  assert.equal(query, 'is:issue is:open label:"problem:titech/zenki/1985/3"');
  assert.equal(solution.generatedAt, '2026-10-21T22:00:00Z');
}));

test('a known empty list differs from unavailable data', () => {
  withSnapshot(snapshot(), index => {
    const result = problemIssues(index, { ...data, question: '4' });
    assert.equal(result.available, true);
    assert.deepEqual(result.issues, []);
  });
  for (const value of [undefined, '{broken', { ...snapshot(), repo: 'other/repo' }, { ...snapshot(), schema_version: 2 }]) {
    withSnapshot(value, index => assert.equal(problemIssues(index, data).available, false));
  }
});

test('summary and noncanonical question IDs have no issue section', () => withSnapshot(snapshot(), index => {
  for (const change of [{ question: '0' }, { type: 'summary' }, { question: '03' }, { university: 'sample_titech' }])
    assert.equal(problemIssues(index, { ...data, ...change }), null);
}));

test('invalid or rejected mappings are unavailable rather than silently empty', () => {
  for (const mutate of [
    s => { s.problems['titech/zenki/1985/3'][0].url = 'javascript:alert(1)'; },
    s => { s.problems['titech/zenki/1985/3'][0].state = 'unknown'; },
    s => { s.generated_at = 'invalid'; },
    s => { s.rejected.push({ number: 8 }); },
  ]) {
    const s = snapshot(); mutate(s);
    withSnapshot(s, index => assert.equal(problemIssues(index, data).available, false));
  }
});
