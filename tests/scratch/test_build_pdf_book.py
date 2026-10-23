from scratch.build_pdf_book import prepare_book


def test_prepare_book_namespaces_problem_and_solution_without_changing_sources(tmp_path):
    source = tmp_path / 'src' / 'titech' / 'zenki'
    question = source / '2004' / '2'
    question.mkdir(parents=True)
    (source / 'main.tex').write_text(r'\subfile{2004/2/problem}' + '\n')
    (question / 'problem.tex').write_text(r'\label{fig:a}')
    (question / 'solution.tex').write_text(r'\cref{fig:a} \label{eq:1} \eqref{eq:1}')
    (question / 'diagram.svg').write_text('<svg/>')
    (source / 'main.pdf').write_text('keep original PDF')
    (source / 'main.aux').write_text('keep original aux')
    destination = tmp_path / 'staged'

    prepare_book(source, destination, 'titech', 'zenki')

    assert (destination / '2004/2/problem.tex').read_text() == r'\label{titech:zenki:2004:2:fig:a}'
    assert (destination / '2004/2/solution.tex').read_text() == (
        r'\cref{titech:zenki:2004:2:fig:a} '
        r'\label{titech:zenki:2004:2:eq:1} '
        r'\eqref{titech:zenki:2004:2:eq:1}')
    assert (question / 'solution.tex').read_text() == r'\cref{fig:a} \label{eq:1} \eqref{eq:1}'
    assert (destination / '2004/2/diagram.svg').read_text() == '<svg/>'
    assert not (destination / 'main.pdf').exists()
    assert not (destination / 'main.aux').exists()
