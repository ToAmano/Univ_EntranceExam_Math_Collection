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
    creation: 0,
    transcription: 0,
    figure: 1,
    other: 1,
  });
  assert.equal(y1975.questions[1].pageHref, '/base/problems/utokyo/zenki/1975/#q2');
  assert.equal(y1975.questions[1].pageLabel, '問題一覧 →');

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
  assert.equal(stats.closedTrendsMeta.hasAnyClosedData, false);
  const utokyoZenki = stats.categories.find(c => c.id === 'utokyo-zenki');
  assert.equal(utokyoZenki.decades.flatMap(d => d.years).length, 2);
  assert.deepEqual(utokyoZenki.closedTrend.dailySeries, []);
});

test('buildIssueStats computes JST daily (30d) and full-range cumulative closed issue trends per category', () => {
  const index = {
    available: true,
    generatedAt: '2026-11-19T12:00:00Z', // 2026-11-19 21:00 JST
    problems: {
      'utokyo/zenki/1975/1': [
        // closed_at takes precedence over updated_at; 2026-10-01T16:00Z = 2026-10-02 01:00 JST (outside 30d window)
        { number: 1, title: 'Old close', state: 'closed', url: `${REPO_URL}/issues/1`, updated_at: '2026-11-18T00:00:00Z', closed_at: '2026-10-01T16:00:00Z', kinds: [] },
        // 2026-11-18T15:30Z = 2026-11-19 00:30 JST
        { number: 2, title: 'Midnight JST close', state: 'closed', url: `${REPO_URL}/issues/2`, updated_at: '2026-11-18T15:30:00Z', closed_at: '2026-11-18T15:30:00Z', kinds: [] },
        { number: 3, title: 'Still open', state: 'open', url: `${REPO_URL}/issues/3`, updated_at: '2026-11-19T00:00:00Z', closed_at: null, kinds: [] },
      ],
      'ukyoto/zenki/2001/1': [
        // fallback to updated_at when closed_at is omitted
        { number: 4, title: 'Legacy closed', state: 'closed', url: `${REPO_URL}/issues/4`, updated_at: '2026-11-17T05:00:00Z', kinds: [] },
      ],
    },
    unmapped: [
      { number: 5, title: '京大前期まとめ完了', state: 'closed', url: `${REPO_URL}/issues/5`, updated_at: '2026-11-19T01:00:00Z', closed_at: '2026-11-19T01:00:00Z', kinds: ['figure'], univ: 'ukyoto', exam: 'zenki' },
    ],
  };

  const stats = buildIssueStats(index, sampleEntries, '');
  assert.equal(stats.closedTrendsMeta.recentDays, 30);
  assert.equal(stats.closedTrendsMeta.cumulativeStartDate, '2026-10-02');
  assert.equal(stats.closedTrendsMeta.dailyStartDate, '2026-10-21');
  assert.equal(stats.closedTrendsMeta.endDate, '2026-11-19');
  assert.equal(stats.closedTrendsMeta.hasAnyClosedData, true);

  const utokyoZenki = stats.categories.find(c => c.id === 'utokyo-zenki');
  assert.equal(utokyoZenki.closedTrend.dailySeries.length, 30);
  assert.equal(utokyoZenki.closedTrend.cumulativeSeries.length, 49); // 2026-10-02..2026-11-19 inclusive
  assert.equal(utokyoZenki.closedTrend.recentTotal, 1);
  assert.equal(utokyoZenki.closedTrend.cumulativeTotal, 2);
  assert.equal(utokyoZenki.closedTrend.dailySeries[0].cumulative, 1); // includes pre-window close on 10/02
  assert.equal(utokyoZenki.closedTrend.dailySeries.at(-1).date, '2026-11-19');
  assert.equal(utokyoZenki.closedTrend.dailySeries.at(-1).count, 1);
  assert.equal(utokyoZenki.closedTrend.dailySeries.at(-1).cumulative, 2);

  const ukyotoZenki = stats.categories.find(c => c.id === 'ukyoto-zenki');
  assert.equal(ukyotoZenki.closedTrend.recentTotal, 2);
  assert.equal(ukyotoZenki.closedTrend.cumulativeTotal, 2);
});

test('buildIssueStats isolates solution creation issues into creation category exclusively', () => {
  const index = {
    available: true,
    generatedAt: '2026-11-21T00:00:00Z',
    problems: {
      'utokyo/zenki/1975/1': [
        { number: 201, title: '[解答作成] 東大前期1975-1：解答を新規作成', state: 'open', url: `${REPO_URL}/issues/201`, updated_at: '2026-11-20T00:00:00Z', kinds: ['proof', 'transcription'] },
        { number: 202, title: '[監査] 東大前期1975-1：論証修正', state: 'open', url: `${REPO_URL}/issues/202`, updated_at: '2026-11-20T00:00:00Z', kinds: ['proof'] },
      ],
      'ukyoto/kouki/1995/1': [
        { number: 203, title: '京大後期1995-1：新設問の解答', state: 'open', url: `${REPO_URL}/issues/203`, updated_at: '2026-11-20T00:00:00Z', kinds: ['creation'] },
      ],
    },
    unmapped: [],
  };

  const stats = buildIssueStats(index, sampleEntries, '');
  assert.equal(stats.totals.openByKind.creation, 2);
  assert.equal(stats.totals.openByKind.proof, 1);
  assert.equal(stats.totals.openByKind.transcription, 0);

  const utokyoZenki = stats.categories.find(c => c.id === 'utokyo-zenki');
  assert.equal(utokyoZenki.openByKind.creation, 1);
  assert.equal(utokyoZenki.openByKind.proof, 1);
  assert.equal(utokyoZenki.openByKind.transcription, 0);
  const y1975 = utokyoZenki.decades.flatMap(d => d.years).find(y => y.year === '1975');
  assert.deepEqual(y1975.questions[0].openByFilter, {
    all: 2,
    proof: 1,
    creation: 1,
    transcription: 0,
    figure: 0,
    other: 0,
  });
  const issue201 = utokyoZenki.openIssues.find(i => i.number === 201);
  assert.deepEqual(issue201.kinds, ['creation']);
  assert.deepEqual(issue201.filterGroups, ['creation']);
});
