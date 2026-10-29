import { readdirSync } from 'node:fs';
import { execSync } from 'node:child_process';
import { fileURLToPath } from 'node:url';

/** The generated Markdown filenames are the slugs used by Astro content. */
export function solutionSlugsFromMarkdown(directory) {
  return new Set(readdirSync(directory)
    .filter(name => name.endsWith('-solution.md'))
    .map(name => name.slice(0, -'.md'.length)));
}

/** Return a problem page's canonical solution only when that page exists. */
export function matchingSolutionSlug(problemSlug, solutionSlugs) {
  if (!problemSlug.endsWith('-problem')) return null;
  const candidate = `${problemSlug.slice(0, -'-problem'.length)}-solution`;
  return solutionSlugs.has(candidate) ? candidate : null;
}

/** Sitemap exclusion uses the same lookup as the problem page canonical. */
export function includeInSitemap(page, solutionSlugs) {
  const pathname = new URL(page).pathname;
  if (pathname.split('/').some(segment => segment.startsWith('sample_'))) return false;
  const match = pathname.match(/\/solutions\/([^/]+)\/?$/);
  if (!match) return true;
  return matchingSolutionSlug(decodeURIComponent(match[1]), solutionSlugs) === null;
}

/**
 * Build git-based lastmod lookup tables so that each sitemap URL has an accurate <lastmod>.
 * - Individual questions: commit date of the corresponding solution.tex / problem.tex
 * - Summary pages: latest commit date among questions for that year
 * - Category pages: latest commit date among questions for that university/category
 * - Root / others: latest commit date in repository
 */
export function buildLastmodData() {
  const slugDateMap = new Map();
  const yearDateMap = new Map();
  const catDateMap = new Map();
  let latestDate = new Date();
  const repoRoot = fileURLToPath(new URL('../../..', import.meta.url));

  try {
    const latestStdout = execSync('git log -1 --format=%cI', {
      cwd: repoRoot,
      encoding: 'utf-8',
      stdio: ['ignore', 'pipe', 'ignore'],
    }).trim();
    if (latestStdout) latestDate = new Date(latestStdout);

    const stdout = execSync('git log --format=%cI --name-only -- ":/:src/*/*/*/*/*.tex"', {
      cwd: repoRoot,
      encoding: 'utf-8',
      stdio: ['ignore', 'pipe', 'ignore'],
    });
    let currentDate = null;
    for (const line of stdout.split('\n')) {
      const trimmed = line.trim();
      if (!trimmed) continue;
      if (trimmed.includes('T') && (trimmed.includes('+') || trimmed.includes('-') || trimmed.endsWith('Z'))) {
        currentDate = new Date(trimmed);
      } else if (trimmed.startsWith('src/')) {
        const parts = trimmed.split('/');
        if (parts.length === 6) {
          const [ , univ, cat, year, q, filename ] = parts;
          const type = filename.replace(/\.tex$/, '');
          const slug = `${univ}-${cat}-${year}-${q}-${type}`;
          if (!slugDateMap.has(slug)) {
            slugDateMap.set(slug, currentDate);
          }
          const yearKey = `${univ}-${cat}-${year}`;
          if (!yearDateMap.has(yearKey) || yearDateMap.get(yearKey) < currentDate) {
            yearDateMap.set(yearKey, currentDate);
          }
          const catKey = `${univ}/${cat}`;
          if (!catDateMap.has(catKey) || catDateMap.get(catKey) < currentDate) {
            catDateMap.set(catKey, currentDate);
          }
        }
      }
    }
  } catch {
    // If git fails, fallback to current time
  }

  return { slugDateMap, yearDateMap, catDateMap, latestDate };
}

/**
 * Returns a serialize function for @astrojs/sitemap that attaches lastmod to each item.
 */
export function createSitemapSerializer(lastmodData = buildLastmodData()) {
  const { slugDateMap, yearDateMap, catDateMap, latestDate } = lastmodData;

  return function serializeSitemapItem(item) {
    const url = new URL(item.url);
    const pathname = url.pathname;

    // Individual solution or summary pages: .../solutions/{slug}/
    const solMatch = pathname.match(/\/solutions\/([^/]+)\/?$/);
    if (solMatch) {
      const slug = decodeURIComponent(solMatch[1]);
      if (slugDateMap.has(slug)) {
        item.lastmod = slugDateMap.get(slug);
        return item;
      }
      const sumMatch = slug.match(/^([a-z_]+-[a-z]+-\d{4})-0-summary$/);
      if (sumMatch && yearDateMap.has(sumMatch[1])) {
        item.lastmod = yearDateMap.get(sumMatch[1]);
        return item;
      }
      item.lastmod = latestDate;
      return item;
    }

    // Category pages: .../category/{univ}/{cat}/
    const catMatch = pathname.match(/\/category\/([^/]+)\/([^/]+)\/?$/);
    if (catMatch) {
      const catKey = `${catMatch[1]}/${catMatch[2]}`;
      if (catDateMap.has(catKey)) {
        item.lastmod = catDateMap.get(catKey);
        return item;
      }
      item.lastmod = latestDate;
      return item;
    }

    item.lastmod = latestDate;
    return item;
  };
}
