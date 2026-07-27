---
university: "ukyoto"
category: "zenki"
year: "1982"
question: "6"
type: "solution"
title: "UKYOTO 1982 zenki Q6 (solution)"
---

\begin{flushright}
\footnotesize\textit{【自動文字起こし・要確認】}
\end{flushright}

(1) $-1 \le x \le 0$ の時、
$$ f(x) = \int_x^0 t e^t dt + \int_0^{x+1} t e^{-t} dt 
$$
より、
$$
 f'(x) = -x e^x + (x+1) e^{-x-1} 
$$
$= e^{-x} \left[ \frac{1}{e}(x+1) - x e^{2x} \right] \ge 0 \quad (\because -1 \le x \le 0) から、f(x)$は単調増加で、
$$
 f(-1) \le f(x) \le f(0) \quad (-1 \le x \le 0) 
$$
(2) 0 \le x の時 f(x) = \int_x^{x+1} t e^{-t} dt だから、
$$
 f'(x) = (x+1) e^{-x-1} - x e^{-x} 
$$
$= e^{-x-1} \left[ (1-e)x + 1 \right] 
x \le -1の時、f(x) = \int_x^{x+1} t e^t dt$ だから
$$
 f'(x) = (x+1) e^{x+1} - x e^x 
$$
$= e^x \left[ (e-1)x + e \right] から増減表をえる

| x| \cdots| \frac{-e}{e-1}| \cdots| -1| \cdots| 0| \cdots| \frac{1}{e-1}| \cdots|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| f'| -| 0| +|  | +|  | +| 0| -|
| f| \searrow|  | \nearrow| \nearrow| \nearrow| \nearrow| \nearrow|  | \searrow|

これで \lim_{x \to \infty} f(x) = 0, \lim_{x \to -\infty} f(x) = 0, f\left(\frac{-e}{e-1}\right) = e^{\frac{-e}{e-1}}(1-e) < 0
f\left(\frac{1}{e-1}\right) = (e-1) e^{-\frac{1}{e-1}-1} > 0$ から、
$$
 \max \cdots x = \frac{1}{e-1} $$
$$ \min \cdots x = \frac{-e}{e-1} $$