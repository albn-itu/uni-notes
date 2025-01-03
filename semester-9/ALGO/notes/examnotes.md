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

## Karger’s algorithm (Lecture 7)
> Q: What is a global min-cut in a graph?

A global min-cut in a graph is simply the smallest set of edges, or the smallest sum of edge weights necessary to separate the graph into two connected components. In max flow there is a rule of thumb that the min-cut must be a set of edges with the same flow as the max flow.

---
> Q: Describe Karger’s algorithm to find a global min-cut in a graph.

Karger's algorithm works by:

1. Sample an edge uniformly and independently
2. Contract it by taking the edge $e = (u,v)$ and turn $u,v$ into a single vertex, deleting all edges between them but keeping all other edges
3. Repeat $n-2$ times

After running the algorithm there will only be 2 vertices left, since we ran it $|V|-2$ times. Output these edges as the result.

A key property of the algorithm is that we never make the cut smaller, some cuts may vanish but any cut in the resulting graph is also a cut in the original graph, since all the edges in the resulting graph also exist in the original.
 
The 2 remaining vertices essentially represent 2 different components.

---
> Q: What is the failure probability of Karger’s algorithm? Sketch an analysis using probability theory and highlight where exactly properties of an assumed min-cut are used in the analysis.

First, say the mincut $c$ has a size $k$. Then for each step $i=1,2,\dots,n-2$, let $E_i$ be the event that the edge contracted in step $i$ is *not* in the mincut.

Similarly, let $F_i$ be the event that no edge contracted in the steps up to, and including, $i$ was in the mincut. 

We note that $Pr(E_i)=\frac{m_i-k}{m_i}$ where $m_i$ is the amount of edges in the graph before contractions in step $i$. If we use the observation that every vertex in any graph must have at least $k$ incident edges, since otherwise ony could just cut a vertex with less than $k$ edges and then have 2 components.

Therefore the amount of edges in the original graph must be at least $\frac{nk}{2}$, with this observation we can define the first step probability as:
$$
Pr(E_1)\geq \frac{\frac{nk}{2}-k}{\frac{nk}{2}} = 1-\frac{2}{n}
$$

Using conditional probabilities, which say that if the event $B$ occurs, then the probability that event $A$ occurs its
$$
Pr(A|B)=\frac{Pr(A\cap B)}{Pr(B)}
$$

Now, we've defined $F_i$ as the event that no edge contracted up to step $i$ was part of the mincut. In other words, the solution may still be found. Using the information from before we also know the size of $m_i$, as follows, must be the size of the original graph plus the size of the cut, minus the amount of removed vertices.
$$
m_i \geq \frac{nk}{2}+\frac{k}{2}-\frac{ik}{2} = \frac{(n+1-i)k}{2}
$$

Using this we can define the probability that we do not remove part of the solution, given that the previous steps didn't:
$$
Pr(E_i|F_{i-1})=\frac{m_i-k}{m_i}\geq 1-\frac{2}{n+i-1}
$$

Using Bayes theorem we can calulate:
$$
\begin{align*}
Pr(F_{n-2}) &= Pr(E_{n-2}\cap F_{n-3})=Pr(E_{n-2}|F_{n-3})Pr(F_{n-3})\\
&=\prod_{i=1}^{n-2}Pr(E_i|F_{i-1})\\
&=\prod_{i=1}^{n-2}\left(\frac{m_i-k}{m_i}\right)\geq \prod_{i=1}^{n-2}\left(1-\frac{2}{n+1-i}\right)\\
&=\prod_{i=1}^{n-2}\left(\frac{n-1-i}{n+1-i}\right)=\frac{n-2}{n}\cdot\frac{n-3}{n-1}\cdots\frac{1}{3}=\frac{2}{n(n-1)}
\end{align*}
$$

This means that the probability of finding the mincut is $\frac{2}{n(n-1)}$, or $\frac{1}{n^2}$. As always we can increase the success probability by repeating the process $k$ times to get an error probability of $\left(1-\frac{1}{n^2}\right)^k$. If we repeat $n^2$ times then the success probability is $1-\left(1-\frac{1}{n^2}\right)^{n^2} > 1-e^{-2}$, and the error probability is $e^{-2}$.

---
> Q: Why does the success probability analysis of Karger’s algorithm imply that any graph has at most $n \choose 2$ global min-cuts?

Define the problem as whether to put each vertex into bag $S$ or $T$, there are then 2 choices for each vertex, aka $2^n$ choices. This is actually reduced to $2^{n-1}$ since we can always switch the two bags and sicne 2 of the choices are the same, we get $2^{n-1}-1$ distinct choices.

By the analysis of the success probability $Pr(F_{n-2})=\frac{2}{n(n-1)}$ we can see that the probability of finding the mincut is proportional to the square of the number of vertces in the graph. We can rewrite this to $\frac{1}{n \choose 2}={n \choose 2}^{-1}$, this is also the amount of mincuts in the graph.

