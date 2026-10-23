import unittest

from scratch import tex_references as refs


def test_normalize_equations_renames_definitions_and_all_reference_forms():
    source = (r'\label{2004-2:eq:7} \cref{2004-2:eq:7,eq:foo} '
              r'\label{eq:foo} \ref{eq:foo} \eqref{2004-2:eq:7}'
              '\n% \\label{eq:comment} \\cref{eq:foo}\n')
    expected = (r'\label{eq:1} \cref{eq:1,eq:2} '
                r'\label{eq:2} \ref{eq:2} \eqref{eq:1}'
                '\n% \\label{eq:comment} \\cref{eq:foo}\n')
    assert refs.normalize_equation_labels(source) == expected


def test_normalize_equations_rejects_duplicate_old_names():
    with unittest.TestCase().assertRaises(refs.AmbiguousLabelError):
        refs.normalize_equation_labels(r'\label{eq:1} \label{eq:1} \cref{eq:1}')


def test_namespacing_preserves_lists_and_non_reference_text():
    source = (r'\label{eq:1} \label{fig:a} '
              r'\cref{eq:1, fig:a} \Cref{fig:a} \ref{eq:1} \eqref{eq:1}')
    expected = (r'\label{titech:zenki:2004:2:eq:1} '
                r'\label{titech:zenki:2004:2:fig:a} '
                r'\cref{titech:zenki:2004:2:eq:1, titech:zenki:2004:2:fig:a} '
                r'\Cref{titech:zenki:2004:2:fig:a} '
                r'\ref{titech:zenki:2004:2:eq:1} '
                r'\eqref{titech:zenki:2004:2:eq:1}')
    assert refs.namespace_references(source, 'titech:zenki:2004:2') == expected


def test_literal_tex_and_comments_are_not_rewritten():
    source = (r'\verb|\label{eq:1}| ' + '\n'
              + r'\begin{verbatim}\cref{eq:1}\end{verbatim}' + '\n'
              + r'% \label{eq:1}' + '\n'
              + r'\label{eq:1}')
    expected = source[:-len(r'\label{eq:1}')] + r'\label{x:y:eq:1}'
    assert refs.namespace_references(source, 'x:y') == expected


def test_normalize_math_environment_labels_without_eq_prefix():
    source = (r'\begin{align}x=1\label{old_1}\end{align} '
              r'\cref{old_1} \begin{figure}\label{fig:a}\end{figure}')
    expected = (r'\begin{align}x=1\label{eq:1}\end{align} '
                r'\cref{eq:1} \begin{figure}\label{fig:a}\end{figure}')
    assert refs.normalize_equation_labels(source) == expected
