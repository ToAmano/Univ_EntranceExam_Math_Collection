import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { h } from 'hastscript';
import { toText } from 'hast-util-to-text';
import { SKIP, visitParents } from 'unist-util-visit-parents';
import { AssistiveMmlHandler } from 'mathjax-full/js/a11y/assistive-mml.js';
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js';
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js';
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js';
import { TeX } from 'mathjax-full/js/input/tex.js';
import { CHTML } from 'mathjax-full/js/output/chtml.js';
import { mathjax } from 'mathjax-full/js/mathjax.js';

const WEB_ROOT = fileURLToPath(new URL('../..', import.meta.url));
const MATHJAX_WOFF_SRC_DIR = path.join(
  WEB_ROOT,
  'node_modules/mathjax-full/es5/output/chtml/fonts/woff-v2'
);
const PUBLIC_FONTS_DIR = path.join(WEB_ROOT, 'public/fonts/mathjax');

const emptyOptions = {};
const emptyClasses = [];

/**
 * Copy MathJax WOFF fonts from mathjax-full into web/public/fonts/mathjax/
 * so that CHTML math works self-hosted under the site's base path without
 * external CDN dependencies.
 */
export function syncMathjaxFonts(
  srcDir = MATHJAX_WOFF_SRC_DIR,
  destDir = PUBLIC_FONTS_DIR
) {
  if (!fs.existsSync(srcDir)) {
    throw new Error(`MathJax font source directory not found: ${srcDir}`);
  }
  fs.mkdirSync(destDir, { recursive: true });
  const files = fs.readdirSync(srcDir).filter((file) => file.endsWith('.woff'));
  for (const file of files) {
    const srcFile = path.join(srcDir, file);
    const destFile = path.join(destDir, file);
    const srcStat = fs.statSync(srcFile);
    if (!fs.existsSync(destFile) || fs.statSync(destFile).size !== srcStat.size) {
      fs.copyFileSync(srcFile, destFile);
    }
  }
  return files;
}

function fromLiteElement(liteElement) {
  const children = [];
  for (const node of liteElement.children) {
    children.push(
      'value' in node
        ? { type: 'text', value: node.value }
        : fromLiteElement(node)
    );
  }
  return h(liteElement.kind, liteElement.attributes, children);
}

function createChtmlRenderer(options) {
  const texOptions = options.tex || {};
  const chtmlOptions = options.chtml || {};
  const enableAssistiveMml = options.enableAssistiveMml ?? true;

  if (!chtmlOptions.fontURL) {
    throw new Error('rehype-mathjax-chtml: missing `chtml.fontURL` option');
  }

  const input = new TeX({ packages: AllPackages, ...texOptions });
  const output = new CHTML(chtmlOptions);
  let document;
  let handler;

  return {
    register() {
      const adapter = liteAdaptor();
      const baseHandler = RegisterHTMLHandler(adapter);
      handler = enableAssistiveMml ? AssistiveMmlHandler(baseHandler) : baseHandler;
      document = mathjax.document('', {
        InputJax: input,
        OutputJax: output,
        enableAssistiveMml,
      });
    },
    render(value, renderOptions) {
      const liteElement = document.convert(value, renderOptions);
      return [fromLiteElement(liteElement)];
    },
    styleSheet() {
      const node = fromLiteElement(output.styleSheet(document));
      node.properties.id = undefined;
      return node;
    },
    unregister() {
      mathjax.handlers.unregister(handler);
    },
  };
}

/**
 * Custom rehype plugin that renders TeX math using MathJax v3 CHTML (CommonHTML)
 * and embeds AssistiveMML (<mjx-assistive-mml><math>...</math></mjx-assistive-mml>)
 * so equations contain real DOM text nodes for searchability, SEO, and accessibility.
 */
export default function rehypeMathjaxChtml(options) {
  return function transform(tree, file) {
    const renderer = createChtmlRenderer(options || emptyOptions);
    let found = false;
    let context = tree;

    visitParents(tree, 'element', function (element, parents) {
      const classes = Array.isArray(element.properties.className)
        ? element.properties.className
        : emptyClasses;
      const languageMath = classes.includes('language-math');
      const mathDisplay = classes.includes('math-display');
      const mathInline = classes.includes('math-inline');
      let display = mathDisplay;

      if (element.tagName === 'head') {
        context = element;
      }

      if (!languageMath && !mathDisplay && !mathInline) {
        return;
      }

      let parent = parents[parents.length - 1];
      let scope = element;

      if (
        element.tagName === 'code' &&
        languageMath &&
        parent &&
        parent.type === 'element' &&
        parent.tagName === 'pre'
      ) {
        scope = parent;
        parent = parents[parents.length - 2];
        display = true;
      }

      if (!parent) return;

      if (!found && renderer.register) renderer.register();
      found = true;

      const text = toText(scope, { whitespace: 'pre' });
      let result;

      try {
        result = renderer.render(text, { display });
      } catch (error) {
        const cause = error;
        file.message('Could not render math with mathjax', {
          ancestors: [...parents, element],
          cause,
          place: element.position,
          ruleId: 'mathjax-error',
          source: 'rehype-mathjax',
        });

        result = [
          {
            type: 'element',
            tagName: 'span',
            properties: {
              className: ['mathjax-error'],
              style: 'color:#cc0000',
              title: String(cause),
            },
            children: [{ type: 'text', value: text }],
          },
        ];
      }

      const index = parent.children.indexOf(scope);
      parent.children.splice(index, 1, ...result);
      return SKIP;
    });

    if (found) {
      if (renderer.styleSheet) context.children.push(renderer.styleSheet());
      if (renderer.unregister) renderer.unregister();
    }
  };
}
