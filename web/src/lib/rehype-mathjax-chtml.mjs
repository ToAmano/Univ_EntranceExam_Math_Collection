import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { h } from 'hastscript';
import { toText } from 'hast-util-to-text';
import { SKIP, visitParents } from 'unist-util-visit-parents';
import { AssistiveMmlHandler } from '@mathjax/src/js/a11y/assistive-mml.js';
import { liteAdaptor } from '@mathjax/src/js/adaptors/liteAdaptor.js';
import { RegisterHTMLHandler } from '@mathjax/src/js/handlers/html.js';
import { TeX } from '@mathjax/src/js/input/tex.js';
import { CHTML } from '@mathjax/src/js/output/chtml.js';
import { mathjax } from '@mathjax/src/js/mathjax.js';
import { MathJaxNewcmFont } from '@mathjax/mathjax-newcm-font/js/chtml.js';

import '@mathjax/src/js/input/tex/base/BaseConfiguration.js';
import '@mathjax/src/js/input/tex/action/ActionConfiguration.js';
import '@mathjax/src/js/input/tex/ams/AmsConfiguration.js';
import '@mathjax/src/js/input/tex/amscd/AmsCdConfiguration.js';
import '@mathjax/src/js/input/tex/autoload/AutoloadConfiguration.js';
import '@mathjax/src/js/input/tex/bbox/BboxConfiguration.js';
import '@mathjax/src/js/input/tex/boldsymbol/BoldsymbolConfiguration.js';
import '@mathjax/src/js/input/tex/braket/BraketConfiguration.js';
import '@mathjax/src/js/input/tex/bussproofs/BussproofsConfiguration.js';
import '@mathjax/src/js/input/tex/cancel/CancelConfiguration.js';
import '@mathjax/src/js/input/tex/cases/CasesConfiguration.js';
import '@mathjax/src/js/input/tex/centernot/CenternotConfiguration.js';
import '@mathjax/src/js/input/tex/color/ColorConfiguration.js';
import '@mathjax/src/js/input/tex/colortbl/ColortblConfiguration.js';
import '@mathjax/src/js/input/tex/configmacros/ConfigMacrosConfiguration.js';
import '@mathjax/src/js/input/tex/empheq/EmpheqConfiguration.js';
import '@mathjax/src/js/input/tex/enclose/EncloseConfiguration.js';
import '@mathjax/src/js/input/tex/extpfeil/ExtpfeilConfiguration.js';
import '@mathjax/src/js/input/tex/gensymb/GensymbConfiguration.js';
import '@mathjax/src/js/input/tex/html/HtmlConfiguration.js';
import '@mathjax/src/js/input/tex/mathtools/MathtoolsConfiguration.js';
import '@mathjax/src/js/input/tex/mhchem/MhchemConfiguration.js';
import '@mathjax/src/js/input/tex/newcommand/NewcommandConfiguration.js';
import '@mathjax/src/js/input/tex/noundefined/NoUndefinedConfiguration.js';
import '@mathjax/src/js/input/tex/require/RequireConfiguration.js';
import '@mathjax/src/js/input/tex/setoptions/SetOptionsConfiguration.js';
import '@mathjax/src/js/input/tex/tagformat/TagFormatConfiguration.js';
import '@mathjax/src/js/input/tex/textcomp/TextcompConfiguration.js';
import '@mathjax/src/js/input/tex/textmacros/TextMacrosConfiguration.js';
import '@mathjax/src/js/input/tex/unicode/UnicodeConfiguration.js';
import '@mathjax/src/js/input/tex/upgreek/UpgreekConfiguration.js';
import '@mathjax/src/js/input/tex/verb/VerbConfiguration.js';

if (!mathjax.asyncLoad) {
  mathjax.asyncLoad = (name) => import(name);
}

const ALL_TEX_PACKAGES = [
  'base',
  'action',
  'ams',
  'amscd',
  'autoload',
  'bbox',
  'boldsymbol',
  'braket',
  'bussproofs',
  'cancel',
  'cases',
  'centernot',
  'color',
  'colortbl',
  'configmacros',
  'empheq',
  'enclose',
  'extpfeil',
  'gensymb',
  'html',
  'mathtools',
  'mhchem',
  'newcommand',
  'noundefined',
  'require',
  'setoptions',
  'tagformat',
  'textcomp',
  'textmacros',
  'unicode',
  'upgreek',
  'verb',
];

const WEB_ROOT = fileURLToPath(new URL('../..', import.meta.url));
const MATHJAX_WOFF_SRC_DIR = path.join(
  WEB_ROOT,
  'node_modules/@mathjax/mathjax-newcm-font/chtml/woff2'
);
const PUBLIC_FONTS_DIR = path.join(WEB_ROOT, 'public/fonts/mathjax');

const emptyOptions = {};
const emptyClasses = [];

/**
 * Copy MathJax v4 WOFF2 fonts from @mathjax/mathjax-newcm-font into
 * web/public/fonts/mathjax/ so that CHTML math works self-hosted under the
 * site's base path without external CDN dependencies.
 */
