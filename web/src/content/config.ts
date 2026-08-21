import { defineCollection, z } from 'astro:content';

const solutionsCollection = defineCollection({
	type: 'content',
	schema: z.object({
		university: z.string(),
		category: z.string(),
		year: z.string(),
		question: z.string(),
		type: z.string().optional(),
		title: z.string().optional(),
		tags: z.array(z.string()).optional(),
	}),
});

// 手動で書くお知らせ（「サイトのデザインを更新しました」等、特定の解答ファイルに
// 紐づかないもの）。src/**/solution.tex の追加・更新から自動生成されるニュースは
// scratch/generate_news.py が web/src/data/news-auto.json に書き出す（ビルドごとに
// 再生成、コミットはしない）。トップページ・お知らせ一覧ページは両方を読んでマージする。
const newsCollection = defineCollection({
	type: 'content',
	schema: z.object({
		date: z.string(),
		title: z.string(),
	}),
});

export const collections = {
	solutions: solutionsCollection,
	news: newsCollection,
};
