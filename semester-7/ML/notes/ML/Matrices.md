---
tags:
  - term
  - math
---

A list of [[Vectors]]. Multiple Matrices are called [[Tensors]]

## Math
### Vectors to matrix
The conversion of 3 vectors $u$, $v$, and $w$ looks like:
$$
u = \begin{bmatrix*}[r] 1\\ -1\\ 1\\\end{bmatrix*}\qquad v=\begin{bmatrix*}[r] 0\\ 1\\ -1\\\end{bmatrix*}\qquad w=\begin{bmatrix*}[r] 0\\ 0\\ 1\\\end{bmatrix*}
$$
Combines to:
$$
\begin{bmatrix*}[r]
  1 & 0 & 0\\
  -1 & 1 & 0\\
  1 & -1 & 1\\
\end{bmatrix*}
$$

### Combinatorics
The linear combination in three dimensional space $x_1 u+x_2 v+x_3 w$ translates to
$$
x_1 \begin{bmatrix*}[r] 1\\ -1\\ 1\\\end{bmatrix*} + x_2\begin{bmatrix*}[r] 0\\ 1\\ -1\\\end{bmatrix*} + x_3\begin{bmatrix*}[r] 0\\ 0\\ 1\\\end{bmatrix*} = \begin{bmatrix*}[l]
  x_1\\
  x_2 - x_1\\
  x_3 - x_2\\
\end{bmatrix*}
$$

This operation can also be written as a vector on matrix combination, known as $Ax$ or $A\cdot x$
$$
\begin{bmatrix*}[r]
  1 & 0 & 0\\
  -1 & 1 & 0\\
  1 & -1 & 1\\
\end{bmatrix*}\begin{bmatrix*}[r] x_1\\ x_2\\ x_3\\\end{bmatrix*} = \begin{bmatrix*}[l]
  x_1\\
  x_2 - x_1\\
  x_3 - x_2\\
\end{bmatrix*}
$$

> The first matrix here ($A$) is known as a **Difference Matrix**

This pattern continues, so the next result would be $b_4 = x_4-x_3$. This is the new way of multiplying matrices with vectors, the usual way was a row at a time, but they achieve the same result.

### Inverse combinatorics
> Which combination of $u,v,w$ produces a vector $b$

Assuming the equations for $Ax = b$:
$$
\begin{align*}
x_1 &= b_1\\
-x_1+x_2 &= b_2\\
-x_2+x_3 &= b_3\\
\end{align*}
$$

Then $x=A^{-1}b$ must be
$$
\begin{align*}
x_1 &= b_1\\
x_2 &= b_1+b_2\\
x_3 &= b_1+b_2+b_3\\
\end{align*}
$$

### Connect to calculus
The vector $x$ can be written as the function $x(t)$ while the differences $Ax$ become the derivative $dx/dt = b(t)$. In the inverse direction the sums $A^{-1}b$ become the integral of $b(t)$. 
> Sums of the differences are like integrals of derivatives

In math:
$$
Ax = b \text{ and } x = A^{-1}b\qquad \frac{dx}{dt}=b \text{ and } x(t)\int_0^t{b\cdot dt}
$$

If we were to take the example of squares:
$$
x = \begin{bmatrix*}[r] 1^2\\ 2^2\\ 3^2\\\end{bmatrix*} = \begin{bmatrix*}[r] 1\\ 4\\ 9\\\end{bmatrix*} 
$$
When using the difference matrix $A$ we get the following, we see this as a 4 dimensional matrix where $x_0 = 0$
$$
Ax = \begin{bmatrix*}[r] 1-0\\ 4-1\\ 9-4\\\end{bmatrix*}=\begin{bmatrix*}[r] 1\\ 3\\ 5\\\end{bmatrix*} = b 
$$
The differences of the squares $(0,1,4,9)$ then is $(1,3,5)$, this doesn't quite line up with the derivative of $x(t) = t^2$ as that would be $2t$ our differences are $2t-1$, that's because the derivative and differentiation isn't the same. We can prove it by calculation the backward difference:
$$
x(t)-x(t-1) = t^2 - (t-1)^2 = t^2 - (t^2 - 2t + 1)=2t-1
$$
The forward difference would be:
$$
x(t+1)-x(t) = (t+1)^2-t^2 = (t^2-2t+1)-t^2 = 2t+1
$$
We can then calculate the centered difference:
$$
\frac{f(x+1)}{2} = \frac{(t^2 - (t-1)^2) - ((t+1)^2-t^2)}{2} = \frac{(t-1)^2 - (t+1)^2}{2} = 2t
$$

Difference matrices are great, but centered differences are the best to go for.

#### Non invertible matrix
If we were to change $w$ to $w*$ such that:
$$
u = \begin{bmatrix*}[r] 1\\ -1\\ 1\\\end{bmatrix*}\qquad v=\begin{bmatrix*}[r] 0\\ 1\\ -1\\\end{bmatrix*}\qquad w*=\begin{bmatrix*}[r] -1\\ 0\\ 1\\\end{bmatrix*}
$$
Then we would get the cyclic difference matrix $C$:
$$
Cx =
\begin{bmatrix*}[r]
  1 & 0 & 0\\
  -1 & 1 & 0\\
  -1 & -1 & 1\\
\end{bmatrix*}
\begin{bmatrix*}[r] x_1\\ x_2\\ x_3\\\end{bmatrix*} = \begin{bmatrix*}[l]
  x_1 - x_3\\
  x_2 - x_1\\
  x_3 - x_2\\
\end{bmatrix*} = b
$$

This matrix is impossible to solve as it has infinitely many solutions.

### Multiplication
When multiplying 2 matrices a few rules apply, first is that $AB\cdot C = A\cdot BC$

Second is that if $A$ is $m$ by $n$ and $B$ is $n$ by $p$ then the product $AB$ is $m$ by $p$

Each entry in $C$ is the dot product $C_{ij} = (\text{row } i \text{ of } A)\cdot (\text{column } j \text{ of } B)$, for example:
$$
\begin{bmatrix*}[l]
  1 & 1\\
  2 & -1
\end{bmatrix*}
\begin{bmatrix*}[l]
  2 & 2\\
  3 & 4
\end{bmatrix*} =
\begin{bmatrix*}[l]
  C_{1,1} = 1\cdot 2 + 1\cdot 3 & C_{1,2} = 1\cdot 2 + 1\cdot 4\\
  C_{2,1} = 2\cdot 2 + -1\cdot 3 & C_{2,2} = 2\cdot 2 + -1\cdot 4
\end{bmatrix*} = 
\begin{bmatrix*}[l]
  5 & 6\\
  1 & 0
\end{bmatrix*}
$$