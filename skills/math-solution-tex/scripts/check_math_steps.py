#!/usr/bin/env python3
"""式変形の自動検算（SymPy による数値比較）。

align 環境の中の式変形を取り出し、隣り合う式に数値を代入して比べる。
誤りの「候補」を出す道具であり、指摘は必ず人が原稿で確かめる。

確度:
  A     文字を含まない数値どうしの比較（文脈に左右されない。誤りの可能性が高い）
  B     それ以外（文字の意味や前提を人が確かめる必要がある）

検査の種類:
  EQ    等号でつないだ変形（a = b = c）で、隣り合う式の値が一致しない
  NEW   定数だった式の次に、文字を含む式が等号で続く（代入の向きが逆・文字の書き忘れの疑い）
  INEQ  不等号でつないだ変形で、数値を代入すると不等号が成り立たない（反例）
  SOLVE 行ごとに書いた方程式で、次の行の解（x = ... の形）が前の行の方程式を満たさない

文字の扱い:
  - 本文の「$p=\\sin^2\\theta$ とおく」「$c=\\cos\\theta$ とする」などの定義を拾い、
    定義された文字を代入してから比べる（使う文字が変わる変形も検算できる）。
  - n, m, k, l, j, N, M は正の整数として、それ以外の文字は 0.3〜1.9 の値として代入する。
  - 虚数単位 i は、文字 i として比べて一致しない場合に虚数単位としても比べ、両方で一致しないときだけ報告する。

使い方:
  python3 scripts/check_math_steps.py path/to/solution.tex [...]
  python3 scripts/check_math_steps.py --tier A --json out.json src/*/*/*/*/solution.tex

依存: scripts/requirements.txt（sympy と、sympy.parsing.latex が使う antlr4-python3-runtime==4.11）
  python3 -m pip install -r scripts/requirements.txt
"""
import argparse
import json
import multiprocessing
import subprocess
from concurrent.futures import ThreadPoolExecutor
import random
import re
import signal
import sys
import time
from contextlib import contextmanager

import sympy as sp
from sympy.core.function import AppliedUndef
from sympy.parsing.latex import parse_latex

_C, _S, _U = sp.symbols('c s u__')
ALIGN_RE = re.compile(r'\\begin\{(align\*?|split)\}(.*?)\\end\{\1\}', re.S)
INTEGER_NAMES = {'n', 'm', 'k', 'l', 'j', 'N', 'M'}
FUNCS = ['sin', 'cos', 'tan', 'log', 'ln', 'exp']
REL_RE = re.compile(r'(\\leqq(?![A-Za-z])|\\geqq(?![A-Za-z])|\\leq(?![A-Za-z])|\\geq(?![A-Za-z])|'
                    r'\\le(?![A-Za-z])|\\ge(?![A-Za-z])|<|>|=)')
REL_NORM = {'\\leqq': '<=', '\\leq': '<=', '\\le': '<=', '\\geqq': '>=', '\\geq': '>=', '\\ge': '>=',
            '<': '<', '>': '>', '=': '='}
# 数式として比べられない内容（論理記号・ベクトル・日本語など）を含む式は飛ばす
SKIP_RE = re.compile(r'\\text|\\mathrm\{[^}]{2,}\}|\\therefore|\\because|\\iff|\\Rightarrow|\\Leftarrow|'
                     r'\\begin|\\end|\\cdots|\\ldots|\\dots|\\overrightarrow|\\vec|\\triangle|\\angle|'
                     r'[ぁ-んァ-ヶ一-龥]|\\pm|\\mp|\\approx|\\equiv|\\in\b|\\sim|\\to\b|\\neq|\\ne\b|'
                     r'\\max|\\min|\\sup|\\inf|\\prime|\'|\\mid|\\perp|\\parallel|\\cap|\\cup|\\subset|'
                     r'\\overline|\\bar|\\hat|\\boldsymbol|\\bm|\\mathbf|\\det|\\infty|!|'
                     r'\\node|\\draw|\\x\b|\.\.\.|_\{[^{}]*,[^{}]*\}|:|\\arg|\b[Ee]\(|\\operatorname')
