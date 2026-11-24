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
        displayOverflow: 'overflow',
        linebreaks: {
          inline: true,
        },
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
  assert.match(html, /<mi[^>]*>f<\/mi>/);
  assert.match(html, /<mn[^>]*>2<\/mn>/);

  // 3. Stylesheet references self-hosted v4 NewCM WOFF2 fonts under base path
  assert.match(html, new RegExp(`${FONT_URL}/mjx-ncm-n\\.woff2`));
  assert.match(html, /mjx-assistive-mml\s*\{/);
});

test('marks breakable points for automatic inline math linebreaking in v4', async () => {
  const html = await renderMarkdown(
    '条件 $a_1 + a_2 + a_3 = b_1 + b_2 + b_3$ が成り立つ．'
  );
  const mathMarkup = html.split('<style')[0];

  assert.match(mathMarkup, /<mjx-math[^>]*breakable="true"/);
  assert.match(mathMarkup, /<mjx-break[\s>]/);
});

test('supports extended TeX packages (dcases, numcases, cancel, dynamic fonts, Japanese mtext)', async () => {
  const html = await renderMarkdown(
    '$$\n\\begin{dcases} x = \\cancel{a} + b \\in \\mathbb{R} & (\\text{通り}) \\\\ \\mathcal{F}(\\mathfrak{g}) = \\mathscr{S} & \\end{dcases}\n$$\n\n$$\n\\begin{numcases}{f(x)=} x & $x \\ge 0$ \\\\ -x & $x < 0$ \\end{numcases}\n$$'
  );
  const mathMarkup = html.split('<style')[0];

  assert.doesNotMatch(mathMarkup, /mathjax-error|mjx-merror/);
  assert.match(mathMarkup, /通り/);
  assert.match(mathMarkup, /ℝ/);
});

test('preserves dynamic @font-face rules across repeated independent document renders', async () => {
  const first = await renderMarkdown('$x$');
  const second = await renderMarkdown('$$\\bigtriangleup ABC \\implies \\mathbb{R}$$');

  assert.doesNotMatch(second.split('<style')[0], /mathjax-error|mjx-merror/);
  assert.match(first, /@font-face/);
  assert.match(second, /@font-face \/\* NCM-SH \*\//);
  assert.match(second, /mjx-ncm-sh\.woff2/);
});

test('syncMathjaxFonts copies all WOFF2 fonts into public/fonts/mathjax', () => {
  const copied = syncMathjaxFonts();
  assert.ok(copied.length >= 20, `expected at least 20 WOFF2 fonts, got ${copied.length}`);
  const publicFontsDir = fileURLToPath(new URL('../public/fonts/mathjax', import.meta.url));
  for (const file of ['mjx-ncm-n.woff2', 'mjx-ncm-i.woff2', 'mjx-ncm-zero.woff2']) {
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
  assert.doesNotMatch(mathMarkup, /style="[^"]*background-image/);
  assert.match(mathMarkup, /<img[^>]*src="\/img\/inline_1\.svg"[^>]*class="inline-tikz-icon"/);
  assert.match(mathMarkup, /<(?:mpadded|mrow)[^>]*class="mjx-inline-tikz"[^>]*><mtext>\[図\]<\/mtext><\/(?:mpadded|mrow)>/);
});
