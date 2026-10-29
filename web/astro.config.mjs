import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeMathjax from 'rehype-mathjax';
import sitemap from '@astrojs/sitemap';
import { fileURLToPath } from 'node:url';
import { includeInSitemap, solutionSlugsFromMarkdown, createSitemapSerializer } from './src/lib/canonical-sitemap.mjs';

const solutionSlugs = solutionSlugsFromMarkdown(fileURLToPath(new URL('./src/content/solutions/', import.meta.url)));
const serializeItem = createSitemapSerializer();

export default defineConfig({
  site: 'https://toamano.github.io',
  base: '/Univ_EntranceExam_Math_Collection',
  trailingSlash: 'always',
  integrations: [
    sitemap({
      filter: page => includeInSitemap(page, solutionSlugs),
      serialize: serializeItem,
    }),
  ],
  markdown: {
    remarkPlugins: [remarkMath],
    rehypePlugins: [
      [rehypeMathjax, {
        tex: {
          tags: 'ams',
          inlineMath: [['$', '$'], ['\\(', '\\)']],
          macros: {
            mqty: ['\\begin{pmatrix}#1\\end{pmatrix}', 1],
          },
        },
        options: {
          skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
        },
      }],
    ],
  },
});
