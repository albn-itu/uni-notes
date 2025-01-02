# General notes
## Fields
A **field** is a set $\mathbb{F}$ and two operations, addition $+$ and multiplication $\times$, such that:

- **Associativity**: $a + (b + c) = (a + b) + c$ and $a \times (b \times c) = (a \times b) \times c$.
- **Commutativity**: $a + b = b + a$ and $a \times b = b \times a$.
- **Identities**: There exist elements $0$ and $1$ such that $a + 0 = a$ and $a \times 1 = a$.
- **Inverses**: For every element $a$, there exists an additive inverse $-a$ such that $a + (-a) = 0$, and if $a \neq 0$, there exists a multiplicative inverse $a^{-1}$ such that $a \times a^{-1} = 1$.
- **Distributivity**: $a \times (b + c) = (a \times b) + (a \times c)$.

If everything above is fulfilled except the criteria that all non-zero elements have a multiplicative inverse, we instead get a **(commutative) ring**.

**Examples**:

- $\mathbb{Z}_p$, the set of integers $\{0, 1, \dots, p-1\}$ with addition and multiplication computed modulo $p$, is a finite field for $p$ prime, but only a ring when $p$ is not. For instance, in $\mathbb{Z}_6$, there is no multiplicative inverse to $2$.

# Randomized algorithms
## Polynomial identity testing (Lecture 6)
> Q: What is the polynomial identity testing problem? Why can it be reduced to deciding whether a given polynomial is the zero polynomial?

Simply put the polynomial identity testing problem (PIT) is the problem of determining whether two multivariate polynomials are equal.

Say we are given $p(x_1,\dots,x_n)$ and $q(x_1,\dots,x_n)$, over some field $\mathbb{F}$, and we want to determine whether $p(x_1,\dots,x_n) = q(x_1,\dots,x_n)$ which is the same as determining if the difference $p-q=0$. This latter case also allows for using single polynomials by asking the question if $p(x_1,\dots,x_n) = 0$ over some field $\mathbb{F}$.

In PIT the the 0 polynomial is defined as the sum of of monomials over the polynomial with various coefficients which are all 0. Say we have the polynomial $p(x,y,z) = (x+2y)(3y-z)$, the we expand it to: $p(x,y,z) = 3xy - xz + 6y^2 - 2yz$. Then we ask if all the coefficients are 0, if so, then the polynomial is the zero polynomial. (Problematically there may be $d^k$ monomials)

This is different from the zero everywhere problem where we ask for every choice of number in $p(x_1,\dots,x_n)$ if the polynomial evaluates to 0.

---
> Q: Assume black-box access to a polynomial p of degree at most n: You can choose a query point s and get back p(s) as the result of your query.

> _Q: How many points do you have to query in the worst-case in order to find out whether p is the zero polynomial?

This is the DeMillo-Lipton-Schwartz-Zippel lemma which states that if we have a polynomial $p(x_1,\dots,x_n)$ of degree at most $d$ over some field $\mathbb{F}$, and the finite set $S \subseteq \mathbb{F}$, then if we pick $y_1,\dots,y_k$ uniformly at random from $S$ and evaluate $p(y_i)\forall i$, then the probability that $p = 0$ is at most $\frac{d}{|S|}^k$.

So essentially. If we pick a random point then there is a $\frac{d}{|S|}$ chance that we chose a root. Now, to solve the problem, assume that $d < |\mathbb{F}|$ then we simply pick $y_1,\dots,y_k$ uniformly at random from $\mathbb{F}$ and evaluate $p(y_i)\forall i$, if we get 0 then we know say that $p$ is the zero polynomial. If we don't get 0 then we know that $p$ is not the zero polynomial. The latter case is always correct. While the formers probability of error is $\frac{d}{|\mathbb{F}|} < 1$, we can repeat the process $k$ times to get a probability of error of  $\left(\frac{d}{|\mathbb{F}|}\right)^k$.

There is an extremely low chance of success. The case where $d=|\mathbb{F}|-1$ and repeating the process $k=|\mathbb{F}|$ times gives a success probability of 

$$\frac{|\mathbb{F}|-1}{|\mathbb{F}|} \leq \left(1-\frac{1}{|\mathbb{F}|}\right)^{|\mathbb{F}|}\leq 1/e$$

> _Q: How can you recover the coefficients of p in this model

If we have a polynomial $p(x_1,\dots,x_n)$ of degree at most $d$ over some field $\mathbb{F}$, and the finite set $S \subseteq \mathbb{F}$, then if we pick $y_1,\dots,y_{d+1}$ points distinct points from $S$ then we can solve a system of linear equations where we know the result. Fx. if have a 2 degree polynomial and 3 points then we can solve:
$$
\begin{align*}
p(y_1) &= a_0 + a_1y_1 + a_2y_1^2\\
p(y_2) &= a_0 + a_1y_2 + a_2y_2^2\\
p(y_3) &= a_0 + a_1y_3 + a_2y_3^2\\
\end{align*}
$$