CONSEQ_RE = re.compile(r'\s*\\(?:therefore|iff|Longleftrightarrow|Leftrightarrow|Rightarrow|Longrightarrow)\s*')
NAME_RE = re.compile(r'(?:\\?[A-Za-z]+(?:_\{?[^{}]*\}?)?(?:\^\{?[^{}]*\}?)?(?:\([^()]*\))?|\|[^|]*\|)')


class Timeout(Exception):
    pass


@contextmanager
def time_limit(seconds):
    """入れ子で使える時間制限。外側の残り時間より長くはしない。"""
    def handler(signum, frame):
        raise Timeout()
    outer = signal.getitimer(signal.ITIMER_REAL)[0]
    start = time.monotonic()
    old = signal.signal(signal.SIGALRM, handler)
    signal.setitimer(signal.ITIMER_REAL, min(seconds, outer) if outer > 0 else seconds)
    try:
        yield
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, old)
        if outer > 0:
            remaining = outer - (time.monotonic() - start)
            signal.setitimer(signal.ITIMER_REAL, max(remaining, 1e-3))


# ---------------------------------------------------------------------------
# LaTeX の前処理
# ---------------------------------------------------------------------------

def strip_comments(text):
    return '\n'.join(re.sub(r'(?<!\\)%.*', '', line) for line in text.splitlines())


def _braced(s, i):
    """s[i] == '{' の対応する '}' の次の位置を返す。"""
    depth = 0
    for j in range(i, len(s)):
        if s[j] == '{':
            depth += 1
        elif s[j] == '}':
            depth -= 1
            if depth == 0:
                return j + 1
    return len(s)


def _wrap_function_args(e):
    """\\sin 2t や \\tan\\frac{\\pi}{n} の引数を括弧で囲む。\\sin^2 x は (\\sin(x))^2 にする。"""
    out = []
    i = 0
    func_re = re.compile(r'\\(' + '|'.join(FUNCS) + r')(?![A-Za-z])')
    while True:
        m = func_re.search(e, i)
        if not m:
            out.append(e[i:])
            break
        out.append(e[i:m.start()])
        j = m.end()
        power = ''
        base = ''
        if m.group(1) == 'log':
            bm = re.match(r'\s*_(\{[^{}]*\}|\d)', e[j:])
            if bm:
                base = bm.group(1).strip('{}')
                j += bm.end()
        pm = re.match(r'\s*\^(\{[^{}]*\}|\d)', e[j:])
        if pm:
            power = pm.group(1)
            j += pm.end()
        while j < len(e) and e[j] == ' ':
            j += 1
        if j < len(e) and e[j] == '(':
            # すでに括弧がある：対応する ')' まで
            depth = 0
            k = j
            while k < len(e):
                depth += {'(': 1, ')': -1}.get(e[k], 0)
                k += 1
                if depth == 0:
                    break
            arg = e[j + 1:k - 1]
            # \sin(k+1)\theta は \sin((k+1)\theta)
            tm = re.match(r'\s*(\\(?:theta|alpha|beta|gamma|phi|varphi|omega)|[a-zA-Z])(?![a-zA-Z(])', e[k:])
            if tm:
                arg = f'({arg}){tm.group(1)}'
                k += tm.end()
        else:
            k = j
            while k < len(e):
                c = e[k]
                if c in '+-=,)]<>|}' or e.startswith('\\cdot', k) or e.startswith('\\times', k) \
                        or e.startswith('\\right', k) or func_re.match(e, k):
                    break
                if c == '\\':
                    cm = re.match(r'\\(frac|dfrac|sqrt)', e[k:])
                    if cm and e[j:k].strip():
                        break  # \cos^2\theta \frac{1}{...} の \frac は次の因子
                    if cm:
                        k += cm.end()
                        while k < len(e) and e[k] in '{[':
                            k = _braced(e, k) if e[k] == '{' else e.index(']', k) + 1
                        continue
                    cm = re.match(r'\\[A-Za-z]+', e[k:])
                    k += cm.end() if cm else 1
                    continue
                if c in '^_':
                    k += 1
                    if k < len(e) and e[k] == '{':
                        k = _braced(e, k)
                    else:
                        k += 1
                    continue
                if c == '{':
                    k = _braced(e, k)
                    continue
                if c == '(':
                    # 引数の直後の括弧は掛け算（\sin\theta (1+x) など）として扱い、引数を閉じる
                    if e[j:k].strip():
                        break
                k += 1
            arg = e[j:k]
        if not arg.strip():
            out.append(e[m.start():k])
            i = k
            continue
        fn = '\\' + m.group(1)
        body = f'{fn}({_wrap_function_args(arg)})'
        if base:
            body = f'\\frac{{\\log({_wrap_function_args(arg)})}}{{\\log({base})}}'
        out.append(f'({body})^{{{power.strip("{}")}}}' if power else body)
        i = k
    return ''.join(out)


