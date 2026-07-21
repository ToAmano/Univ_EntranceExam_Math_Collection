---
university: "sample_titech"
category: "kouki"
year: "1995"
question: "0"
type: "summary"
title: "1995年 全体サマリ"
---

% \documentclass[a4paper,12pt]{article}
% \usepackage[utf8]{inputenc}
% \usepackage[japanese]{babel}
% \usepackage{xeCJK}
% \usepackage{geometry}
% \usepackage{array}
% \usepackage{booktabs}
% \usepackage{fancybox}

% % ページ設定
% \geometry{top=25mm, bottom=25mm, left=20mm, right=20mm}
% \pagestyle{empty}

% % フォント設定
% \setCJKmainfont{Noto Sans CJK JP}

% \begin{document}

% 年度の大きな表示
\begin{center}{\fontsize{48pt}{58pt}\selectfont \textbf{1995}\normalsize\textbf{年度}}
\end{center}

% 本文

% 出題テーマと難易度の表
\noindent\textbf{出題テーマと難易度}

\begin{center}
  \shadowbox{%
    \begin{tabular}{|c|p{8cm}|c|}
      \hline
      \textbf{問題番号} & \textbf{テーマ} & \textbf{難易度} \\
      \hline
      第1問           & 空間図形，極限      & 普            \\
      \hline
      第2問           & 平面図形         & 普            \\
      \hline
    \end{tabular}%
  }
\end{center}

% 解答
\noindent\textbf{解答}

\begin{center}
  \shadowbox{%
    \renewcommand{\arraystretch}{1.6}
    \begin{tabular}{|c|c|p{8cm}|}
      \hline
      \textbf{問題番号}        & \textbf{小問} & \textbf{答え}                                        \\
      \hline
      \multirow{2}{*}{第1問} & (1)         & $\displaystyle r_n = (2-\sqrt{3})^n$               \\
      \cline{2-3}
                           & (2)         & $\displaystyle V = 8 - \frac{6\sqrt{3}+10}{15}\pi$ \\
      \hline
      \multirow{2}{*}{第2問} & (1)         & $\displaystyle X^2+Y^2=a^2+1$                      \\
      \cline{2-3}
                           & (2)         & $\displaystyle V=4\pi^2a (a^2-a+1)$                \\
      \hline
    \end{tabular}%
    \renewcommand{\arraystretch}{1.0}
  }
\end{center}

% 解答時間
\noindent\textbf{試験形態}

\begin{center}
  \shadowbox{%
    \begin{tabular}{p{8cm}}
      2問60分
    \end{tabular}%
  }
\end{center}