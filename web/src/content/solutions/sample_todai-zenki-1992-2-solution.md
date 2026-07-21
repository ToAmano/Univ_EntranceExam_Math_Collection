---
university: "sample_todai"
category: "zenki"
year: "1992"
question: "2"
type: "solution"
title: "SAMPLE_TODAI 1992 zenki Q2 (solution)"
---

**【解】**

### (1)

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          view={100}{25},   
          axis lines=center, 
          ticks=none,        
          xlabel=$x$, ylabel=$y$, zlabel=$z$, 
          xmin=-5, xmax=2,
          ymin=-1, ymax=4,
          zmin=-1, zmax=3.5,
          xtick={\empty},ytick={\empty},ztick={\empty},
          clip=false         
        ]

        \def\angleTheta{120} 
        \coordinate (B) at (0,0,0);      
        \coordinate (A) at (-2,3,0);      
        \coordinate (Aprime) at (-2,0,0);
        \coordinate (Cprime) at (-4,0,0); 

        \coordinate (C) at (-4, {3*cos(\angleTheta)}, {3*sin(\angleTheta)});

        \addplot3[surf, fill=gray, fill opacity=0.9]
        coordinates {(-5,-0.5,0) (4,-0.5,0) (4,3.5,0) (-5,3.5,0) (-5,-0.5,0)};
        \addplot3[surf, fill=gray, fill opacity=0.1]
        coordinates {
            (-5,0,0) (4,0,0)
            (4, {3.5*cos(\angleTheta)}, {3.5*sin(\angleTheta)})
            (-5, {3.5*cos(\angleTheta)}, {3.5*sin(\angleTheta)})
            (-5,0,0)
          };

        \draw[thick] (A) -- (B);
        \draw[thick] (B) -- (C);

        \draw[dashed] (A) -- (Aprime);
        \draw[dashed] (C) -- (Cprime);
        \draw[dashed] (A) -- (C);

        \fill (A) circle (1.5pt);
        \fill (B) circle (1.5pt);
        \fill (Cprime) circle (1.5pt);
        \fill (C) circle (1.5pt);
        \node[right] at (A) {A};
        \node[below] at (B) {B};
        \node[above] at (C) {C};
        \node[right] at (Cprime) {C'};

        \coordinate (pY) at (4,1.5,0);
        \coordinate (pH2) at (4, {1.5*cos(\angleTheta)}, {1.5*sin(\angleTheta)});
        \coordinate (p3) at (4,0,0);
        \pic[draw, "$\theta$", angle eccentricity=1.3, angle radius=0.8cm] {angle = pY--p3--pH2};

        \node at (3,0.5,0) {$H_1$};
        \node at (0, {2.5*cos(\angleTheta)}, {2.5*sin(\angleTheta)}) {$H_2$};
        \node at (-6, 0, 0) {$L$};

      \end{axis}
    \end{tikzpicture}
    \caption{平面$H_1,H_2$の様子．}
    \label{1992-2:fig:1}
  \end{figure}

  $L$を$x$軸, $H_1$を$xy$平面, Bを原点とし,
  $H_2$が$z \geqq 0$になるように空間座標をおく．
  $H_1$と$H_2$のなす角を$\theta$とおく．
  $C$から$L$に下ろした垂足を$C'$とし，その座標をC'($p, 0, 0$)とする．

  $CC' = q (q>0)$ とおくと，
  
$$
\begin{align*}
    C(p, q\cos\theta, q\sin\theta)
  \end{align*}
$$

  とおける．

  さらに A($a, b, 0$) ($b>0$) とおくと，$\overline{AC}$の長さは
  
$$
\begin{align*}
    \overline{AC}^2
     & = (a-p)^2 + (b-q\cos\theta)^2 + q^2\sin^2\theta \\
     & = -2bq\cos\theta + q^2+b^2+(a-p)^2
  \end{align*}
$$

  と書ける．

  さて，$\angle ABC=\alpha\, (0 \le \alpha \le \pi)$とおいて$\triangle ABC$に余弦定理を用いると
  
$$
\begin{align*}
    \cos\alpha
     & = \frac{\overline{AB}^2+\overline{BC}^2-\overline{AC}^2}{2\overline{AB} \cdot \overline{BC}}                                                              \\
     & = \frac{\overline{AB}^2+\overline{BC}^2}{2\overline{AB} \cdot \overline{BC}} + \frac{2bq\cos\theta - q^2-b^2-(a-p)^2}{2\overline{AB} \cdot \overline{BC}}
  \end{align*}
$$

  と書ける．

  $\theta$の変化によって$\overline{AB}, \overline{BC}$は変化しないから，
  
$$
\begin{align*}
    \cos\alpha
     & = (\text{定数})  + \frac{bq}{\overline{AB} \cdot \overline{BC}} \cos\theta
  \end{align*}
$$

  と書ける．

  従って，$0 \leqq \theta \leqq \pi$で$\cos\theta$は単調減少で，$\frac{bq}{AB \cdot BC} > 0$から
  $\cos\alpha$は$\theta$の単調減少関数である．
  $0 \leqq \alpha \leqq \pi$とあわせて$\alpha$は$\theta$の単調増加関数である．
  よって題意は示された．$\cdots$(答)

### (2)

  どの点が同一直線上にあるかで場合分けして考える．

  
  **1° A,B,C,Dが同一直線上の時**

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          axis equal,
          hide axis,
          xmin=-1, xmax=5,
          ymin=-1, ymax=1,
          clip=false,
        ]
        \addplot [
          black,      
          mark=*,      
          only marks  
        ] coordinates {
            (0,0)
            (2,1)
            (3,1.5)
            (5,2.5)
          };

        \draw (axis cs:0,0) -- (axis cs:5,2.5);

        \node [below left] at (axis cs:0,0) {A};
        \node [below] at (axis cs:2,1) {B};
        \node [below right] at (axis cs:3,1.5) {C};
        \node [below right] at (axis cs:5,2.5) {D};
      \end{axis}
    \end{tikzpicture}
    \caption{1° A,B,C,Dが同一直線上の時}
    \label{1992-2:fig:2}
  \end{figure}

  対称性から\cref{1992-2:fig:2}の時だけ考える．
  
