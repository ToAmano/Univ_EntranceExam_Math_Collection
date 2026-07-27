export const UNIVERSITY_NAMES: Record<string, string> = {
	sample_utokyo: '東京大学',
	sample_titech: '東京工業大学',
	sample_ukyoto: '京都大学',
	utokyo: '東京大学',
	titech: '東京工業大学',
	ukyoto: '京都大学',
};

export const CATEGORY_NAMES: Record<string, string> = {
	zenki: '前期',
	kouki: '後期',
};

export function univName(id: string): string {
	return UNIVERSITY_NAMES[id] || id;
}

export function catName(id: string): string {
	return CATEGORY_NAMES[id] || id;
}