The implication comes from the algorithm depending on not removing any edges from the mincut, and the probability of this happening is $\frac{1}{n \choose 2}$, ergo the amount of mincuts in the graph.

## Monte Carlo method (Lecture 9)
> Q: Sketch how you can determine the number $\pi$ by throwing darts.

This is very close to the example from the lecture. Essentially, imagine circular dart board with it's center being denoted $0,0$. Then the dart board is a circle with radius 1, so the east most point is $1,0$ and the north most point is $0,1$. Imagine a square whose opossite corners are $-1,1$ and $1, -1$. The area of the square is $4$ and the area of the circle is $\pi$. If we throw darts at the square then the probability of hitting the circle is $\frac{\pi}{4}$, since that is the ratio of the areas. Then if we throw $n$ darts and $m$ of them hit the circle then $\frac{m}{n} \approx \frac{\pi}{4}$, ergo $\pi \approx 4\frac{m}{n}$.

---
> Q: What does it mean for a randomized algorithm to $(\epsilon, \delta)$-approximate a value?

An algorithm is said to approximate the answer if it produces an estimate that is within a factor of $(1+-\epsilon)$ of the true answer with probability at least $1-\delta$. This means that the algorithm is allowed to be wrong with probability $\delta$ and the answer is allowed to be off by a factor of $\epsilon$.

---
> Q: How many samples are sufficient to $(\epsilon, \delta)$-approximate the mean $\mu$ of an indicator random variable $X$? What is the name of the bound used to prove this? (You don’t need to prove this bound, but have a rough idea how the proof works.)

This is the Chernoff bound. The Chernoff bound bounds the sum of independent random variables by providing an upper limit on the probability that the sum deviates from its expected value by more than a certain amount.

When dealing with indicator functions, where $X_i$ is 1 if an event occurs and 0 otherwise, then let $S$ be the sum $S=X_1+\dots+X_n$ after $n$ samples and $\mu=\frac{S}{n}$ be the mean. This must be within $\epsilon$ of the true mean $\mu$ with probability at least $1-\delta$.

Assuming $0<\delta<1$ then the multiplicative Chernoff bound states that for any $\epsilon>0$:
$$
Pr[S \geq (1+\epsilon)n\mu] \leq \left(\frac{e^\epsilon}{(1+\epsilon)^{1+\epsilon}}\right)^\mu \leq e^{-\frac{\epsilon^2n\mu}{3}}
$$
and
$$
Pr[S \leq (1-\epsilon)n\mu] \leq \left(\frac{e^{-\epsilon}}{(1-\epsilon)^{1-\epsilon}}\right)^\mu \leq e^{-\frac{\epsilon^2n\mu}{2}}
$$

We can use a union bound, which states that for any finite or countable set of events then the probability that at least one of the events occurs is at most the sum of the probabilities of the individual events. This means that the probability that the sum deviates from the mean by more than $\epsilon$ is at most $2e^{-\frac{\epsilon^2n\mu}{3}}$.

This must be less than $\delta$, so we can set:
$$
2e^{-\frac{\epsilon^2n\mu}{3}} \leq \delta
$$

We can now solve for $n$ to get the number of samples needed to approximate the mean, by taking the natural logarithm of both sides and solving for $n$:
$$
n \geq \frac{3\ln(2/\delta)}{\epsilon^2\mu}
$$

---
> Q: Consider the following algorithm: To determine the number of satisfying assignments for a Boolean formula $F$ with $n$ variables, randomly sample some number $T$ of assignments. Among those sampled assignments, let $S$ be the number of assignments that satisfy $F$. Then output $S/T * 2^n$.
> _Q: Is the expected output of this algorithm correct?

Yes. $S/T$ represents the fraction of correct assignments in the samples, while $2^n$ is number of assignments in a single correct assignment, as it is the number of possible assignments for $n$ variables. Therefore $S/T * 2^n$ is the expected number of correct assignments.

> _Q: What other problem is there?

If the number of satisfying assigments is very small then the algorithm may not find them unless $T$ is very large, which would make it very slow. Formally if the number of assignments is small compared to $2^n$ then the probability of finding it is very small. This will be solved by the next algorithm.

---
> Q: Describe the randomized approximation algorithm for counting satisfying assignments to DNFs discussed in class.

The algorithm works by creating a very small sample space. Imagine a DNF formula, fx:
$$
(x_1 \wedge \overline{x_2}\wedge x_3) \vee (x_2\wedge x_4) \vee (\overline{x_1}\wedge x_3\wedge x_4)
$$

The algorithm then for each clause $C_i$ in the DNF formula defines the set of assignments that would satisfy it as $SC_i$, the size of this set is $2^{n-l_i}$ where $l_i$ is the number of literals in the clause. 

