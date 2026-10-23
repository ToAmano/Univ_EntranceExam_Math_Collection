"""Read and rewrite literal LaTeX labels and references without touching comments."""

import re
from collections import Counter


COMMAND_RE = re.compile(r'(?<!\\)\\(label|cref|Cref|ref|eqref)\s*\{([^{}]*)\}')
VERBATIM_RE = re.compile(r'\\begin\{(verbatim\*?|Verbatim|lstlisting|minted)\}')
INLINE_VERB_RE = re.compile(r'\\verb\*?([^a-zA-Z\s])')
EQUATION_RE = re.compile(r'eq:')
MATH_ENV_RE = re.compile(
    r'\\begin\{(align\*?|equation\*?|gather\*?|multline\*?|eqnarray\*?|flalign\*?|alignat\*?|subequations)\}'
    r'.*?\\end\{\1\}', re.DOTALL)


class AmbiguousLabelError(ValueError):
    """A duplicate source label prevents unambiguous reference rewriting."""


def visible_text(source):
    """Blank comments and verbatim text while retaining every character offset."""
    chars = list(source)
    i = 0
    while i < len(source):
        inline = INLINE_VERB_RE.match(source, i)
        if inline:
            end = source.find(inline.group(1), inline.end())
            end = len(source) if end < 0 else end + 1
            chars[i:end] = ' ' * (end - i)
            i = end
            continue
        verbatim = VERBATIM_RE.match(source, i)
        if verbatim:
            end_token = '\\end{' + verbatim.group(1) + '}'
            end = source.find(end_token, verbatim.end())
            end = len(source) if end < 0 else end + len(end_token)
            chars[i:end] = ' ' * (end - i)
            i = end
            continue
        if source[i] == '\\' and i + 1 < len(source):
            i += 2
            continue
        if source[i] == '%':
            end = source.find('\n', i)
            end = len(source) if end < 0 else end
            chars[i:end] = ' ' * (end - i)
            i = end
            continue
        i += 1
    return ''.join(chars)


def commands(source):
    masked = visible_text(source)
    for match in COMMAND_RE.finditer(masked):
        yield match.group(1), source[match.start(2):match.end(2)], match.start(2), match.end(2)


def references(argument):
    return [part.strip() for part in argument.split(',')]


def math_label_positions(source):
    masked = visible_text(source)
    spans = [(match.start(), match.end()) for match in MATH_ENV_RE.finditer(masked)]
    return {start for command, _, start, _ in commands(source)
            if command == 'label' and any(begin <= start < end for begin, end in spans)}


def replace_arguments(source, replacements):
    for start, end, value in sorted(replacements, reverse=True):
        source = source[:start] + value + source[end:]
    return source


def normalize_equation_labels(source):
    math_positions = math_label_positions(source)
    labels = [name for command, name, start, _ in commands(source)
              if command == 'label' and (EQUATION_RE.search(name) or start in math_positions)
              and ',' not in name]
    repeated = [name for name, count in Counter(labels).items() if count > 1]
    if repeated:
        raise AmbiguousLabelError('duplicate equation label: ' + ', '.join(repeated))
    mapping = {name: 'eq:' + str(index) for index, name in enumerate(labels, 1)}
    changes = []
    for command, argument, start, end in commands(source):
        if command == 'label':
            replacement = mapping.get(argument, argument)
        else:
            replacement = ','.join(
                part[:len(part) - len(part.lstrip())]
                + mapping.get(part.strip(), part.strip())
                + part[len(part.rstrip()):]
                for part in argument.split(','))
        if replacement != argument:
            changes.append((start, end, replacement))
    return replace_arguments(source, changes)


def namespace_references(source, prefix):
    changes = []
    for command, argument, start, end in commands(source):
        if command == 'label':
            replacement = prefix + ':' + argument
        else:
            replacement = ','.join(
                part[:len(part) - len(part.lstrip())]
                + prefix + ':' + part.strip()
                + part[len(part.rstrip()):]
                for part in argument.split(','))
        changes.append((start, end, replacement))
    return replace_arguments(source, changes)