$$
\begin{align*}
    \angle ABC + \angle BCD + \angle CDA + \angle DAB = 2\pi
  \end{align*}
$$

  だから与式は成立する．

  
  **2° AからDのうち3つが同一直線上の時**

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          axis equal, 
          hide axis,  
          xmin=-1.5, xmax=3, 
          ymin=-1, ymax=2.5  
        ]
        \coordinate (A) at (0, 2);
        \coordinate (B) at (-1, 0);
        \coordinate (D) at (2.5, 0.5);

        \coordinate (C) at ($(B)!0.4!(D)$);

        \draw (A) -- (B) -- (D) -- cycle;
        \draw[dashed] (A) -- (C);

        \fill (A) circle (2pt);
        \fill (B) circle (2pt);
        \fill (C) circle (2pt);
        \fill (D) circle (2pt);

        \node [above] at (A) {A};
        \node [below left] at (B) {B};
        \node [below right] at (C) {C};
        \node [below right] at (D) {D};
      \end{axis}
    \end{tikzpicture}
    \caption{2° AからDのうち3つが同一直線上の時}
    \label{1992-2:fig:3}
  \end{figure}

  対称性から図の時だけ考える．
  
$$
\begin{align*}
    \angle ABC + \angle BCD + \angle CDA + \angle DAB = \pi + \pi = 2\pi
  \end{align*}
