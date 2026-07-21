---
university: "kyodai"
category: "kouki"
year: "2006"
question: "5"
type: "solution"
title: "KYODAI 2006 kouki Q5 (solution)"
---

## 【解】

  

<figure id="fig_1">
  <img src="/Univ_EntranceExam_Math_Collection/images/tikz/kyodai/kouki/2006/5/fig_1.svg" alt="図 1" />
  <figcaption>図 1: 円錐</figcaption>
</figure>

  容器は底面半径$R$高さ$H$の円錐を逆向きにしたものである．
  水面の底からの高さ$h$の時の水面の面積$S(h)$として，題意の条件は
  
$$
\begin{align}
\sqrt{h} = -S \frac{dh}{dt}\label{2006-5:eq:1}
\end{align}
$$

  と書き表せる．

  高さ$h$の時の円錐の半径は
  
$$
\begin{align*}
R\frac{h}{H}
\end{align*}
$$

  だから，$S(h)$はこの半径を持つ円の面積で
  
$$
\begin{align*}
S(h) = \pi R^2 \left(\frac{h}{H}\right)^2
\end{align*}
$$

  であり，$\eqref{2006-5:eq:1}$に代入して
  
$$
\begin{align}
\sqrt{h}& = -\pi\frac{R^2}{H^2} h^2 \frac{dh}{dt}\nonumber\\
    dt       & = -\frac{\pi R^2}{H^2} h^{3/2} dh \label{2006-5:eq:2}
\end{align}
$$

  を得る．両辺積分して，積分定数を$C$とおくと
  
$$
\begin{align*}
t = -\frac{\pi R^2}{H^2}\frac{2}{5} h^{5/2} + C
\end{align*}
$$

  初期条件は$t=0$の時，$h=H$だから
  
$$
\begin{align*}
C= \frac{2}{5}\pi R^2 \sqrt{H}
\end{align*}
$$

  なので，
  
$$
\begin{align*}
t = -\frac{\pi R^2}{H^2}\frac{2}{5} h^{5/2} + \frac{2}{5}\pi R^2 \sqrt{H}
\end{align*}
$$

  となる．$h=0$となるときの$t$は従って，
  
$$
\begin{align*}
t = \frac{2}{5}\pi R^2 \sqrt{H}
\end{align*}
$$

  である． $\cdots$(答)

  
  

## 【解説】

  問題文からは，先に$V(t)$を求めてから微分方程式を立ててほしい，という意図を感じる．
  しかしながら，その方法は一回積分をしてから方程式を立てるため，少し回り道であるため
  今回の回答では直接排出速度について式を立てる方針とした．

  一応題意に沿ってやるとどうなるかを見せるため，以下$V(t)$を出すことで微分方程式を導出しよう．
  時刻$t$での高さ$h$とすると，$V(t)$は高さ$H$の円錐の体積から高さ$h$の円錐の体積を引いたものであり，
  
$$
\begin{align*}
V(t)
     & = \frac{1}{3}\pi H R^2 - \frac{1}{3}\pi\left(\frac{h}{H}R\right)^2 h \\& = \frac{1}{3}\pi H R^2 - \frac{1}{3}\pi\frac{R^2}{H^2} h^3
\end{align*}
$$

  と表せる．
  両辺$t$で微分すると
  
$$
\begin{align*}
\frac{dV}{dt} = -\pi\frac{R^2}{H^2} h^2 \frac{dh}{dt}
\end{align*}
$$

  ここに題意より$dV/dt=\sqrt{h}$を代入して
  
$$
\begin{align*}
-\pi\frac{R^2}{H^2} h^{3/2} dh = dt
\end{align*}
$$

  を得る．これは$\eqref{2006-5:eq:2}$と同じ方程式であるから，以下全く同様に解ける．

  以上の導出でわかるように，いちいち$V(t)$を出すよりも直接水面の面積を利用して立式した方が早いということが理解できる．