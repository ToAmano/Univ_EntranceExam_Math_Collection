import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkMath from 'remark-math';
import remarkRehype from 'remark-rehype';
import rehypeStringify from 'rehype-stringify';
import rehypeMathjaxChtml, { syncMathjaxFonts } from '../src/lib/rehype-mathjax-chtml.mjs';

const FONT_URL = '/Univ_EntranceExam_Math_Collection/fonts/mathjax';

async function renderMarkdown(md) {
  const file = await unified()
    .use(remarkParse)
    .use(remarkMath)
    .use(remarkRehype, { allowDangerousHtml: true })
    .use(rehypeMathjaxChtml, {
      tex: {
        tags: 'ams',
        inlineMath: [['$', '$'], ['\\(', '\\)']],
        macros: {
          mqty: ['\\begin{pmatrix}#1\\end{pmatrix}', 1],
          dd: '{\\mathrm{d}}',
          bctetraedre: '\\class{mjx-bctetraedre}{\\phantom{\\mathrm{M}}}\\,',
        },
      },
      chtml: {
        fontURL: FONT_URL,
      },
    })
    .use(rehypeStringify, { allowDangerousHtml: true })
    .process(md);
  return String(file);
}

test('renders TeX math as CHTML with AssistiveMML text nodes and self-hosted font URLs', async () => {
  const html = await renderMarkdown(
    '関数 $f(x) = \\dfrac{x^2+1}{2}$ について\n\n$$\n\\begin{align}\n\\int_0^1 \\mqty{x \\\\ y} \\dd x &= 1 \\label{eq:1}\n\\end{align}\n$$'
  );

  // 1. CHTML output is used instead of inline SVG paths
  assert.match(html, /jax="CHTML"/);
  assert.doesNotMatch(html, /<svg[\s>]/);

  // 2. AssistiveMML embeds real MathML text nodes for SEO/search/accessibility
  assert.match(html, /<mjx-assistive-mml[^>]*><math[\s>]/);
  assert.match(html, /<mi>f<\/mi>/);
  assert.match(html, /<mn>2<\/mn>/);

  // 3. Stylesheet references self-hosted fontURL under base path
  assert.match(html, new RegExp(`${FONT_URL}/MathJax_Main-Regular\\.woff`));
  assert.match(html, /mjx-assistive-mml\s*\{/);
});

test('syncMathjaxFonts copies all WOFF fonts into public/fonts/mathjax', () => {
  const copied = syncMathjaxFonts();
  assert.ok(copied.length >= 20, `expected at least 20 WOFF fonts, got ${copied.length}`);
  const publicFontsDir = fileURLToPath(new URL('../public/fonts/mathjax', import.meta.url));
  for (const file of ['MathJax_Main-Regular.woff', 'MathJax_Math-Italic.woff', 'MathJax_Zero.woff']) {
    assert.ok(fs.existsSync(path.join(publicFontsDir, file)), `missing ${file}`);
  }
});

test('renders bctetraedre macro without undefined control sequence errors', async () => {
  const html = await renderMarkdown(
    '$$\n\\begin{align}\nV = \\bctetraedre\\mathrm{POAB} + \\bctetraedre\\mathrm{POBC}\n\\end{align}\n$$'
  );
  const mathMarkup = html.split('<style')[0];

  assert.doesNotMatch(mathMarkup, /mathjax-error|mjx-merror/);
  assert.match(mathMarkup, /class="mjx-bctetraedre"/);
  assert.match(mathMarkup, /POAB/);
});

test('renders mjx-inline-tikz placeholders as img tags inside CHTML equations', async () => {
  const html = await renderMarkdown(
    '$$\n\\begin{align}\nV = \\left(\\class{mjx-inline-tikz}{\\style{background-image:url(/img/inline_1.svg);}{\\vcenter{\\hbox{\\rule{2.75em}{2.86em}}}}}\\right)\n\\end{align}\n$$'
  );
  const mathMarkup = html.split('<style')[0];

  assert.doesNotMatch(mathMarkup, /mathjax-error|mjx-merror/);
  assert.doesNotMatch(mathMarkup, /background-color:\s*black/);
  assert.doesNotMatch(mathMarkup, /background-image/);
  assert.match(mathMarkup, /<img[^>]*src="\/img\/inline_1\.svg"[^>]*class="inline-tikz-icon"/);
  assert.match(mathMarkup, /<mrow[^>]*class="mjx-inline-tikz"[^>]*><mtext>\[図\]<\/mtext><\/mrow>/);
});