$$

  だから与式は成立する．

  
  **3° どの3点も同一直線上にない時**

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          view={100}{25},   
          axis lines=center, 
          ticks=none,        
          xlabel=$x$, ylabel=$y$, zlabel=$z$, 
          xmin=-8, xmax=0,
          ymin=-1, ymax=4,
          zmin=-1, zmax=3.5,
          xtick={\empty},ytick={\empty},ztick={\empty},
          clip=false         
        ]

        \def\angleTheta{120} 
        \coordinate (A) at (0,0,0);      
        \coordinate (B) at (-2,3,0);      
        \coordinate (C) at (-7,0,0);      
        \coordinate (Aprime) at (-2,0,0);
        \coordinate (Cprime) at (-4,0,0); 

        \coordinate (D) at (-4, {3*cos(\angleTheta)}, {3*sin(\angleTheta)});

        \addplot3[surf, fill=gray, fill opacity=0.9]
        coordinates {(-8,-0.5,0) (4,-0.5,0) (4,3.5,0) (-8,3.5,0) (-8,-0.5,0)};
        \addplot3[surf, fill=gray, fill opacity=0.1]
        coordinates {
            (-8,0,0) (4,0,0)
            (4, {3.5*cos(\angleTheta)}, {3.5*sin(\angleTheta)})
            (-8, {3.5*cos(\angleTheta)}, {3.5*sin(\angleTheta)})
            (-8,0,0)
          };

        \draw[thick] (A) -- (B) -- (C) -- (D) -- cycle;

        \fill (A) circle (1.5pt);
        \fill (B) circle (1.5pt);
        \fill (C) circle (1.5pt);
        \node[below right] at (A) {A};
        \node[below] at (B) {B};
        \node[above] at (C) {C};
        \node[above] at (D) {D};

        \coordinate (pY) at (4,1.5,0);
        \coordinate (pH2) at (4, {1.5*cos(\angleTheta)}, {1.5*sin(\angleTheta)});
        \coordinate (p3) at (4,0,0);
        \pic[draw, "$\theta$", angle eccentricity=1.3, angle radius=0.8cm] {angle = pY--p3--pH2};

        \node at (3,2,0) {$H_1$};
        \node at (0, {2.5*cos(\angleTheta)}, {2.5*sin(\angleTheta)}) {$H_2$};
        \node at (-9, 0, 0) {$L$};

        \pic[draw, angle eccentricity=1.3, angle radius=0.2cm] {angle = B--A--D};
        \pic[draw, angle eccentricity=1.3, angle radius=0.6cm] {angle = A--D--C};
        \pic[draw, angle eccentricity=1.3, angle radius=0.2cm] {angle = D--C--B};
        \pic[draw, angle eccentricity=1.3, angle radius=0.6cm] {angle = C--B--A};

      \end{axis}
    \end{tikzpicture}
    \caption{3° どの3点も同一直線上にない時}
    \label{1992-2:fig:4}
  \end{figure}

  直線ACをLとしてLを共通の境界とし，角$\theta(0 \leqq \theta \leqq \pi)$で交わる
  2半平面$H_1$, $H_2$上のLと異なる所に各々点B, Dをとることが出来る．

  この時$3$点(B,C,D), (A,B,D)に(1)の議論を用いることが出来る．
  まず平面$H_1,H_2$上でA,B,C,Dを固定して$\theta$を$0 \leqq \theta \leqq \pi$で動かす．
  この時
  $\angle ABC$, $\angle CDA$は一定で，(1)から
  $\angle DAB$, $\angle BCD$は$\theta$の単調増加関数だから
  $\angle ABC + \angle BCD + \angle CDA + \angle DAB$は$\theta=\pi$で最大値をとる．
  この時4点A,B,C,Dはどの3点も同一直線上にないことから四角形ABCDを構成する．
  この時直線ACに関してB, Dが反対側にあることから各点の関係は\cref{1992-2:fig:5}のようになる．

  \begin{figure}[H]
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          axis equal, 
          hide axis,  
          xmin=-1.5, xmax=4.5, 
          ymin=-2.5, ymax=2.5  
        ]
        \coordinate (A) at (0, 0);
        \coordinate (B) at (2.5, -1.5);
        \coordinate (C) at (3.5, 0.75);
        \coordinate (D) at (1, 1.8);

        \draw (A) -- (B) -- (C) -- (D) -- cycle;

        \draw ($(A)!-0.4!(C)$) -- ($(A)!1.2!(C)$);

        \fill (A) circle (2pt);
        \fill (B) circle (2pt);
        \fill (C) circle (2pt);
        \fill (D) circle (2pt);

        \node [below left] at (A) {A};
        \node [below] at (B) {B};
        \node [right] at (C) {C};
        \node [above] at (D) {D};
      \end{axis}
    \end{tikzpicture}
    \caption{点ABCDの関係}
    \label{1992-2:fig:5}
  \end{figure}

  よって条件をみたすもとでA〜Dをうごかしても，四角形の内角の和は$2\pi$で一定だから
  
$$
\begin{align*}
    \angle ABC + \angle BCD + \angle CDA + \angle DAB = 2\pi
  \end{align*}
$$

  よって与式は成立する．

  
  以上1°〜3°で全ての場合は尽くされ，題意は示された．$\cdots$(答)
  

  **【解説】**