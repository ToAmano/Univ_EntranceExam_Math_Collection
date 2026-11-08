import { readFileSync } from 'node:fs';
import { resolve } from 'node:path';

export const REPO = 'ToAmano/Univ_EntranceExam_Math_Collection';
export const REPO_URL = `https://github.com/${REPO}`;
const PROBLEM_ID = /^(utokyo|ukyoto|titech)\/(zenki|kouki)\/[0-9]{4}\/[1-9][0-9]*$/;
const VALID_UNIVS = new Set(['utokyo', 'ukyoto', 'titech']);
const VALID_EXAMS = new Set(['zenki', 'kouki']);
const VALID_KINDS = new Set(['proof', 'figure', 'reference', 'transcription', 'style']);

function isValidIssueCore(issue) {
  if (!issue || typeof issue !== 'object') return false;
  if (!Number.isSafeInteger(issue.number) || issue.number < 1 || typeof issue.title !== 'string') return false;
  if (!['open', 'closed'].includes(issue.state) || issue.url !== `${REPO_URL}/issues/${issue.number}`) return false;
  if (issue.kinds !== undefined) {
    if (!Array.isArray(issue.kinds) || issue.kinds.some(k => typeof k !== 'string' || !VALID_KINDS.has(k))) return false;
  }
  return true;
}

/** Read once per build, never once per page or from a visitor's browser. */
export function readIssueIndex(file = resolve('src/data/issues-by-problem.json')) {
  try {
    const index = JSON.parse(readFileSync(file, 'utf8'));
    if (index.schema_version !== 1 || index.repo !== REPO ||
        typeof index.generated_at !== 'string' || !Number.isFinite(Date.parse(index.generated_at)) ||
        !index.problems || typeof index.problems !== 'object' || Array.isArray(index.problems) ||
        !Array.isArray(index.rejected) || index.rejected.length) throw new Error('Invalid issue index');
    for (const [id, issues] of Object.entries(index.problems)) {
      if (!PROBLEM_ID.test(id) || !Array.isArray(issues)) throw new Error('Invalid problem mapping');
      for (const issue of issues) {
        if (!isValidIssueCore(issue)) throw new Error('Invalid issue entry');
      }
    }
    const unmapped = index.unmapped ?? [];
    if (!Array.isArray(unmapped)) throw new Error('Invalid unmapped list');
    for (const issue of unmapped) {
      if (!isValidIssueCore(issue)) throw new Error('Invalid unmapped issue entry');
      if (issue.univ !== null && issue.univ !== undefined && !VALID_UNIVS.has(issue.univ)) throw new Error('Invalid unmapped univ');
      if (issue.exam !== null && issue.exam !== undefined && !VALID_EXAMS.has(issue.exam)) throw new Error('Invalid unmapped exam');
    }
    return { available: true, generatedAt: index.generated_at, problems: index.problems, unmapped };
  } catch (error) {
    console.warn(`[issues] Snapshot unavailable: ${error.message}`);
    return { available: false, generatedAt: null, problems: {}, unmapped: [] };
  }
}

/** The page type is excluded from the identity: problem and solution share Issues. */
export function problemIssues(index, data) {
  const id = `${data.university}/${data.category}/${data.year}/${data.question}`;
  if (data.type === 'summary' || !PROBLEM_ID.test(id)) return null;
  const query = new URLSearchParams({ q: `is:issue is:open label:"problem:${id}"` });
  return {
    available: index.available,
    generatedAt: index.generatedAt,
    searchUrl: `${REPO_URL}/issues?${query}`,
    issues: (index.problems[id] || []).filter(i => i.state === 'open').sort((a, b) => a.number - b.number),
  };
}
