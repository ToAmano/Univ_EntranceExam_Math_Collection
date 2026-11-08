import { REPO_URL } from './issues.mjs';

export const CATEGORIES = [
  {
    id: 'utokyo-zenki',
    university: 'utokyo',
    category: 'zenki',
    univName: '東京大学',
    catName: '前期 理系数学',
    shortLabel: '東大前期',
    color: '#ef4444',
    textAccent: '#fca5a5',
    gradient: 'linear-gradient(135deg, rgba(239, 68, 68, 0.16), rgba(15, 23, 42, 0.82))',
    border: 'rgba(239, 68, 68, 0.35)',
  },
  {
    id: 'ukyoto-zenki',
    university: 'ukyoto',
    category: 'zenki',
    univName: '京都大学',
    catName: '前期 理系数学',
    shortLabel: '京大前期',
    color: '#8b5cf6',
    textAccent: '#c4b5fd',
    gradient: 'linear-gradient(135deg, rgba(139, 92, 246, 0.16), rgba(15, 23, 42, 0.82))',
    border: 'rgba(139, 92, 246, 0.35)',
  },
  {
    id: 'titech-zenki',
    university: 'titech',
    category: 'zenki',
    univName: '東京工業大学',
    catName: '前期 理系数学',
    shortLabel: '東工大前期',
    color: '#10b981',
    textAccent: '#6ee7b7',
    gradient: 'linear-gradient(135deg, rgba(16, 185, 129, 0.16), rgba(15, 23, 42, 0.82))',
    border: 'rgba(16, 185, 129, 0.35)',
  },
  {
    id: 'utokyo-kouki',
    university: 'utokyo',
    category: 'kouki',
    univName: '東京大学',
    catName: '後期 理系数学',
    shortLabel: '東大後期',
    color: '#f43f5e',
    textAccent: '#fda4af',
    gradient: 'linear-gradient(135deg, rgba(244, 63, 94, 0.14), rgba(15, 23, 42, 0.82))',
    border: 'rgba(244, 63, 94, 0.3)',
  },
  {
    id: 'ukyoto-kouki',
    university: 'ukyoto',
    category: 'kouki',
    univName: '京都大学',
    catName: '後期 理系数学',
    shortLabel: '京大後期',
    color: '#a78bfa',
    textAccent: '#ddd6fe',
    gradient: 'linear-gradient(135deg, rgba(167, 139, 250, 0.14), rgba(15, 23, 42, 0.82))',
    border: 'rgba(167, 139, 250, 0.3)',
  },
  {
    id: 'titech-kouki',
    university: 'titech',
    category: 'kouki',
    univName: '東京工業大学',
    catName: '後期 理系数学',
    shortLabel: '東工大後期',
    color: '#34d399',
    textAccent: '#a7f3d0',
    gradient: 'linear-gradient(135deg, rgba(52, 211, 153, 0.14), rgba(15, 23, 42, 0.82))',
    border: 'rgba(52, 211, 153, 0.3)',
  },
];

export const KIND_META = [
  { key: 'proof', label: 'proof', jp: '論証・解答' },
  { key: 'transcription', label: 'transcription', jp: '文字起こし' },
  { key: 'figure', label: 'figure', jp: '図表・TikZ' },
  { key: 'reference', label: 'reference', jp: '相互参照' },
  { key: 'style', label: 'style', jp: '書式' },
];

const VALID_UNIVS = new Set(['utokyo', 'ukyoto', 'titech']);
const VALID_CATS = new Set(['zenki', 'kouki']);

function emptyKindCounts() {
  return { proof: 0, transcription: 0, figure: 0, reference: 0, style: 0, unclassified: 0 };
}

function addKinds(target, kinds = []) {
  if (!kinds || kinds.length === 0) {
    target.unclassified += 1;
    return;
  }
  for (const k of kinds) {
    if (k in target) target[k] += 1;
  }
}

function filterGroupsForKinds(kinds = []) {
  const groups = new Set();
  if (!kinds || kinds.length === 0) {
    groups.add('other');
  } else {
    for (const k of kinds) {
      if (k === 'proof' || k === 'transcription' || k === 'figure') groups.add(k);
      if (k === 'reference' || k === 'style') groups.add('other');
    }
  }
  return [...groups];
}

function calcRate(closed, open) {
  const all = closed + open;
  if (all === 0) return null;
  return Math.round((closed / all) * 1000) / 10;
}

function formatShortDate(iso) {
  if (!iso || typeof iso !== 'string') return null;
  const t = Date.parse(iso);
  if (!Number.isFinite(t)) return null;
  return new Date(t).toISOString().slice(0, 10);
}

