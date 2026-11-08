import pytest
from scratch.check_figure_only_diff import (
    check_figure_only_diff,
    is_figure_only_diff,
)


def test_pure_figure_replacement():
    """figure環境内のTikZコードのみが変更されたケース: PASS"""
    old_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}

\begin{figure}[htb]
  \centering
  \begin{tikzpicture}
    \draw (0, 0) -- (1, 1);
  \end{tikzpicture}
  \caption{古い図}
\end{figure}

ゆえに求める答えは$x=1$である．
\end{document}
"""
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}

\begin{figure}[htb]
  \centering
  \begin{tikzpicture}[>=stealth]
    \coordinate (O) at (0, 0);
    \draw[->, thick] (O) -- (2, 2);
    \node[circle, fill, inner sep=1.2pt] at (O) {};
  \end{tikzpicture}
  \caption{新しい図}
  \label{fig:new}
\end{figure}

ゆえに求める答えは$x=1$である．
\end{document}
"""
    result = check_figure_only_diff(old_tex, new_tex)
    assert result.is_figure_only is True
    assert is_figure_only_diff(old_tex, new_tex) is True
    assert result.non_figure_diff == ""


def test_zahyou_to_figure_replacement():
    """旧式 emath zahyou 環境から figure への置き換え: PASS"""
    old_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{zahyou}[ul=5mm](-2,2)(-2,2)
  \draw (0, 0) -- (1, 1);
\end{zahyou}
したがって答えは$2$である．
\end{document}
"""
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \centering
  \begin{tikzpicture}
    \draw (0, 0) -- (1, 1);
  \end{tikzpicture}
  \caption{グラフ}
\end{figure}
したがって答えは$2$である．
\end{document}
"""
    assert is_figure_only_diff(old_tex, new_tex) is True


def test_center_includegraphics_to_figure_replacement():
    """center + includegraphics + vspace から figure への置き換え: PASS"""
    old_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
交線は$x=2a$となり，下図のようになる．
\vspace{-3\zh}
\begin{center}
  \includegraphics[scale=0.5]{ut-73-1.eps}
\end{center}
\vspace{2\zh}
$P$が見えるのは$2a\le x$の領域である．
\end{document}
"""
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
交線は$x=2a$となり，下図のようになる．

\begin{figure}[htb]
  \centering
  \begin{tikzpicture}
    \draw (0, 0) -- (1, 1);
  \end{tikzpicture}
  \caption{空間図形}
\end{figure}

$P$が見えるのは$2a\le x$の領域である．
\end{document}
"""
    assert is_figure_only_diff(old_tex, new_tex) is True


def test_todo_to_figure_replacement():
    """% TODO: 概要図 から figure への置き換え: PASS"""
    old_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}

% TODO: 概要図

これより最大値は$a=1$である．
\end{document}
"""
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}

\begin{figure}[htb]
  \centering
  \begin{tikzpicture}
    \draw (0, 0) -- (1, 1);
  \end{tikzpicture}
  \caption{概要図}
\end{figure}

これより最大値は$a=1$である．
\end{document}
"""
    assert is_figure_only_diff(old_tex, new_tex) is True


def test_text_modification_fails():
    """本文の文字や数式が変更されたケース: FAIL"""
    old_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \draw (0, 0) -- (1, 1);
\end{figure}
ゆえに $x = 1$ である．
\end{document}
"""
    # 本文の $x = 1$ が $x = 2$ に変更されている
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \draw (0, 0) -- (2, 2);
\end{figure}
ゆえに $x = 2$ である．
\end{document}
"""
    result = check_figure_only_diff(old_tex, new_tex)
    assert result.is_figure_only is False
    assert "-ゆえに $x = 1$ である．" in result.non_figure_diff
    assert "+ゆえに $x = 2$ である．" in result.non_figure_diff


def test_format_conversion_fails():
    """jarticle から subfiles へのヘッダー移行が含まれるケース: FAIL"""
    old_tex = r"""\documentclass[a4j]{jarticle}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \draw (0, 0) -- (1, 1);
\end{figure}
答えは$1$．
\end{document}
"""
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \draw (0, 0) -- (2, 2);
\end{figure}
答えは$1$．
\end{document}
"""
    result = check_figure_only_diff(old_tex, new_tex)
    assert result.is_figure_only is False
    assert r"-\documentclass[a4j]{jarticle}" in result.non_figure_diff
    assert r"+\documentclass[../../main.tex]{subfiles}" in result.non_figure_diff


def test_cref_modification_fails():
    """数式参照の変更が含まれるケース: FAIL"""
    old_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \draw (0, 0) -- (1, 1);
\end{figure}
\cref{eq:1}，\cref{eq:2}より求まる．
\end{document}
"""
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \draw (0, 0) -- (2, 2);
\end{figure}
\cref{eq:1,eq:2}より求まる．
\end{document}
"""
    result = check_figure_only_diff(old_tex, new_tex)
    assert result.is_figure_only is False
    assert r"-\cref{eq:1}，\cref{eq:2}より求まる．" in result.non_figure_diff
    assert r"+\cref{eq:1,eq:2}より求まる．" in result.non_figure_diff


def test_heading_modification_fails():
    """見出しの変更が含まれるケース: FAIL"""
    old_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf[解]}
\begin{figure}[htb]
  \draw (0, 0) -- (1, 1);
\end{figure}
答えは$1$．
\end{document}
"""
    new_tex = r"""\documentclass[../../main.tex]{subfiles}
\begin{document}
{\bf [解答]}
\begin{figure}[htb]
  \draw (0, 0) -- (2, 2);
\end{figure}
答えは$1$．
\end{document}
"""
    result = check_figure_only_diff(old_tex, new_tex)
    assert result.is_figure_only is False
    assert r"-{\bf[解]}" in result.non_figure_diff
    assert r"+{\bf [解答]}" in result.non_figure_diff