def _script_arg(e, i):
    """e[i] から始まる上付き・下付きの引数（{...} または1文字）と、その次の位置を返す。"""
    while i < len(e) and e[i] == ' ':
        i += 1
    if i < len(e) and e[i] == '{':
        j = _braced(e, i)
        return e[i + 1:j - 1], j
    return (e[i], i + 1) if i < len(e) else ('', i)


def _expand_evaluation_brackets(e):
    """[F(x)]_{a}^{b} を (F(b)-F(a)) に展開する。積分変数は F にあって a,b にない文字が1つのとき。"""
    consts = {sp.Symbol('e'): sp.E, sp.Symbol('pi'): sp.pi}
    for close in [k for k, ch in enumerate(e) if ch == ']']:
        m = re.match(r'\s*_', e[close + 1:])
        if not m:
            continue
        lower, k = _script_arg(e, close + 1 + m.end())
        m2 = re.match(r'\s*\^', e[k:])
        if not m2:
            continue
        upper, k2 = _script_arg(e, k + m2.end())
        depth, open_ = 0, None
        for j in range(close - 1, -1, -1):
            if e[j] == ']':
                depth += 1
            elif e[j] == '[':
                if depth == 0:
                    open_ = j
                    break
                depth -= 1
        if open_ is None:
            continue
        try:
            F = parse_latex(e[open_ + 1:close]).subs(consts)
            a = parse_latex(lower).subs(consts)
            b = parse_latex(upper).subs(consts)
        except Exception:
            return e
        cands = F.free_symbols - a.free_symbols - b.free_symbols
        if F.free_symbols and F.free_symbols <= {_C, _S} and not (a.free_symbols | b.free_symbols) \
                and (a.has(sp.pi) or b.has(sp.pi)):
            # c=\cos\theta, s=\sin\theta の略記のまま角度の値を代入している
            F = F.subs({_C: sp.cos(_U), _S: sp.sin(_U)})
            cands = {_U}
        if len(cands) != 1:
            return e
        v = cands.pop()
        val = sp.latex(F.subs(v, b) - F.subs(v, a))
        return _expand_evaluation_brackets(e[:open_] + '(' + val + ')' + e[k2:])
    return e


def _mqty_norm(e):
    """|\\mqty(a \\\\ b)| をベクトルの大きさ \\sqrt{(a)^2+(b)^2} にする。"""
    pat = re.compile(r'(?:\\left)?\|\s*\\mqty\(')
    m = pat.search(e)
    if not m:
        return e
    depth, k = 1, m.end()
    while k < len(e) and depth:
        depth += {'(': 1, ')': -1}.get(e[k], 0)
        k += 1
    inner = e[m.end():k - 1]
    end = re.match(r'\s*(?:\\right)?\|', e[k:])
    if not end:
        return e
    comps = [c.strip() for c in re.split(r'\\\\', inner) if c.strip()]
    norm = '\\sqrt{' + '+'.join(f'({c})^2' for c in comps) + '}'
    return _mqty_norm(e[:m.start()] + norm + e[k + end.end():])