const VALID_YEAR_RE = /^[0-9]{4}$/;
const VALID_QUESTION_RE = /^[1-9][0-9]*$/;

function isRealCatalogEntry(entry) {
  const d = entry?.data;
  if (!d) return false;
  if (!VALID_UNIVS.has(d.university) || !VALID_CATS.has(d.category)) return false;
  if (!VALID_YEAR_RE.test(String(d.year)) || !VALID_QUESTION_RE.test(String(d.question))) return false;
  if (d.type === 'summary') return false;
  return true;
}

export function buildArchiveSummary(allEntries = []) {
  const seenQuestions = new Set();
  const byUniversity = { utokyo: 0, ukyoto: 0, titech: 0 };
  const zenkiYears = new Set();
  const koukiYears = new Set();
  let minYear = null;
  let maxYear = null;

  for (const entry of allEntries) {
    if (!isRealCatalogEntry(entry)) continue;
    const { university, category, year, question } = entry.data;
    const key = `${university}/${category}/${year}/${question}`;
    if (!seenQuestions.has(key)) {
      seenQuestions.add(key);
      byUniversity[university] += 1;
    }
    if (category === 'zenki') zenkiYears.add(year);
    if (category === 'kouki') koukiYears.add(year);
    if (minYear === null || year < minYear) minYear = year;
    if (maxYear === null || year > maxYear) maxYear = year;
  }

  return {
    totalQuestions: seenQuestions.size,
    byUniversity,
    minYear,
    maxYear,
    zenkiYearCount: zenkiYears.size,
    koukiYearCount: koukiYears.size,
  };
}