---
> Q: How does randomness help in the polynomial identity testing problem? In particular, which success probability can you achieve using randomness?

A polynomial can have an incredibly large amount of monomials which are infeasible to solve. Secondly the polynomial can have a potentially infinite number of roots, there is no way to check all of them. So randomness helps in testing a large space while only checking a small subset of it.

The randomness allows us to use the DeMillo-Lipton-Schwartz-Zippel lemma to determine if a polynomial is the zero polynomial. It's error probability is at most $\frac{d}{\mathbb{F}}$ at a single random point. We can increase the success probability by repeating the process $k$ times to get an error probability of $\left(\frac{d}{|\mathbb{F}|}\right)^k$.

## Freivalds’ algorithm (Lecture 6)
> Q: What is the purpose of Freivalds’ algorithm?

Freivalds algorithm solves the matrix verification problem. Formally the matrix verification problem takes $n\times n$ matrices $A$, $B$ and $C$ and asks if $AB = C$. Freivalds algorithm solves this problem in $O(n^2)$ time. This must be compared to the naive matrix multiplication algorithm which takes $O(n^3)$ Technically $O(n^{2.373})$ time.

---
> Q: Why is it faster than computing matrix products?

The naive matrix multiplication algorithm takes $O(n^3)$ time to compute the matrix product, using the standard matrix multiplication algorithm (see later sections). Freivalds algorithm significantly reduces the time complexity by using a random "fingerprint". The algorithm works by defining the function:
$$
f(v) = (A\times B - C) \times v
$$

If $AB=C$ then $f(v)$ will always be zero, regardless of the value of $v$. If $AB\neq C$ then $f(v)$ will be non-zero for some $v$, but there might be $v$ values that make $f(v)$ zero. 

We can calculate it by using distributive laws, such that we calculate:
$$
f(v) = (A\times (B \times v)) - C \times v
$$

Every step in the calculation is $O(n^2)$.

---
> Q: Describe the random choices made by the algorithm. Depending on the random choices, when does the algorithm succeed and when does it fail?

Freivalds algorithm works like this:

1. Choose a random vector $v$ of length $n$, where each element is chosen uniformly at random from $\mathbb{F}$.
2. Calculate $f(v) = (A\times (B \times v)) - C \times v$.
3. If $f(v) = 0$ then the algorithm returns "YES", otherwise it returns "NO".

If the resulting vector is not the zero vector then the algorithm returns "NO". This will always be correct, and has not chance of false positivies. On the other hand if it is the all-zero vector, then the algorithm concludes that $AB=C$, but there is a chance that it was simply the correct $v$ value to cause this result, therefore there may be false positives.

The probability of a false positive, aka the error probability is $\frac{1}{|\mathbb{F}|}$ where $\mathbb{F}$ is the field over which the vector is defined. So for $\mathbb{F} = \{0,1\}$ the error probability is $\frac{1}{2}$. We can reduce the error probability by repeating the process $k$ times to get an error probability of $\left(\frac{1}{|\mathbb{F}|}\right)^k$.

---
> Q: What is the failure probability of the algorithm? Use probability theory to give an argument for your answer.

The failure probability of the algorithm is the probability that the algorithm returns "YES" when $AB\neq C$. This occurs only if $f(v)=(AB-C)v=0$ for non-zero matrix $AB-C$ and non-zero vector $v$.

1. If $AB\neq C$ then $D=AB-C$ is a non-zero matrix.
2. The equation $Dv=0$ implies that $v$ is in the kernel (null space) of $D$, which is a subspace where $Dv=0$.
3. Since $v$ is a random vector with entries chosen uniformly from $\mathbb{F}$, the probability that $v$ is in the kernel of $D$ is at most $\frac{1}{|\mathbb{F}|}$. Since:
    - The kernel of $D$ is a proper subspace of $\mathbb{F}^n$
    - The size of the kernel is $|Kernel(D)|=|\mathbb{F}|^{n-rank(D)}$
    - The total number of vectors in $\mathbb{F}^n$ is $|\mathbb{F}|^n$
    - The probability that a random vector is in the kernel of $D$ is $Pr[Dv=0]=\frac{|Kernel(D)|}{|\mathbb{F}|^n}=\frac{|\mathbb{F}|^{n-rank(D)}}{|\mathbb{F}|^n}=|\mathbb{F}|^{-rank(D)}$
    - Since $D$ is non-zero, $rank(D)\geq 1$ so $Pr[Dv=0]\leq \frac{1}{|\mathbb{F}|}$
4. Therefore the probability that the algorithm fails is at most $\frac{1}{|\mathbb{F}|}$. We can reduce the error probability by repeating the process, with new vectors, $k$ times to get an error probability of $\left(\frac{1}{|\mathbb{F}|}\right)^k$.