We want to find $|\bigcup_{i=1}^t SC_i|$, which is the number of satisfying assignments. This can be an absolutely huge set. $t$ is the number of clauses in the DNF formula.

> _Q: What exactly is the set it samples from?

We can the define the space where they all meet as $U=\{(i,a): 1\leq i\leq t \text{ and } a\in SC_i\}$. Now, every assignment that satisfies the formula is repsented in $U$. This set is relatively small compared to the total number of assignments from before. We can say that 

$$
\frac{|U|}{|\bigcup_{i=1}^t SC_i|} \geq \frac{1}{t}
$$

> _Q: Which condition does it check on such a sample?

First sample randomly from $U$ by randomly selecting which clause $C_i$ to sample from:
$$
Pr[\text{Choose } C_i] = \frac{|SC_i|}{|U|}
$$

Then sample a random assignment from $SC_i$ and set all other variables to random values. Since $SC_i$ only contains satisfying assignments for $C_i$ then the probability that the assignment satisfies the formula is 1. 

Now... The condition to check is that the earliest clause the assignment satisfies must be $i$. If the assignment satisfies an earlier clause then the assignment is discarded, this avoids overcounting, as the assignment would be counted by a different assignd overcounting: only count a sampled assignment if the
earliest clause it satisfies is the one we generament.

Say $i=3$ and the assignment satisfies the first clause, then it would be counted by the first clause and not the third. This is the condition that the algorithm checks.

> _Q: How does this algorithm solve the problem encountered by the algorithm in the previous bullet point?

The earlier algorithm had the problem that a satisfying assignment might not be found. The difference here is that the sample space is only satisfying assignments which are then sampled from. This entirely circumvents the problem.

## Primality testing (Lecture 9)
> Q: What is a strong probable prime?

A prime is a positive integer $p$ such that no integer $q$ strictly between 1 and $p$ divides $p$ ($p/q$ is never an integer for $1<q<p$).

All primes over 2 are odd, so only work with odd integers. A strong probable prime is an odd integer $n$ with a positive integer $s$ and an odd integer $d$ such that $n=2^sd+1$ satisfies either of the following conditions:

$$
\begin{align*}
&1. a^d = 1 \mod n       & &\text{ for some } 0<a\\
&2. a^{2^rd} = -1 \mod n & &\text{ for some } 0<a \text{ and } 0\leq r < s
\end{align*}
$$

---
> Q: What is the repeated squaring algorithm? What is its running time?

The repeated squaring algorithm is an algorithm designed to efficiently calculated $a^b \mod n$ for large $b$. It's very useful when using modular exponentiation, both to avoid overflow and to speed up the calculation.

The idea is we can turn $a^b$ into:
$$
a^b = a^{2^0b_0+2^1b_1+\dots+2^kb_k} = a^{2^0b_0}a^{2^1b_1}\dots a^{2^kb_k}
$$

Where $b_i$ is the $i$th bit of $b$. The algorithm only does the multiplying when the corresponding digit of $b$ is 1, which also skips some computations. Each computation is also done modulo $n$, since $a*b\mod n = (a\mod n)(b\mod n)\mod n$. The full algorithm goes as follows:

1. Set $c=1$ and $a_{cur}=a
2. For $i=0,1,\dots,k$, where $k$ is the number of bits in $b$:
    1. If $b_i=1$ then set $c=c*a_{cur} \mod n$
    2. Set $a_{cur}=a_{cur}^2 \mod n$
3. Return $c$

The running time of the algorithm is $O(\log b)$, since the number of bits in $b$ is $\log b$. For each iteration there is at most one multiplication and one squaring operation.

Don't include unless asked:
Each multiplication and squaring operation takes $O(\log^2 n)$ time. The total running time is $O(\log b\log^2 n)$. Unless $m$ is small or fixed then the running time is $O(\log b)$.

---        
> Q: Describe one algorithm that efficiently checks whether an integer is a prime or not w.h.p.

The Miller-Rabin primality test is a probabilistic algorithm that determines whether a given number is prime or not. It is based on the strong probable prime definition. The algorithm works by:

1. Find $d$ and $s$ such that $n-1=2^sd$.
2. Pick a random $r$ between $2<r<n-2$.
3. Compute $x=r^d \mod n$.
4. Repeat $s$ times:
    1. Compute $y=x^2\mod n$.
    2. If $y=1$ and $x\neq 1$ and $x\neq n-1$ then return "composite".
    3. Set $x=y$.
5. If $x\neq 1$ then return "composite", otherwise return "prime".

The algorithm is correct with probability at least $\frac{3}{4}$, and can be made arbitrarily close to 1 by repeating the process $k$ times. The running time of the algorithm is $O(k\log^3 n)$ for $k$ iterations. This is pretty good as the algorithm usually deals with very large numbers.