def clean(expr):
    e = _mqty_norm(expr)
    # TeX では ^ や _ の直後の1文字だけが上付き・下付きになる（\sum_{k=1}^9 99k の上端は 9）
    e = re.sub(r'([\^_])\s*([0-9A-Za-z])', r'\1{\2}', e)
    e = re.sub(r'\\label\{[^}]*\}|\\notag|\\nonumber|\\tag\{[^}]*\}', '', e)
    e = re.sub(r'\\(?:,|;|!|:)', ' ', e)
    e = re.sub(r'\\(?:Bigg|bigg|Big|big)[lr]?(?=[\(\)\[\]\.|]|\\\{|\\\})', '', e)
    e = re.sub(r'\\(?:left|right)(?=[\(\)\[\]|])', '', e)
    e = re.sub(r'\\(?:left|right)\.', '', e)
    e = re.sub(r'\\(?:left|right)\\([{}])', r'\\\1', e)
    e = e.replace(r'\dfrac', r'\frac').replace(r'\tfrac', r'\frac').replace(r'\cfrac', r'\frac')
    e = e.replace(r'\displaystyle', '').replace(r'\leqq', r'\le').replace(r'\geqq', r'\ge')
    e = re.sub(r'\\mathrm\{d\}', 'd', e)
    e = re.sub(r'\\mathrm\{([A-Za-z])\}', r'\1', e)
    # 組合せ {}_nC_k → \binom{n}{k}
    e = re.sub(r'\{\}_\{?([^{}C]+?)\}?\s*C_\{?([^{}]+?)\}?(?=[^A-Za-z0-9]|$)', r'\\binom{\1}{\2}', e)
    # 度数法
    e = re.sub(r'(\d+(?:\.\d+)?)\s*\^\{?\\circ\}?', r'(\\frac{\1\\pi}{180})', e)
    e = e.strip().rstrip(',.，．')
    e = _wrap_function_args(e)
    # a(b+c) は掛け算。関数名として使う f, g, h, F, G, H だけは関数の値 f(x) とみなす
    e = re.sub(r'(?<![\\A-Za-z_])([A-EI-Za-eij-z])(?=\s*\()', r'\1\\cdot ', e)
    return e.strip()


# ---------------------------------------------------------------------------
# 本文からの定義の拾い上げ（「〜とおく」「〜とする」）
# ---------------------------------------------------------------------------

DEF_RE = re.compile(r'\$\s*(?:と|を)?\s*(?:おく|置く|おける|おいて|とおく|とする|とすると|として)')


def harvest_definitions(text):
    """'$p=\\sin^2\\theta$ とおく' のような定義を {文字: 式} で返す。
    「$\\cos\\theta = c$，$s = \\sin\\theta$とおく」のように同じ文の中に並んだ定義もまとめて拾う。"""
    defs = {}
    for m in DEF_RE.finditer(text):
        start = max(text.rfind('．', 0, m.start()), text.rfind('。', 0, m.start()), text.rfind('\n\n', 0, m.start()))
        sentence = text[start + 1:m.start() + 1]
        segments = re.findall(r'\$([^$]{1,80})\$', sentence)
        for part in (p for seg in segments for p in re.split(r',|，|\\quad', seg)):
            part = re.sub(r'\\[ ,;!:]', ' ', part)
            if part.count('=') != 1:
                continue
            lhs, rhs = (s.strip() for s in part.split('='))
            for name, value in ((lhs, rhs), (rhs, lhs)):
                if re.fullmatch(r'[A-Za-z](?:_\{?[A-Za-z0-9]+\}?)?|\\[a-zA-Z]+', name) and name != value:
                    try:
                        sym = parse_latex(clean(name))
                        val = parse_latex(clean(value))
                    except Exception:
                        continue
                    if isinstance(sym, sp.Symbol) and sym not in val.free_symbols and val.free_symbols:
                        defs[sym] = val
                        break
    return defs


