import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import sitemap from '@astrojs/sitemap';
import { fileURLToPath } from 'node:url';
import { includeInSitemap, solutionSlugsFromMarkdown, createSitemapSerializer } from './src/lib/canonical-sitemap.mjs';
import rehypeMathjaxChtml, { syncMathjaxFonts } from './src/lib/rehype-mathjax-chtml.mjs';

const BASE_PATH = '/Univ_EntranceExam_Math_Collection';
syncMathjaxFonts();
const solutionSlugs = solutionSlugsFromMarkdown(fileURLToPath(new URL('./src/content/solutions/', import.meta.url)));
const serializeItem = createSitemapSerializer();

export default defineConfig({
  site: 'https://toamano.github.io',
  base: BASE_PATH,
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
      [rehypeMathjaxChtml, {
        tex: {
          tags: 'ams',
          inlineMath: [['$', '$'], ['\\(', '\\)']],
          macros: {
            mqty: ['\\begin{pmatrix}#1\\end{pmatrix}', 1],
            // physics パッケージの微分記号 (\dd x)。PDF は physics.sty が定義する。
            dd: '{\\mathrm{d}}',
            // bclogo パッケージの四面体記号（東工大後期 2011-1）。Layout.astro 側で SVG マスクとして描画する。
            bctetraedre: '\\class{mjx-bctetraedre}{\\phantom{\\mathrm{M}}}\\,',
          },
        },
        chtml: {
          fontURL: `${BASE_PATH}/fonts/mathjax`,
          displayOverflow: 'overflow',
          linebreaks: {
            inline: true,
          },
        },
        options: {
          skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
        },
      }],
    ],
  },
});
