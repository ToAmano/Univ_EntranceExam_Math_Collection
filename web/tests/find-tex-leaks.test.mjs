import test from 'node:test';
import assert from 'node:assert/strict';
import { findLeaks } from '../scripts/find-tex-leaks.mjs';

const commands = (markdown) => findLeaks(markdown).map((leak) => leak.command);

test('TeX commands shown outside math are reported', () => {
  assert.deepEqual(commands('とかける．\\label{eq:1} この曲線'), ['\\label']);
  assert.deepEqual(commands('\\begin{addmargin}[2em]{0pt}\n\n本文'), ['\\begin']);
  assert.deepEqual(commands('| $f$ | \\curvearrowright |\n|---|---|\n| a | b |'), ['\\curvearrowright']);
});

test('math, Markdown escapes and HTML attributes are not leaks', () => {
  // \% や \# は Markdown のエスケープとして % や # に表示される
  assert.deepEqual(commands('割合は69\\%，100（\\%）とし \\& と \\#'), []);
  // 数式の中の > や < を、タグと取り違えない
  assert.deepEqual(commands('#### $r > \\dfrac{\\ell}{2}$の時\n\n図 2: $0 < r \\le \\dfrac{\\ell}{2}$ のとき'), []);
  assert.deepEqual(commands('$$\n\\begin{align}\nx = \\dfrac{1}{2}\n\\end{align}\n$$'), []);
  assert.deepEqual(commands('<img src="a.svg" alt="$\\alpha, \\beta$ の交点" />'), []);
});

test('front matter is ignored', () => {
  assert.deepEqual(commands('---\ntitle: "\\\\alpha"\n---\n本文．'), []);
});