export function buildIssueStats(index, allEntries = [], baseUrl = '') {
  const cleanBase = baseUrl.replace(/\/$/, '');
  const catalogMap = new Map();

  for (const entry of allEntries) {
    if (!isRealCatalogEntry(entry)) continue;
    const { university, category, year, question, type } = entry.data;
    const id = `${university}/${category}/${year}/${question}`;
    const rec = catalogMap.get(id) || { solutionSlug: null, problemSlug: null };
    if (type === 'solution') rec.solutionSlug = entry.slug;
    else if (type === 'problem') rec.problemSlug = entry.slug;
    catalogMap.set(id, rec);
  }

  const catWideByKey = new Map();
  const generalOpenIssues = [];
  let generalClosedCount = 0;

  for (const item of index.unmapped || []) {
    if (item.univ && item.exam) {
      const catKey = `${item.univ}-${item.exam}`;
      if (!catWideByKey.has(catKey)) catWideByKey.set(catKey, []);
      catWideByKey.get(catKey).push(item);
    } else if (item.state === 'open') {
      generalOpenIssues.push({
        number: item.number,
        title: item.title,
        url: item.url,
        updatedDate: formatShortDate(item.updated_at),
        kinds: item.kinds || [],
      });
    } else {
      generalClosedCount += 1;
    }
  }
  generalOpenIssues.sort((a, b) => b.number - a.number);

  const globalOpenByKind = emptyKindCounts();
  for (const gi of generalOpenIssues) addKinds(globalOpenByKind, gi.kinds);

  let totalProblemOpen = 0;
  let totalProblemClosed = 0;

  const categories = CATEGORIES.map(cfg => {
    const prefix = `${cfg.university}/${cfg.category}/`;
    const yearMap = new Map();

    const ensureCell = (year, question) => {
      if (!yearMap.has(year)) yearMap.set(year, new Map());
      const qMap = yearMap.get(year);
      if (!qMap.has(question)) qMap.set(question, { question, catalog: null, issues: [] });
      return qMap.get(question);
    };

    for (const [id, rec] of catalogMap.entries()) {
      if (!id.startsWith(prefix)) continue;
      const [, , year, question] = id.split('/');
      ensureCell(year, question).catalog = rec;
    }

    for (const [id, issues] of Object.entries(index.problems || {})) {
      if (!id.startsWith(prefix)) continue;
      const [, , year, question] = id.split('/');
      ensureCell(year, question).issues = issues;
    }

    const catOpenByKind = emptyKindCounts();
    let catOpenCount = 0;
    let catClosedCount = 0;
    const catOpenIssues = [];

    for (const cw of catWideByKey.get(cfg.id) || []) {
      if (cw.state === 'open') {
        const ks = cw.kinds || [];
        catOpenCount += 1;
        addKinds(catOpenByKind, ks);
        addKinds(globalOpenByKind, ks);
        catOpenIssues.push({
          scope: 'category',
          problemKey: null,
          year: null,
          question: null,
          badge: '区分横断',
          number: cw.number,
          title: cw.title,
          url: cw.url,
          updatedDate: formatShortDate(cw.updated_at),
          kinds: ks,
          filterGroups: filterGroupsForKinds(ks),
          pageHref: null,
          pageLabel: null,
        });
      } else {
        catClosedCount += 1;
      }
    }

    const sortedYears = [...yearMap.keys()].sort((a, b) => b.localeCompare(a));
    const decadeMap = new Map();

    for (const year of sortedYears) {
      const qMap = yearMap.get(year);
      const sortedQs = [...qMap.values()].sort((a, b) =>
        a.question.localeCompare(b.question, undefined, { numeric: true })
      );

      let yearOpenCount = 0;
      const questions = sortedQs.map(cell => {
        const openList = cell.issues.filter(i => i.state === 'open');
        const closedCount = cell.issues.length - openList.length;
        catOpenCount += openList.length;
        catClosedCount += closedCount;
        yearOpenCount += openList.length;

        const recorded = Boolean(cell.catalog?.solutionSlug || cell.catalog?.problemSlug);
        const pageHref = cell.catalog?.solutionSlug
          ? `${cleanBase}/solutions/${cell.catalog.solutionSlug}/`
          : cell.catalog?.problemSlug
            ? `${cleanBase}/solutions/${cell.catalog.problemSlug}/`
            : null;
        const pageLabel = cell.catalog?.solutionSlug
          ? '解答ページ →'
          : cell.catalog?.problemSlug
            ? '問題ページ →'
            : null;

        const problemKey = `${year}/${cell.question}`;
        const cellOpenByFilter = { all: openList.length, proof: 0, transcription: 0, figure: 0, other: 0 };

        for (const iss of openList) {
          const ks = iss.kinds || [];
          const groups = filterGroupsForKinds(ks);
          addKinds(catOpenByKind, ks);
          addKinds(globalOpenByKind, ks);
          for (const g of groups) cellOpenByFilter[g] += 1;

          catOpenIssues.push({
            scope: 'problem',
            problemKey,
            year,
            question: cell.question,
            badge: `${year}年 第${cell.question}問`,
            number: iss.number,
            title: iss.title,
            url: iss.url,
            updatedDate: formatShortDate(iss.updated_at),
            kinds: ks,
            filterGroups: groups,
            pageHref,
            pageLabel,
          });
        }

        return {
          question: cell.question,
          problemKey,
          recorded,
          pageHref,
          pageLabel,
          openCount: openList.length,
          closedCount,
          openByFilter: cellOpenByFilter,
        };
      });

      const decadeLabel = `${year.slice(0, 3)}0s`;
      if (!decadeMap.has(decadeLabel)) decadeMap.set(decadeLabel, []);
      decadeMap.get(decadeLabel).push({ year, openCount: yearOpenCount, questions });
    }

    totalProblemOpen += catOpenCount;
    totalProblemClosed += catClosedCount;

    const searchQuery = new URLSearchParams({
      q: `is:issue is:open label:"univ:${cfg.university}" label:"exam:${cfg.category}"`,
    });

    return {
      ...cfg,
      openCount: catOpenCount,
      closedCount: catClosedCount,
      completionRate: index.available ? calcRate(catClosedCount, catOpenCount) : null,
      openByKind: catOpenByKind,
      githubSearchUrl: `${REPO_URL}/issues?${searchQuery}`,
      decades: [...decadeMap.entries()].map(([label, years]) => ({ label, years })),
      openIssues: catOpenIssues,
    };
  });

  const totalOpen = totalProblemOpen + generalOpenIssues.length;
  const totalClosed = totalProblemClosed + generalClosedCount;
  const totalAll = totalOpen + totalClosed;

  const generalQuery = new URLSearchParams({
    q: 'is:issue is:open -label:univ:utokyo -label:univ:ukyoto -label:univ:titech',
  });

  return {
    available: Boolean(index.available),
    generatedAt: index.generatedAt || null,
    repoIssuesUrl: `${REPO_URL}/issues`,
    totals: {
      open: totalOpen,
      closed: totalClosed,
      all: totalAll,
      completionRate: index.available ? calcRate(totalClosed, totalOpen) : null,
      problemOpen: totalProblemOpen,
      generalOpen: generalOpenIssues.length,
      openByKind: globalOpenByKind,
    },
    categories,
    general: {
      openCount: generalOpenIssues.length,
      closedCount: generalClosedCount,
      githubSearchUrl: `${REPO_URL}/issues?${generalQuery}`,
      openIssues: generalOpenIssues,
    },
  };
}