def _auto_trig(a, b):
    """定義が見つからなくても、c と s が両方使われていれば c=cos u, s=sin u とみなす（c^2+s^2=1 を反映）。"""
    syms = a.free_symbols | b.free_symbols
    if {_C, _S} <= syms:
        sub = {_C: sp.cos(_U), _S: sp.sin(_U)}
        return a.subs(sub), b.subs(sub)
    return a, b


def apply_definitions(e, defs):
    for _ in range(4):
        new = e.subs(defs)
        if new == e:
            break
        e = new
    return e


# ---------------------------------------------------------------------------
# 数値比較
# ---------------------------------------------------------------------------

def _sample(symbols, rng):
    sub = {}
    for s in symbols:
        base = str(s).split('_')[0]
        if base in INTEGER_NAMES:
            sub[s] = rng.randint(2, 6)
        else:
            sub[s] = sp.Rational(rng.randint(3, 19), 10)
    return sub


def _value(e, sub):
    v = complex(sp.N(e.subs(sub), 20))
    if v != v or abs(v) == float('inf'):
        raise ValueError
    return v


def _with_imaginary(e):
    i = sp.Symbol('i')
    return e.subs(i, sp.I) if i in e.free_symbols else e


def compare(a, b, rel='=', trials=6, seed=0):
    """True: 成り立つ / False: すべての代入で成り立たない / None: 判定できない。"""
    rng = random.Random(seed)
    syms = sorted(a.free_symbols | b.free_symbols, key=str)
    ok = bad = 0
    witness = None
    for _ in range(trials):
        sub = _sample(syms, rng)
        try:
            va, vb = _value(a, sub), _value(b, sub)
        except Exception:
            continue
        if rel == '=':
            holds = abs(va - vb) <= 1e-8 * max(1, abs(va), abs(vb))
        else:
            if abs(va.imag) > 1e-9 or abs(vb.imag) > 1e-9:
                continue
            x, y = va.real, vb.real
            eps = 1e-9 * max(1, abs(x), abs(y))
            holds = {'<': x < y + eps, '<=': x <= y + eps, '>': x > y - eps, '>=': x >= y - eps}[rel]
        ok += 1
        if not holds:
            bad += 1
            witness = witness or {str(k): str(v) for k, v in sub.items()}
    if ok == 0:
        return None, None
    # 定義域が分からないので、等式・不等式とも「代入したすべての値で成り立たない」ときだけ候補にする
    return (bad < ok), witness


# ---------------------------------------------------------------------------
# align の行の解析
# ---------------------------------------------------------------------------

def split_rows(body, line0):
    """(行番号, 行の中身) を返す。\\quad 以降の注記は切り落とす。"""
    # 括弧の外にある \\ だけで行を区切る（\mqty(a \\ b) の中の \\ では区切らない）
    pieces, depth, start, k = [], 0, 0, 0
    while k < len(body):
        ch = body[k]
        if ch in '({':
            depth += 1
        elif ch in ')}':
            depth -= 1
        elif body.startswith('\\\\', k) and depth <= 0:
            pieces.append((start, body[start:k]))
            start = k + 2
            k += 2
            continue
        k += 1
    pieces.append((start, body[start:]))
    for pos, raw in pieces:
        line = line0 + body[:pos].count('\n')
        row = re.split(r'\\q?quad', raw)[0].replace('&', '')
        # 文末の注記 (p=s^2) のような括弧書きは、関係式を含むなら切り落とす
        row = re.sub(r'\(\s*[^()]*[=<>][^()]*\)\s*$', '', row.strip())
        yield line, row


