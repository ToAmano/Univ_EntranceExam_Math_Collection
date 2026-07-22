---
university: "ukyoto"
category: "kouki"
year: "2006"
question: "6"
type: "solution"
title: "UKYOTO 2006 kouki Q6 (solution)"
---

## 【解】

  $\tan 1^\circ$ が有理数と仮定して背理法により題意を示す．
  以下 $\tan \theta^\circ (\theta=1,2,\dots,89)$ が有理数であることを帰納的に示す．
  $\theta=1^\circ$ の時は仮定から成立するので，$\theta=k^\circ \in \mathbb{N}$ での成立を仮定し，$\theta=k+1^\circ$ でも成立することを示す．
  $\tan\theta$の加法定理から
  

$$
\begin{align*}
\tan(k+1)^\circ
    = \frac{\tan 1^\circ + \tan k^\circ}{1 - \tan 1^\circ \tan k^\circ}\in\mathbb{Q}\quad(\because\text{仮定})
\end{align*}
$$

  から $\theta=k+1^\circ$ でも成立．
  以上から $\tan \theta^\circ \in \mathbb{Q} (\theta=1,2,\dots,89)$．

  しかし，$\theta=60^\circ$ とすると $\tan 60^\circ = \sqrt{3} \notin \mathbb{Q}$ となり，矛盾．

  従って，$\tan 1^\circ \notin \mathbb{Q}$ である．$\cdots$(答)

  
  

## 【解説】