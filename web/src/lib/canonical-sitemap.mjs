import { readdirSync } from 'node:fs';

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