def split_relations(row):
    """'a = b < c' → [('', a), ('=', b), ('<', c)]。カンマで並べた式は別の式として分ける。"""
    pieces, depth, cur = [], 0, ''
    for ch in row:
        depth += {'{': 1, '}': -1, '(': 1, ')': -1}.get(ch, 0)
        if ch == ',' and depth == 0:
            pieces.append(cur)
            cur = ''
        else:
            cur += ch
    pieces.append(cur)
    if any(p.count('|') % 2 for p in pieces):
        pieces = [row]  # |(x, y)| のような成分表示のカンマでは区切らない
    for piece in pieces:
        yield _split_top_level_relations(piece)


def _split_top_level_relations(piece):
    """括弧の外にある関係記号だけで区切る（\\sum_{k=0}^{n} の = では区切らない）。"""
    depth = 0
    mask = []
    for ch in piece:
        if ch in '{(':
            depth += 1
        elif ch in '})':
            depth -= 1
        mask.append(depth)
    items, last, rel = [], 0, ''
    for m in REL_RE.finditer(piece):
        if mask[m.start()] != 0:
            continue
        items.append((rel, piece[last:m.start()].strip()))
        rel, last = REL_NORM[m.group(1)], m.end()
    items.append((rel, piece[last:].strip()))
    return items


def parse(expr, cache):
    if expr in cache:
        return cache[expr]
    result = None
    if expr and not SKIP_RE.search(expr):
        try:
            with time_limit(2):
                e = _expand_evaluation_brackets(clean(expr))
                result = parse_latex(e)
                if isinstance(result, (sp.Equality, sp.Rel)) or not isinstance(result, sp.Expr):
                    result = None
                elif result.atoms(AppliedUndef):
                    result = None  # f(-1) などの未定義関数の値は比べられない
                else:
                    result = result.subs({sp.Symbol('pi'): sp.pi, sp.Symbol('e'): sp.E})
        except Exception:
            result = None
    cache[expr] = result
    return result


