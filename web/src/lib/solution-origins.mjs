import { existsSync, readFileSync } from 'node:fs';
import { resolve } from 'node:path';
import yaml from 'js-yaml';

export const POST_HIGHSCHOOL_LABEL = '高校卒業後作成';

const DEFAULT_PATH = resolve('..', 'data', 'solution_origins.yaml');
let cachedConfig;

export function parseSolutionOrigins(raw = {}) {
	const yearFrom = typeof raw?.rules?.post_highschool_year_from === 'number'
		? raw.rules.post_highschool_year_from
		: null;
	const include = new Set(Array.isArray(raw?.post_highschool) ? raw.post_highschool : []);
	const exclude = new Set(Array.isArray(raw?.exclude) ? raw.exclude : []);
	return { yearFrom, include, exclude };
}

export function readSolutionOrigins(file = DEFAULT_PATH) {
	if (file === DEFAULT_PATH && cachedConfig) return cachedConfig;
	const raw = existsSync(file) ? (yaml.load(readFileSync(file, 'utf8')) || {}) : {};
	const config = parseSolutionOrigins(raw);
	if (file === DEFAULT_PATH) cachedConfig = config;
	return config;
}

export function isPostHighschoolSolution(data = {}, config = readSolutionOrigins()) {
	const { university, category, year, question, type } = data;
	if (type && type !== 'solution') return false;
	if (!question || String(question) === '0') return false;
	const uni = String(university || '').replace(/^sample_/, '');
	const id = `${uni}/${category}/${year}/${question}`;
	if (config.exclude.has(id)) return false;
	if (config.include.has(id)) return true;
	if (config.yearFrom !== null && /^\d{4}$/.test(String(year))) {
		return Number(year) >= config.yearFrom;
	}
	return false;
}
