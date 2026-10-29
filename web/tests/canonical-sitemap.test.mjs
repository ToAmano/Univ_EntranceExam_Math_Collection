import test from 'node:test';
import assert from 'node:assert/strict';
import { mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
import { matchingSolutionSlug, solutionSlugsFromMarkdown, includeInSitemap, createSitemapSerializer } from '../src/lib/canonical-sitemap.mjs';

const root = 'https://toamano.github.io/Univ_EntranceExam_Math_Collection/';

test('problem canonical and sitemap use the same solution lookup', () => {
  const solutions = new Set(['utokyo-zenki-2000-1-solution']);
  assert.equal(matchingSolutionSlug('utokyo-zenki-2000-1-problem', solutions), 'utokyo-zenki-2000-1-solution');
  assert.equal(includeInSitemap(root + 'solutions/utokyo-zenki-2000-1-problem/', solutions), false);
  assert.equal(includeInSitemap(root + 'solutions/utokyo-zenki-2000-1-solution/', solutions), true);
  assert.equal(matchingSolutionSlug('utokyo-zenki-2000-2-problem', solutions), null);
  assert.equal(includeInSitemap(root + 'solutions/utokyo-zenki-2000-2-problem/', solutions), true);
});

test('summaries and other public routes remain in the sitemap', () => {
  const solutions = new Set(['utokyo-zenki-2000-1-solution']);
  for (const route of ['', 'category/utokyo/zenki/', 'tags/', 'solutions/utokyo-zenki-2000-0-summary/']) {
    assert.equal(includeInSitemap(root + route, solutions), true);
  }
  assert.equal(includeInSitemap(root + 'category/sample_utokyo/zenki/', solutions), false);
});

test('new or removed solution markdown changes the next build without manual URL lists', () => {
  const dir = mkdtempSync(join(tmpdir(), 'math-sitemap-'));
  try {
    writeFileSync(join(dir, 'utokyo-zenki-2000-1-problem.md'), '');
    assert.equal(solutionSlugsFromMarkdown(dir).size, 0);
    writeFileSync(join(dir, 'utokyo-zenki-2000-1-solution.md'), '');
    const solutions = solutionSlugsFromMarkdown(dir);
    assert.equal(solutions.has('utokyo-zenki-2000-1-solution'), true);
    assert.equal(includeInSitemap(root + 'solutions/utokyo-zenki-2000-1-problem/', solutions), false);
    rmSync(join(dir, 'utokyo-zenki-2000-1-solution.md'));
    assert.equal(includeInSitemap(root + 'solutions/utokyo-zenki-2000-1-problem/', solutionSlugsFromMarkdown(dir)), true);
  } finally {
    rmSync(dir, { recursive: true, force: true });
  }
});

test('sitemap serializer attaches valid lastmod Date to each item', () => {
  const dummyData = {
    slugDateMap: new Map([['utokyo-zenki-2000-1-solution', new Date('2026-05-01T00:00:00Z')]]),
    yearDateMap: new Map([['utokyo-zenki-2000', new Date('2026-05-01T00:00:00Z')]]),
    catDateMap: new Map([['utokyo/zenki', new Date('2026-05-01T00:00:00Z')]]),
    latestDate: new Date('2026-04-01T00:00:00Z'),
  };
  const serialize = createSitemapSerializer(dummyData);

  const solItem = serialize({ url: root + 'solutions/utokyo-zenki-2000-1-solution/' });
  assert.equal(solItem.lastmod.toISOString(), '2026-05-01T00:00:00.000Z');

  const sumItem = serialize({ url: root + 'solutions/utokyo-zenki-2000-0-summary/' });
  assert.equal(sumItem.lastmod.toISOString(), '2026-05-01T00:00:00.000Z');

  const catItem = serialize({ url: root + 'category/utokyo/zenki/' });
  assert.equal(catItem.lastmod.toISOString(), '2026-05-01T00:00:00.000Z');

  const rootItem = serialize({ url: root });
  assert.equal(rootItem.lastmod.toISOString(), '2026-04-01T00:00:00.000Z');
});
