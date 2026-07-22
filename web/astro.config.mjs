import { defineConfig } from 'astro/config';
import remarkMath from 'remark-math';
import rehypeMathjax from 'rehype-mathjax';

export default defineConfig({
  site: 'https://toamano.github.io',
  base: '/Univ_EntranceExam_Math_Collection',
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