def check_text(text, path='<text>'):
    text = strip_comments(text)
    # 図のコード（数式中の図形アイコンを含む）は比べない。行番号を保つため改行だけ残す
    text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}',
                  lambda m: '\n' * m.group(0).count('\n'), text, flags=re.S)
    if '常用対数' in text or re.search(r'\\log_\{?10', text):
        text = re.sub(r'\\log(?![_A-Za-z])', r'\\log_{10}', text)  # 常用対数の問題では \log は底 10
    defs = harvest_definitions(text)
    cache = {}
    gauss = 'ガウス' in text
    matrix = '行列' in text
    findings = []
    stats = dict(pairs=0, checked=0, flagged=0)

    def report(kind, line, lhs, rel, rhs, witness=None, tier='B'):
        stats['flagged'] += 1
        findings.append(dict(path=path, line=line, kind=kind, tier=tier, lhs=lhs, rel=rel, rhs=rhs, witness=witness))

    def check_pair(line, x, rel, y, first=False, chain_has_eq=True):
        stats['pairs'] += 1
        a, b = parse(x, cache), parse(y, cache)
        if a is None or b is None:
            return
        if matrix and re.search(r'(?<![\\A-Za-z])[A-Z](?![A-Za-z])', x + y):
            return  # 行列の問題の大文字は掛け算の順序を入れ替えられないので比べない
        if gauss and '[' in x + y and ']_' not in x + y:
            return  # ガウス記号 [x] を使う問題の角括弧は比べない
        a2, b2 = apply_definitions(a, defs), apply_definitions(b, defs)
        a2, b2 = _auto_trig(a2, b2)
        try:
            with time_limit(4):
                if rel == '=' and not a2.free_symbols and b2.free_symbols - {sp.Symbol('i')}:
                    if not first and not re.search(r'\\int|\]_|\\right\]|[A-Za-z]_\{?[A-Za-z0-9]+\}?\(', x + y):  # 連鎖の最初の等号は方程式の提示なので対象外
                        stats['checked'] += 1
                        report('NEW', line, x, rel, y)
                    return
                if rel != '=' and (a2.free_symbols or b2.free_symbols):
                    # 文字を含む不等式は定義域が分からず、条件の記述と区別できないので比べない
                    return
                if rel == '=' and a2.free_symbols != b2.free_symbols:
                    # 定義を代入しても使う文字が違う：代入の段階なので比べない
                    return
                stats['checked'] += 1
                holds, witness = compare(a2, b2, rel)
                if holds is False and 'i' in {str(s) for s in a2.free_symbols | b2.free_symbols}:
                    holds, witness = compare(_with_imaginary(a2), _with_imaginary(b2), rel)
                if holds is False:
                    # 文字を含まない数値どうしの比較は文脈に左右されないので確度が高い（A）
                    tier = 'A' if not (a2.free_symbols | b2.free_symbols) else 'B'
                    report('EQ' if rel == '=' else 'INEQ', line, x, rel, y, witness, tier)
        except Timeout:
            pass

    for m in ALIGN_RE.finditer(text):
        line0 = text[:m.start()].count('\n') + 1
        chain = []          # 変形の連鎖 [(行, 関係, 式)]
        equations = []      # 行ごとの方程式 [(行, 左辺, 右辺)]
        for line, row in split_rows(m.group(2), line0):
            cm = CONSEQ_RE.match(row)
            consequence = bool(cm)
            if cm:
                row = row[cm.end():]
            for items in split_relations(row):
                if chain and re.match(r'\s*[+\-]', items[0][1]):
                    # 行頭が演算子：前の行の式が2行にわたって続いている
                    l, r, e = chain[-1]
                    chain[-1] = (l, r, e + ' ' + items[0][1])
                    chain += [(line, r2, e2) for r2, e2 in items[1:]]
                    continue
                if items[0][1] == '' and chain:
                    # 行頭が関係記号：前の行の連鎖の続き
                    chain += [(line, r, e) for r, e in items[1:]]
                    continue
                if len(chain) >= 2:
                    _flush_chain(chain, check_pair)
                if len(items) == 2 and items[1][0] == '=':
                    equations.append((line, items[0][1], items[1][1], consequence))
                else:
                    equations.append(None)
                chain = [(line, r, e) for r, e in items]
        if len(chain) >= 2:
            _flush_chain(chain, check_pair)
        _check_equations(equations, cache, defs, report, stats)
    return findings, stats


def _flush_chain(chain, check_pair):
    # 等号1つだけの行（a = b）は方程式として _check_equations で扱う
    if len(chain) < 3:
        return
    pairs = list(zip(chain, chain[1:]))
    first = chain[0][2].replace(' ', '')
    if NAME_RE.fullmatch(first) and pairs and pairs[0][1][1] == '=':
        pairs = pairs[1:]  # 先頭が名前（V, |PQ|, f(x) など）なら最初の等号は定義
    has_eq = any(r == '=' for _, r, _ in chain[1:])
    first_pair = pairs[0] if pairs and pairs[0] == (chain[0], chain[1]) else None
    for pair in pairs:
        (_, _, x), (line, rel, y) = pair
        check_pair(line, x, rel, y, first=(pair is first_pair), chain_has_eq=has_eq)