export function syncMathjaxFonts(
  srcDir = MATHJAX_WOFF_SRC_DIR,
  destDir = PUBLIC_FONTS_DIR
) {
  if (!fs.existsSync(srcDir)) {
    throw new Error(`MathJax font source directory not found: ${srcDir}`);
  }
  fs.mkdirSync(destDir, { recursive: true });
  const files = fs.readdirSync(srcDir).filter((file) => /\.woff2?$/i.test(file));
  const expected = new Set(files);
  for (const existing of fs.readdirSync(destDir)) {
    if (/\.woff2?$/i.test(existing) && !expected.has(existing)) {
      fs.unlinkSync(path.join(destDir, existing));
    }
  }
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

const INLINE_TIKZ_URL_RE = /background-image:\s*url\(([^)]+)\)\s*;?/i;
const INLINE_TIKZ_BG_RE = /background-color:\s*[^;]+;?/i;

function replaceInlineTikzIcons(nodes) {
  for (const root of nodes) {
    visitParents(root, 'element', function (element) {
      const classes = Array.isArray(element.properties?.className)
        ? element.properties.className
        : emptyClasses;
      if (!classes.includes('mjx-inline-tikz')) return;

      const style = String(element.properties?.style || '');
      const urlMatch = style.match(INLINE_TIKZ_URL_RE);
      if (!urlMatch) return;
      const src = urlMatch[1].trim().replace(/^['"]|['"]$/g, '');
      const cleanedStyle = style.replace(INLINE_TIKZ_URL_RE, '').trim();
      if (cleanedStyle) {
        element.properties.style = cleanedStyle;
      } else {
        delete element.properties.style;
      }

      if (element.tagName === 'mpadded' || element.tagName === 'mrow') {
        element.children = [h('mtext', '[図]')];
        return SKIP;
      }

      visitParents(element, 'element', function (child) {
        if (child.tagName !== 'mjx-mspace') return;
        const mspaceStyle = String(child.properties?.style || '');
        const cleanedMspaceStyle = mspaceStyle.replace(INLINE_TIKZ_BG_RE, '').trim();
        child.properties.style = cleanedMspaceStyle;
        const wMatch = cleanedMspaceStyle.match(/width:\s*([^;]+)/i);
        const hMatch = cleanedMspaceStyle.match(/height:\s*([^;]+)/i);
        const imgStyle = [
          wMatch ? `width:${wMatch[1].trim()};` : '',
          hMatch ? `height:${hMatch[1].trim()};` : '',
        ].join('');
        child.children = [
          h('img', {
            src,
            alt: '数式中の図',
            className: ['inline-tikz-icon'],
            ...(imgStyle ? { style: imgStyle } : {}),
          }),
        ];
        return SKIP;
      });

      return SKIP;
    });
  }
}

function createChtmlRenderer(options) {
  const texOptions = options.tex || {};
  const chtmlOptions = options.chtml || {};
  const enableAssistiveMml = options.enableAssistiveMml ?? true;

  if (!chtmlOptions.fontURL) {
    throw new Error('rehype-mathjax-chtml: missing `chtml.fontURL` option');
  }

  const adapter = liteAdaptor();
  const input = new TeX({ packages: ALL_TEX_PACKAGES, ...texOptions });
  const output = new CHTML({ fontData: MathJaxNewcmFont, ...chtmlOptions });
  let readyPromise = null;
  let dynamicFontStyles = null;
  let document;

  return {
    ensureReady() {
      if (!readyPromise) {
        readyPromise = output.font.loadDynamicFiles().then(() => {
          // FontData#styles clears fontUsage after the first stylesheet build.
          // Snapshot dynamic @font-face / font-family rules so every SSG page
          // receives the full self-hosted font CSS after reset().
          dynamicFontStyles = { ...output.font.fontUsage };
          const baseHandler = RegisterHTMLHandler(adapter);
          const handler = enableAssistiveMml
            ? AssistiveMmlHandler(baseHandler)
            : baseHandler;
          try {
            document = mathjax.document('', {
              InputJax: input,
              OutputJax: output,
              enableAssistiveMml,
            });
          } finally {
            mathjax.handlers.unregister(handler);
          }
        });
      }
      return readyPromise;
    },
    reset() {
      document.reset({ all: true });
      document.clear();
      output.font.fontUsage = { ...dynamicFontStyles };
    },
    render(value, renderOptions) {
      const liteElement = document.convert(value, renderOptions);
      const nodes = [fromLiteElement(liteElement)];
      replaceInlineTikzIcons(nodes);
      return nodes;
    },
    styleSheet() {
      const node = fromLiteElement(output.styleSheet(document));
      node.properties.id = undefined;
      return node;
    },
  };
}

/**
 * Custom rehype plugin that renders TeX math using MathJax v4 CHTML (CommonHTML)
 * and embeds AssistiveMML (<mjx-assistive-mml><math>...</math></mjx-assistive-mml>)
 * so equations contain real DOM text nodes for searchability, SEO, and accessibility.
 */
export default function rehypeMathjaxChtml(options) {
  const renderer = createChtmlRenderer(options || emptyOptions);

  return async function transform(tree, file) {
    await renderer.ensureReady();
    renderer.reset();
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
      context.children.push(renderer.styleSheet());
    }
  };
}
