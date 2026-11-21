/** Muted topic colors shared by the chart and question matrix on the dark site theme. */
export const TOPIC_COLORS = {
	'積分': { color: '#6f95d2', border: '#8ba8d6' },
	'方程式・不等式': { color: '#9085d2', border: '#a29dd6' },
	'微分': { color: '#58abc4', border: '#7ab8cd' },
	'数列': { color: '#5daca1', border: '#7eb8b4' },
	'極限': { color: '#5796be', border: '#7aa9c8' },
	'整数': { color: '#9c82d2', border: '#aa9bd6' },
	'三角関数': { color: '#bda16f', border: '#c1b191' },
	'平面図形': { color: '#b97dab', border: '#be97bb' },
	'図形と方程式': { color: '#be8f74', border: '#c2a495' },
	'場合の数・確率': { color: '#5eacb0', border: '#7fb8bf' },
	'空間図形': { color: '#bc7992', border: '#c095aa' },
	'指数・対数': { color: '#b8aa6e', border: '#beb790' },
	'行列・一次変換': { color: '#7f89d0', border: '#96a0d5' },
	'ベクトル': { color: '#8db474', border: '#a0be95' },
	'複素数平面': { color: '#b17ccf', border: '#b997d4' },
};

export function topicCellGradient(tags) {
	if (!tags.length || tags.some((tag) => !TOPIC_COLORS[tag])) return null;
	const tint = (tag) => {
		const hex = TOPIC_COLORS[tag].color;
		const channels = [1, 3, 5].map((index) => parseInt(hex.slice(index, index + 2), 16));
		return `rgba(${channels.join(', ')}, 0.3)`;
	};
	if (tags.length === 1) return tint(tags[0]);
	const stops = tags.flatMap((tag, index) => {
		const start = Number((index * 100 / tags.length).toFixed(3));
		const end = Number(((index + 1) * 100 / tags.length).toFixed(3));
		return [`${tint(tag)} ${start}%`, `${tint(tag)} ${end}%`];
	});
	return `linear-gradient(90deg, ${stops.join(', ')})`;
}
