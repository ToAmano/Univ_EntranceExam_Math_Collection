import test from 'node:test';
import assert from 'node:assert/strict';
import { buildArchiveSummary, buildIssueStats } from '../src/lib/issue-stats.mjs';
import { REPO_URL } from '../src/lib/issues.mjs';

const makeEntry = (university, category, year, question, type = 'solution') => ({
  slug: `${university}-${category}-${year}-${question}-${type}`,
  data: { university, category, year, question, type },
});

const sampleEntries = [
  makeEntry('utokyo', 'zenki', '1975', '1', 'problem'),
  makeEntry('utokyo', 'zenki', '1975', '1', 'solution'),
  makeEntry('utokyo', 'zenki', '1975', '2', 'problem'),
  makeEntry('utokyo', 'zenki', '2014', '1', 'solution'),
  makeEntry('utokyo', 'zenki', '2014', '0', 'summary'),
  makeEntry('utokyo', 'zenki', '2014', 'foo', 'solution'),
  makeEntry('sample_utokyo', 'zenki', '2020', '1', 'solution'),
  makeEntry('ukyoto', 'kouki', 'sample', '1', 'solution'),
  makeEntry('ukyoto', 'kouki', '1995', '1', 'solution'),
];

test('buildArchiveSummary deduplicates problem/solution pairs and ignores summaries and samples', () => {
  const summary = buildArchiveSummary(sampleEntries);
  assert.equal(summary.totalQuestions, 4);
  assert.deepEqual(summary.byUniversity, { utokyo: 3, ukyoto: 1, titech: 0 });
  assert.equal(summary.minYear, '1975');
  assert.equal(summary.maxYear, '2014');
  assert.equal(summary.zenkiYearCount, 2);
  assert.equal(summary.koukiYearCount, 1);
});

test('buildIssueStats aggregates single-problem, category-wide, general, and unrecorded-problem issues', () => {
  const index = {
    available: true,
    generatedAt: '2026-11-08T18:00:00Z',
    problems: {
      'utokyo/zenki/1975/1': [
        { number: 101, title: 'Proof & fig issue', state: 'open', url: `${REPO_URL}/issues/101`, updated_at: '2026-11-05T10:00:00Z', kinds: ['figure', 'proof'] },
        { number: 102, title: 'Second open issue', state: 'open', url: `${REPO_URL}/issues/102`, updated_at: '2026-11-06T10:00:00Z', kinds: [] },
        { number: 90, title: 'Closed issue', state: 'closed', url: `${REPO_URL}/issues/90`, updated_at: '2026-10-01T10:00:00Z', kinds: ['proof'] },
      ],
      'titech/kouki/1996/2': [
        { number: 11, title: '[TeX化] 東工大後期1996年 第2問', state: 'open', url: `${REPO_URL}/issues/11`, updated_at: '2026-07-22T00:00:00Z', kinds: ['transcription'] },
      ],
    },
    unmapped: [
      { number: 1408, title: '京大前期TikZ改修', state: 'open', url: `${REPO_URL}/issues/1408`, updated_at: '2026-11-07T00:00:00Z', kinds: ['figure'], univ: 'ukyoto', exam: 'zenki' },
      { number: 593, title: '横断タスク', state: 'open', url: `${REPO_URL}/issues/593`, updated_at: '2026-11-08T00:00:00Z', kinds: [], univ: null, exam: null },
      { number: 500, title: '完了済みCI改修', state: 'closed', url: `${REPO_URL}/issues/500`, updated_at: '2026-09-01T00:00:00Z', kinds: [], univ: null, exam: null },
    ],
  };

  const stats = buildIssueStats(index, sampleEntries, '/base');
  assert.equal(stats.available, true);
  assert.equal(stats.totals.open, 5);
  assert.equal(stats.totals.closed, 2);
  assert.equal(stats.totals.all, 7);
  assert.equal(stats.totals.problemOpen, 4);
  assert.equal(stats.totals.generalOpen, 1);
  assert.equal(stats.totals.completionRate, 28.6);
  assert.equal(stats.totals.openByKind.proof, 1);
  assert.equal(stats.totals.openByKind.figure, 2);
  assert.equal(stats.totals.openByKind.transcription, 1);
  assert.equal(stats.totals.openByKind.unclassified, 2);

  const utokyoZenki = stats.categories.find(c => c.id === 'utokyo-zenki');
  assert.equal(utokyoZenki.openCount, 2);
  assert.equal(utokyoZenki.closedCount, 1);
  const y1975 = utokyoZenki.decades.flatMap(d => d.years).find(y => y.year === '1975');
  assert.equal(y1975.questions[0].pageHref, '/base/solutions/utokyo-zenki-1975-1-solution/');
  assert.equal(y1975.questions[0].pageLabel, '解答ページ →');
  assert.equal(y1975.questions[0].openCount, 2);
  assert.deepEqual(y1975.questions[0].openByFilter, {
    all: 2,
    proof: 1,
    transcription: 0,
    figure: 1,
    other: 1,
  });
  assert.equal(y1975.questions[1].pageHref, '/base/solutions/utokyo-zenki-1975-2-problem/');
  assert.equal(y1975.questions[1].pageLabel, '問題ページ →');

  const ukyotoZenki = stats.categories.find(c => c.id === 'ukyoto-zenki');
  assert.equal(ukyotoZenki.openCount, 1);
  assert.equal(ukyotoZenki.openIssues[0].badge, '区分横断');

  const titechKouki = stats.categories.find(c => c.id === 'titech-kouki');
  assert.equal(titechKouki.openCount, 1);
  const y1996 = titechKouki.decades.flatMap(d => d.years).find(y => y.year === '1996');
  assert.equal(y1996.questions[0].question, '2');
  assert.equal(y1996.questions[0].recorded, false);
  assert.equal(y1996.questions[0].pageHref, null);

  const ukyotoKouki = stats.categories.find(c => c.id === 'ukyoto-kouki');
  assert.deepEqual(
    ukyotoKouki.decades.flatMap(d => d.years.map(y => y.year)),
    ['1995']
  );

  assert.equal(stats.general.openCount, 1);
  assert.equal(stats.general.closedCount, 1);
  assert.equal(stats.general.openIssues[0].number, 593);
});

test('buildIssueStats degrades gracefully when snapshot is unavailable', () => {
  const stats = buildIssueStats({ available: false, generatedAt: null, problems: {}, unmapped: [] }, sampleEntries, '');
  assert.equal(stats.available, false);
  assert.equal(stats.totals.completionRate, null);
  const utokyoZenki = stats.categories.find(c => c.id === 'utokyo-zenki');
  assert.equal(utokyoZenki.decades.flatMap(d => d.years).length, 2);
});
