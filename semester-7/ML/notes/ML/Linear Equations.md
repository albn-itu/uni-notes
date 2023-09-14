---
tags:
  - concept
  - term
  - math
---

A linear equation is an equation of the form $ax+b$, we can also express them as $ax+by$.

## Vector form
Take the following 2 equations
$$
\begin{align*}
3x+2y&=11\\
x-2y&=1
\end{align*}
$$
We can express these as [[Vectors]]:
$$
x\begin{bmatrix*}[r] 1\\ 3\end{bmatrix*} + y \begin{bmatrix*}[r] -2\\ 2\end{bmatrix*} = \begin{bmatrix*}[r] 1\\ 11\end{bmatrix*} = b
$$
> The solution to this equation $b$ is the point where the vectors intersect

The matrix $A$ is known as the coefficient matrix
$$
A = \begin{bmatrix*}[r] 1 & -2 \\ 3 & 2\end{bmatrix*}
$$
which means the matrix equation is $Ax = b$ or
$$
\begin{bmatrix*}[r] 1 & -2 \\ 3 & 2\end{bmatrix*}\begin{bmatrix*}[r] x \\ y\end{bmatrix*} = \begin{bmatrix*}[r] 1 \\ 11\end{bmatrix*}
$$

## Matrix form
We can also express the equations in a [[Matrices]] form, take the following vector form:
$$
x\begin{bmatrix*}[r] 1\\ 2\\ 6\end{bmatrix*} + y \begin{bmatrix*}[r] 2\\ 5\\ -3\end{bmatrix*} + z \begin{bmatrix*}[r] 3\\ 2\\ 1\end{bmatrix*} = \begin{bmatrix*}[r] 6\\ 4\\ 2\end{bmatrix*}
$$
We can express this as the coefficient matrix $A$ in $Ax=b$
$$
A = \begin{bmatrix*}[r] 1 & 2 & 3\\ 2 & 5 & 2\\ 6& -3 & 1\end{bmatrix*}
$$
The matrix equation $Ax=b$ then is
$$
\begin{bmatrix*}[r] 1 & 2 & 3\\ 2 & 5 & 2\\ 6& -3 & 1\end{bmatrix*}\begin{bmatrix*}[r] x\\ y\\ z\end{bmatrix*} = \begin{bmatrix*}[r] 6\\ 4\\ 2\end{bmatrix*}
$$

## Elimination
Elimination goes through 4 general steps:
1. Elimination goes from $A$ to a triangular $U$ by a sequence of matrix steps $E_{ij}$.
2. The triangular system is solved by back substitution: working bottom to top.
3. In matrix language $A$ is factored into $LU$ = (lower triangular) (upper triangular).
4. Elimination succeeds if $A$ is invertible. (But it may need row exchanges.)
This is the computational science way and is expressed as $x = A\backslash b$