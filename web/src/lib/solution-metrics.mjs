import fs from 'node:fs';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

function getDefaultPath() {
	// Check common execution contexts (web/ cwd vs repo-root cwd vs module-relative)
	const candidates = [
		resolve('src/data/solution-metrics.json'),
		resolve('web/src/data/solution-metrics.json'),
		fileURLToPath(new URL('../data/solution-metrics.json', import.meta.url)),
	];
	for (const p of candidates) {
		if (fs.existsSync(p)) {
			return p;
		}
	}
	return candidates[0];
}

export const CATEGORY_META = {
	utokyo_zenki: {
		label: '東大前期',
		shortLabel: '東大前',
		color: '#1d4ed8',
		lightColor: '#dbeafe',
	},
	utokyo_kouki: {
		label: '東大後期',
		shortLabel: '東大後',
		color: '#2563eb',
		lightColor: '#eff6ff',
	},
	ukyoto_zenki: {
		label: '京大前期',
		shortLabel: '京大前',
		color: '#047857',
		lightColor: '#d1fae5',
	},
	ukyoto_kouki: {
		label: '京大後期',
		shortLabel: '京大後',
		color: '#059669',
		lightColor: '#ecfdf5',
	},
	titech_zenki: {
		label: '東工大前期',
		shortLabel: '東工前',
		color: '#b45309',
		lightColor: '#fef3c7',
	},
	titech_kouki: {
		label: '東工大後期',
		shortLabel: '東工後',
		color: '#d97706',
		lightColor: '#fffbeb',
	},
};

/**
 * Read and validate build-time solution metrics JSON snapshot.
 *
 * @param {string} [filePath]
 * @returns {{ available: boolean, data: any | null }}
 */
export function readSolutionMetrics(filePath) {
	try {
		const targetPath = filePath || getDefaultPath();
		if (!fs.existsSync(targetPath)) {
			return { available: false, data: null };
		}
		const raw = fs.readFileSync(targetPath, 'utf-8');
		const data = JSON.parse(raw);

		if (!data || data.schema_version !== 1 || !data.overall || !data.categories) {
			return { available: false, data: null };
		}

		return { available: true, data };
	} catch (err) {
		console.warn('[readSolutionMetrics] Failed to load metrics:', err);
		return { available: false, data: null };
	}
}

/**
 * Return display metadata for a category key.
 *
 * @param {string} catKey
 * @returns {{ label: string, shortLabel: string, color: string, lightColor: string }}
 */
export function getCategoryMeta(catKey) {
	return (
		CATEGORY_META[catKey] || {
			label: catKey,
			shortLabel: catKey,
			color: '#4b5563',
			lightColor: '#f3f4f6',
		}
	);
}

/**
 * Build canonical solution page URL for a given problem item.
 *
 * @param {string} baseUrl
 * @param {{ univ: string, exam: string, year: number | string, question: string }} item
 * @returns {string}
 */
export function buildProblemUrl(baseUrl, item) {
	const cleanBase = baseUrl.endsWith('/') ? baseUrl : `${baseUrl}/`;
	return `${cleanBase}solutions/${item.univ}-${item.exam}-${item.year}-${item.question}-solution/`;
}
