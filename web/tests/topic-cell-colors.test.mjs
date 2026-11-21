import assert from 'node:assert/strict';
import test from 'node:test';
import { TOPIC_COLORS, topicCellGradient } from '../src/lib/topic-colors.mjs';

test('the shared palette uses restrained colors that remain visible on the dark page', () => {
	const colors = Object.values(TOPIC_COLORS).map(({ color }) => color);
	assert.equal(colors.length, 15);
	const channels = (hex) => [1, 3, 5].map((index) => parseInt(hex.slice(index, index + 2), 16) / 255);
	const luminance = (hex) => channels(hex)
		.map((value) => value <= 0.04045 ? value / 12.92 : ((value + 0.055) / 1.055) ** 2.4)
		.reduce((sum, value, index) => sum + value * [0.2126, 0.7152, 0.0722][index], 0);
	const background = luminance('#0f172a');
	for (const color of colors) {
		const rgb = channels(color);
		const range = Math.max(...rgb) - Math.min(...rgb);
		const lightness = (Math.max(...rgb) + Math.min(...rgb)) / 2;
		const saturation = range / (1 - Math.abs(2 * lightness - 1));
		assert.ok(saturation <= 0.54, `${color} is too saturated`);
		assert.ok((luminance(color) + 0.05) / (background + 0.05) >= 5, `${color} is too dark`);
	}
});

test('one topic tints the question cell without hiding the dark surface', () => {
	assert.equal(topicCellGradient(['整数']), 'rgba(156, 130, 210, 0.3)');
});

test('two and three topics occupy equal translucent color bands', () => {
	assert.equal(topicCellGradient(['整数', '積分']),
		'linear-gradient(90deg, rgba(156, 130, 210, 0.3) 0%, rgba(156, 130, 210, 0.3) 50%, rgba(111, 149, 210, 0.3) 50%, rgba(111, 149, 210, 0.3) 100%)');
	assert.equal(topicCellGradient(['整数', '積分', '数列']),
		'linear-gradient(90deg, rgba(156, 130, 210, 0.3) 0%, rgba(156, 130, 210, 0.3) 33.333%, rgba(111, 149, 210, 0.3) 33.333%, rgba(111, 149, 210, 0.3) 66.667%, rgba(93, 172, 161, 0.3) 66.667%, rgba(93, 172, 161, 0.3) 100%)');
});

test('unknown or missing topic tags do not create a misleading color', () => {
	assert.equal(topicCellGradient([]), null);
	assert.equal(topicCellGradient(['未登録']), null);
});
