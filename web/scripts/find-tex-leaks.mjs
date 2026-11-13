// Web 用 Markdown を、サイトと同じ Markdown 処理（remark-math・生 HTML）で HTML にし、
// 数式の外に表示される TeX のコマンド（\begin、\label など）を探す（#1489）。
//
// 使い方: node web/scripts/find-tex-leaks.mjs FILE.md...
// 出力: 見つかったものを1行1件の JSON（{"file", "command", "context"}）で標準出力に書く。
//
// 文字列の正規表現ではなく HTML の木をたどって判定する。正規表現で数式やタグを
// 取り除く方式は、本文の \% など Markdown のエスケープ（表示は %）や、数式の中の
// `>` を誤って漏れと判定していた。
//
// unified・remark-parse・remark-rehype・rehype-raw は Astro の依存として npm ci で
// node_modules の最上位に入る（package.json には直接書いていない）。
import fs from 'node:fs';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkMath from 'remark-math';
import remarkRehype from 'remark-rehype';
import rehypeRaw from 'rehype-raw';

const TEX_COMMAND = /\\[A-Za-z]+/g;
// 中身を表示テキストとして見ない要素（数式・コード）
const SKIP_TAGS = new Set(['code', 'pre', 'script', 'style', 'math', 'svg']);

const processor = unified()
  .use(remarkParse)
  .use(remarkMath)
  .use(remarkRehype, { allowDangerousHtml: true })
  .use(rehypeRaw);

function isSkipped(node) {
  if (node.type !== 'element') return false;
  if (SKIP_TAGS.has(node.tagName)) return true;
  const classes = node.properties?.className ?? [];
  return classes.some((name) => String(name).startsWith('math') || String(name).startsWith('language-math'));
}

// 表示される文字列を、要素の境目に空白を挟んでつなげる
function visibleText(node, out) {
  if (isSkipped(node)) {
    out.push(' ');
    return;
  }
  if (node.type === 'text') out.push(node.value);
  for (const child of node.children ?? []) visibleText(child, out);
  if (node.type === 'element') out.push(' ');
}

export function findLeaks(markdown) {
  const body = markdown.replace(/^---\n[\s\S]*?\n---\n/, '');
  const tree = processor.runSync(processor.parse(body));
  const parts = [];
  visibleText(tree, parts);
  const text = parts.join('');
  return [...text.matchAll(TEX_COMMAND)].map((m) => ({
    command: m[0],
    context: text.slice(Math.max(0, m.index - 30), m.index + m[0].length + 30).replace(/\s+/g, ' ').trim(),
  }));
}

if (import.meta.url === `file://${process.argv[1]}`) {
  for (const file of process.argv.slice(2)) {
    for (const leak of findLeaks(fs.readFileSync(file, 'utf8'))) {
      process.stdout.write(JSON.stringify({ file, ...leak }) + '\n');
    }
  }
}
