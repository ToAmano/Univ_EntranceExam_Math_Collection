import test from 'node:test';
import assert from 'node:assert/strict';
import { readProblemGroups, relatedProblemGroups } from '../src/lib/related-problems.mjs';

const entry = (id, type = 'solution') => {
  const [university, category, year, question] = id.split('/');
  return {
    slug: `${university}-${category}-${year}-${question}-${type}`,
    data: { university, category, year, question, type },
  };
};

const groups = [{
  id: 'integral', name: '積分',
  problems: ['titech/kouki/1992/1', 'titech/zenki/1984/4'],
  related: ['titech/zenki/1978/6'],
}];
const entries = [
  entry('titech/kouki/1992/1'),
  entry('titech/zenki/1984/4', 'problem'),
  entry('titech/zenki/1984/4'),
  entry('titech/zenki/1978/6'),
];

test('a member sees other questions once, preferring solution pages and marking related questions', () => {
  const result = relatedProblemGroups(groups, 'titech/kouki/1992/1', entries);
  assert.deepEqual(result, [{
    id: 'integral', name: '積分',
    items: [
      { id: 'titech/zenki/1984/4', slug: 'titech-zenki-1984-4-solution', relation: 'same' },
      { id: 'titech/zenki/1978/6', slug: 'titech-zenki-1978-6-solution', relation: 'related' },
    ],
  }]);
});

test('related members can navigate to core questions, while unknown questions get no section', () => {
  const result = relatedProblemGroups(groups, 'titech/zenki/1978/6', entries);
  assert.deepEqual(result[0].items.map(item => item.id), ['titech/kouki/1992/1', 'titech/zenki/1984/4']);
  assert.deepEqual(relatedProblemGroups(groups, 'utokyo/zenki/2000/1', entries), []);
});

test('the site reads the curated catalog with its stable IDs and display names', () => {
  const catalog = readProblemGroups();
  assert.equal(catalog.find(group => group.id === 'chebyshev_polynomials')?.name, 'チェビシフ多項式');
  assert.ok(catalog.find(group => group.id === 'oscillatory_integrals')?.related.includes('titech/zenki/1994/3'));
});
