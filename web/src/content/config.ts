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
	}),
});

export const collections = {
	solutions: solutionsCollection,
};