def _check_equations(equations, cache, defs, report, stats):
    """行ごとの方程式で、次の行が x = (数値や式) の解の形なら、前の行の方程式を満たすか確かめる。"""
    for e1, e2 in zip(equations, equations[1:]):
        # 「したがって（\therefore など）」で続く行だけを、前の行から導いた解として調べる
        if e1 is None or e2 is None or not e2[3]:
            continue
        (l1, a1, b1, _), (l2, a2, b2, _) = e1, e2
        lhs1, rhs1, lhs2, rhs2 = (parse(s, cache) for s in (a1, b1, a2, b2))
        if None in (lhs1, rhs1, lhs2, rhs2) or not isinstance(lhs2, sp.Symbol):
            continue
        if lhs2 in rhs2.free_symbols:
            continue
        f = apply_definitions(lhs1 - rhs1, defs)
        if lhs2 not in f.free_symbols:
            continue
        stats['pairs'] += 1
        try:
            with time_limit(4):
                g = f.subs(lhs2, apply_definitions(rhs2, defs))
                holds, witness = compare(g, sp.Integer(0), '=')
        except Timeout:
            continue
        stats['checked'] += 1
        if holds is False:
            report('SOLVE', l2, f'{a1} = {b1}', '⇒', f'{a2} = {b2}', witness)


def _check_path(path, file_seconds=60):
    try:
        text = open(path, encoding='utf-8').read()
        with time_limit(file_seconds):
            findings, stats = check_text(text, path)
        return path, findings, stats
    except Timeout:
        return path, [], None
    except Exception as exc:  # 1つのファイルの失敗で全体を止めない
        print(f'{path}: {exc}', file=sys.stderr)
        return path, [], dict(pairs=0, checked=0, flagged=0)


def _run_worker(path, seconds):
    """1ファイルを別プロセスで検査する。SymPy が C の層で止まっても確実に打ち切れるようにするため。"""
    try:
        out = subprocess.run([sys.executable, __file__, '--worker', path], capture_output=True,
                             text=True, timeout=seconds)
        data = json.loads(out.stdout or '{}')
        return path, data.get('findings', []), data.get('stats')
    except subprocess.TimeoutExpired:
        return path, [], None
    except json.JSONDecodeError:
        return path, [], dict(pairs=0, checked=0, flagged=0)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('files', nargs='+')
    ap.add_argument('--json', help='結果を JSON で保存する')
    ap.add_argument('--worker', action='store_true', help=argparse.SUPPRESS)
    ap.add_argument('--file-timeout', type=int, default=90, help='1ファイルあたりの制限時間（秒）')
    ap.add_argument('--jobs', type=int, default=max(1, multiprocessing.cpu_count() - 1), help='並列数')
    ap.add_argument('--tier', choices=['A', 'B'], help='A なら確度の高い候補だけを表示する')
    ap.add_argument('--kinds', default='EQ,NEW,INEQ,SOLVE', help='表示する検査の種類（カンマ区切り）')
    args = ap.parse_args()
    kinds = set(args.kinds.split(','))
    all_findings = []
    total = dict(pairs=0, checked=0, flagged=0)
    timeouts = []
    if args.worker:
        path, findings, stats = _check_path(args.files[0], file_seconds=10 ** 6)
        json.dump(dict(findings=findings, stats=stats), sys.stdout, ensure_ascii=False)
        return
    with ThreadPoolExecutor(args.jobs) as pool:
        results = list(pool.map(lambda p: _run_worker(p, args.file_timeout), args.files))
    for path, findings, stats in results:
        if stats is None:
            timeouts.append(path)
            continue
        for k in total:
            total[k] += stats[k]
        for f in findings:
            if f['kind'] in kinds and (args.tier != 'A' or f['tier'] == 'A'):
                all_findings.append(f)
                w = f"  例: {f['witness']}" if f['witness'] else ''
                print(f"{f['path']}:{f['line']}: [{f['kind']}/{f['tier']}] {f['lhs']}  {f['rel']}  {f['rhs']}{w}")
    if timeouts:
        print(f'制限時間を超えたファイル: {len(timeouts)} 件 ' + ' '.join(timeouts), file=sys.stderr)
    print(f"\n{len(args.files)} ファイル、比較 {total['pairs']} 組、検算 {total['checked']} 組、候補 {len(all_findings)} 件",
          file=sys.stderr)
    if args.json:
        with open(args.json, 'w', encoding='utf-8') as fp:
            json.dump(all_findings, fp, ensure_ascii=False, indent=1)


if __name__ == '__main__':
    main()
