[[toc]]

# General notes
## Fields
A **field** is a set $\mathbb{F}$ and two operations, addition $+$ and multiplication $\times$, such that:

- **Associativity:** $a + (b + c) = (a + b) + c$ and $a \times (b \times c) = (a \times b) \times c$.
- **Commutativity:** $a + b = b + a$ and $a \times b = b \times a$.
- **Identities:** There exist elements $0$ and $1$ such that $a + 0 = a$ and $a \times 1 = a$.
- **Inverses:** For every element $a$, there exists an additive inverse $-a$ such that $a + (-a) = 0$, and if $a \neq 0$, there exists a multiplicative inverse $a^{-1}$ such that $a \times a^{-1} = 1$.
- **Distributivity:** $a \times (b + c) = (a \times b) + (a \times c)$.

If everything above is fulfilled except the criteria that all non-zero elements have a multiplicative inverse, we instead get a **(commutative) ring**.

**Examples:**

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

According to the fundamental theory of Algebra, a polynomial of degree $n$ has at most $n$ roots. Therefore we only need to query $n+1$ distinct points. If all of these points evaluate to 0 then we know that the polynomial is the zero polynomial. If any of the points do not evaluate to 0 then we know that the polynomial is not the zero polynomial.

We can go further and calculate the probability of error:

This is the DeMillo-Lipton-Schwartz-Zippel lemma which states that if we have a polynomial $p(x_1,\dots,x_n)$ of degree at most $d$ over some field $\mathbb{F}$, and the finite set $S \subseteq \mathbb{F}$, then if we pick $y_1,\dots,y_k$ uniformly at random from $S$ and evaluate $p(y_i)\forall i$, then the probability that $p = 0$ is at most $\frac{d}{|S|}^k$.

So essentially. If we pick a random point then there is a $\frac{d}{|S|}$ chance that we chose a root. Now, to solve the problem, assume that $d < |\mathbb{F}|$ then we simply pick $y_1,\dots,y_k$ uniformly at random from $\mathbb{F}$ and evaluate $p(y_i)\forall i$, if we get 0 then we know say that $p$ is the zero polynomial. If we don't get 0 then we know that $p$ is not the zero polynomial. The latter case is always correct. While the formers probability of error is $\frac{d}{|\mathbb{F}|} < 1$, we can repeat the process $k$ times to get a probability of error of  $\left(\frac{d}{|\mathbb{F}|}\right)^k$.

So to we need to query $d+1$ points which gives us:
$$
\left(\frac{d}{|\mathbb{F}|}\right)^{d+1}
$$


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

1. Set $c=1$ and $a_{cur}=a$
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

## Algebraic algorithms (Lecture 8)
> Q: Roughly, what does the DeMillo-Lipton-Schwartz-Zippel lemma say?

The DeMillo-Lipton-Schwartz-Zippel lemma states that if we have a non-zero polynomial $p(x_1,\dots,x_n)$ of degree $d$ over some field $\mathbb{F}$, then if we pick $y_1,\dots,y_k$ uniformly at random from $\mathbb{F}$ and evaluate then
$$
Pr[p(y_1,\dots,y_k)=0]\leq \frac{d}{|\mathbb{F}|}
$$

This means that if we pick a random point then there is a $\frac{d}{|\mathbb{F}|}$ chance that we chose a root. 

---
> Q: What is the difference between the two mathematical concepts ring and field?

A **field** is a set $\mathbb{F}$ and two operations, addition $+$ and multiplication $\times$, such that:

- **Associativity:** $a + (b + c) = (a + b) + c$ and $a \times (b \times c) = (a \times b) \times c$.
- **Commutativity:** $a + b = b + a$ and $a \times b = b \times a$.
- **Identities:** There exist elements $0$ and $1$ such that $a + 0 = a$ and $a \times 1 = a$.
- **Inverses:** For every element $a$, there exists an additive inverse $-a$ such that $a + (-a) = 0$, and if $a \neq 0$, there exists a multiplicative inverse $a^{-1}$ such that $a \times a^{-1} = 1$.
- **Distributivity:** $a \times (b + c) = (a \times b) + (a \times c)$.

If everything above is fulfilled except the criteria that all non-zero elements have a multiplicative inverse, we instead get a **(commutative) ring**.

**Examples:**

- $\mathbb{Z}_p$, the set of integers $\{0, 1, \dots, p-1\}$ with addition and multiplication computed modulo $p$, is a finite field for $p$ prime, but only a ring when $p$ is not. For instance, in $\mathbb{Z}_6$, there is no multiplicative inverse to $2$.

**Key Differences:**
| Property                  | Ring                                      | Field                                     |
|---------------------------|-------------------------------------------|-------------------------------------------|
| **Multiplicative Inverse** | Not required for non-zero elements.       | Required for all non-zero elements.       |
| **Multiplicative Commutativity** | Not required (unless commutative ring). | Required for all elements.                |
| **Division**              | Division is not always possible.          | Division (by non-zero elements) is always possible. |
| **Examples**              | Integers $\mathbb{Z}$, matrices.     | Rationals $\mathbb{Q}$, reals $\mathbb{R}$. |


**Examples of Rings:**
- The set of integers $\mathbb{Z}$ with addition and multiplication.
- The set of $n \times n$ matrices with matrix addition and multiplication.
- Polynomial rings $R[x]$, where $R$ is a ring.

**Examples of Fields:**
- The set of rational numbers $\mathbb{Q}$ with addition and multiplication.
- The set of real numbers $\mathbb{R}$ with addition and multiplication.
- The set of complex numbers $\mathbb{C}$ with addition and multiplication.
- Finite fields (Galois fields), such as $\mathbb{Z}_p$ where $p$ is a prime number.

**Summary:**
- A **ring** is a more general structure than a field. It requires fewer constraints, particularly regarding multiplicative inverses and commutativity.
- A **field** is a special type of ring where every non-zero element has a multiplicative inverse, and multiplication is commutative.
- All fields are rings, but not all rings are fields. For example, $\mathbb{Z}$ is a ring but not a field, while $\mathbb{Q}$ is both a ring and a field.

---
> Q: Name one combinatorial problem matrix determinants can be used to solve and describe roughly how it works.

Perfect matchings. A perfect matching is a set of vertices such that every vertex is included exactly once. Formally defined as: Given a graph $G=(V,E)$, a perfect matching is a set of edges $M\subseteq E$ such that every vertex in $V$ is incident to exactly one edge in $M$.

If a matrix $A$ is a matrix over some field $\mathbb{F}$ then the determinant $det(A)$ is a scalar value in $\mathbb{F}$ that detects when $A$ is invertible. Aka if $det(A)\neq 0$ then a matrix $A^{-1}$ exists such that $AA^{-1}=I$.

A graph can be mapped to a matrix where the rows and columns are the vertices and the entries are the edges, so a $1$ in $A_{ij}$ means that there is an edge between $i$ and $j$. 

In a bipartite graph, one takes and assigns half of the vertices to the rows and the other half to the columns. The determinant is then the number of perfect matchings in the graph. There may though be a case where the determinant is 0, but there are still perfect matchings in the graph. We can then use the Schwartz-Zippel lemma to determine if there are perfect matchings in the graph. First pick $r_1, r_2, \dots r_m$ uniform points over a large field $\mathbb{F}$. Then replace the entries in the matrix with the points. This, because of Leipnitz formula gives a polynomial $p(r_1,r_2,\dots,r_m)$ which is the determinant of the matrix. If the result is non-zero then there must be a perfect matching in the graph with the extreme probability $1-\frac{m}{|\mathbb{F}|}$.

This also solves the problem of calculating the polynomials which may be an extremely slow process.

For general graphs one can use the Tutte matrix of a graph. The Tutte matrix has the same representation but both rows and columns are $|V|$ long. This makes the algorithm much slower, as the matrix is far bigger. Because of how the Leibnitz expansion works it cancels out all odd-length cycles, leaving only even length cycles which can be decomposed into perfect-matchings. This is because a cycle cover where every cycle is even length can be seen as being composed of two directed perfect matchings. Therefore, if the determinant of the Tutte matrix is non-zero, then there must be a perfect matching in the graph. Same problem as before persists however, so we can use the Schwartz-Zippel lemma to determine if there are perfect matchings in the graph.

---
> Q: How computationally hard is it to compute an $n \times n$ symbolic matrix determinant with polynomials in several variables as entries with total degree bounded by $O(n)$? How computationally hard is it to compute an $n \times n$ numeric matrix determinant with elements from a finite field as entries?

Let's split this question into 2 parts, first one that handles the symbolic matrix determinant, and the second one that handles the numeric matrix determinant.

**Symbolic Matrix Determinant:**

A symbolic matrix is a $n\times n$ matrix where each entry is a polynomial in several variables. So each entry $A_{ij}$ is a polynomial $p_{ij}(x_1,\dots,x_m)$ where $m$ is the number of variables. The total degree of each polynomial is bounded by $O(n)$.

Calculation of the determinant of a symbolic matrix is a computationally hard problem, as it involves polynomial arithmetic. It can be done by unfolding the polynomial into it's monomials and cancelling a bunch of terms to create a large multivariate and multilinear polynomial. This is a very slow process, as it involves a lot of terms and operations. The time complexity of computing the determinant of a symbolic matrix is $O(n!)$, which is very slow for large $n$.

In most cases the symbolic matrix takes exponential time to compute the determinant of due to the large number of monomials.

**Numeric Matrix Determinant:**

A numeric matrix is a $n\times n$ matrix where each entry is a number from a finite field $\mathbb{F}$. 

The numeric matrix determinant can be computed using Gaussian elimination, which reduces the time complexity to $O(n^3)$, with each subroutine costing $O(n)$ time. This is much faster than the symbolic matrix determinant.

---
>Q: Describe one way of computing a numeric determinant.

The determinant can be calculated using the Leibnitz formula, which involves summing over all permutations of the rows or columns of the matrix. Specifically:

$$
det(A) = \sum_{\sigma: [n]\rightarrow[n]} \text{sgn}(\sigma) \prod_{i=1}^n A_{i,\sigma(i)}
$$

Where $\sigma$ is a permutation, eg $1\rightarrow 2$ and sgn is a function that returns the sign of the permutation:
$$
\text{sgn}(\sigma) = (-1)^{\text{number of inversions in } \sigma}
$$

An inversion is a tuple $i<j$ such that $\sigma(i)<\sigma(j)$

Overall this algorithm runs in $O(n!)$ time, which is very slow for large $n$. However, the algorithm can be sped up using Gaussian elimination, which reduces the time complexity to $O(n^3)$, with each subroutine costing $O(n)$ time.

## Markov chains (Lecture 10)
> Q: What is a Markov chain?

**Description:**

A markov chain is a model of events where the probability of every event depends on the state of the previous event. One thing to note is that the even $t$ only depends on the state, not how we got to the state. This is known as being *memoryless*.

Formally, a Markov chain consists of a stochastic process, which is just a collection of random variables $X_0, X_1, \dots$. This process is a Markov chain if:
$$
Pr[X_t=s_t|X_{t-1}=s_{t-1},X_{t-2}=s_{t-2},\dots,X_0=s_0]=Pr[X_t=s_t|X_{t-1}=s_{t-1}]
$$

Where $s_t$ is the state of the process at time $t$. This means that the probability of the next state only depends on the current state.

Transition probabilities are the probabilities of moving from one state to another. These are usually represented as a matrix $P$, called the transition matrix, where $P_{ij}$ is the probability of moving from state $s_i$ to state $s_j$. 

**Irreducibility:**

A finite Markov chain is irreducible if and only if it's state graph, from the matrix, is strongly connected. This means that it is possible to move from any state to any other state in a finite number of steps.

**Recurrent:**

Let $r^t_{ij}$ be the probability of moving from state $s_i$ to state $s_j$ in $t$ steps. A state $s_i$ is recurrent if $\sum_{t\geq 1}r^t_{ii}=1$. This means that the probability of returning to the state is 1. 

On the other hand if $\sum_{t\geq 1}r^t_{ii}<1$ then the state is transient. This means that the probability of returning to the state is less than 1.

A Markov chain is recurrent if all states are recurrent, and transient if all states are transient.

**Return time:**

Let $h_{ij}$ denote the expected time to reach state $s_j$ from state $s_i$, defined as
$$
    h_{ij}=\sum_{t\geq 1}t\cdot r^t_{ij}
$$

$h_ij$ may be infinite if the Markov chain has infinite states. On the other hand if the Markov chain is finite, then $h_{ij}$ converges to a fixed value, this is known as the recurrent state being positive recurrent.

**Periodicity:**

A state $s_i$ is periodic if there exists an integer $\Delta>1$ such that $Pr[X_{t+s}=s_j|X_t=s_j] = 0$ unless $\Delta|s$. This means that the chain can only return to the state only at multiples of $\Delta$.

Forexample: If $\Delta=2$ then the chain can only return to the state at even times. Such as if you have a Markov chain with states equal to the natural numbers, and at every discrete time step you move to one of the at most two adjacent integers, then you will be at odd integers every other time step and at even integers the remaining time. 

**Ergodicity:**

A finite, aperiodic and positive recurrent state is called an ergodic state. A Markov chain is ergodic if all it's states are ergodic. This means that it is possible to eventually get from every state to every other state with some positive probability. It also means we will infinitely ofent visit every state.

**Inequality:**

Markovs inequality states that for any non-negative random variable $X$ and any $a>0$ then the probability that $X$ is at least $a$ is at most the expected value of $X$ divided by $a$:
$$
Pr[X\geq a]\leq \frac{E[X]}{a}
$$

---
> Q: What is a stationary solution to a Markov chain?

Take a time $t$, then we can define a vector of probabilities as $v_t$ which contains one entry per state $s$. The entry $v_t(s)$ is the probability of being in state $s$ at time $t$. The next state then is defined as $v_{t+1}=v_tP$ where $P$ is the transition matrix. This means that the probability of being in state $s$ at time $t+1$ is the sum of the probabilities of being in all states at time $t$ multiplied by the probability of moving from state $s$ to state $s'$.

The sum of all probabilities in $v_t$ is 1, since the probability of being in some state is 1.

A stationary distribution then is a probability vector $\overline{\pi}$ such that $\overline{\pi}P=\overline{\pi}$. This means that the probability of being in state $s$ at time $t+1$ is the same as the probability of being in state $s$ at time $t$. This means that the distribution is stationary, and the chain has reached equilibrium.

Take for example the Markov chain with states $S=\{A,B\}$ then the transition matrix:
$$
P=\begin{bmatrix}
0.7 & 0.3\\
0.4 & 0.6
\end{bmatrix}
$$

To find the stationary distribution $\pi = (\pi_A, \pi_B)$, we solve the equation $\pi = \pi P$:

1. $\pi_A = 0.7 \pi_A + 0.4 \pi_B$
2. $\pi_B = 0.3 \pi_A + 0.6 \pi_B$

Additionally, we have the normalization condition:

3. $\pi_A + \pi_B = 1$

Solving these equations:
- From equation 1: $\pi_A - 0.7 \pi_A = 0.4 \pi_B$ → $0.3 \pi_A = 0.4 \pi_B$ → $\pi_A = \frac{4}{3} \pi_B$.
- Substitute $\pi_A = \frac{4}{3} \pi_B$ into equation 3: $\frac{4}{3} \pi_B + \pi_B = 1$ → $\frac{7}{3} \pi_B = 1$ → $\pi_B = \frac{3}{7}$.
- Then, $\pi_A = \frac{4}{3} \cdot \frac{3}{7} = \frac{4}{7}$.

Thus, the stationary distribution is:

\[
\pi = \left( \frac{4}{7}, \frac{3}{7} \right)
\]

This means that, in the long run, the system spends about $\frac{4}{7}$ of the time in state $A$ and $\frac{3}{7}$ of the time in state $B$.

---
> Q: What is the cover time of a random walk on a graph?

Let $G=(V,E)$ be a graph with $n$ vertices and $m$ edges. The cover time of a random walk on $G$ is the expected number of steps it takes for the random walk to visit every vertex at least once from a vertex $v$. The probability of moving from a vertex $v$ with degree $d$ to any of its neighbors is $\frac{1}{d}$.

The cover time is the maximum over all starting vertices $v$ of the expected number of steps to visit every vertex at least once. This is a measure of how long it takes for the random walk to explore the entire graph.

---
> Q: Show a tight asymptotic upper bound on the cover time of a random walk on an undirected non-bipartite connected graph.

<!-- TODO: I don't think this is deep enough. -->

First, choose a spanning tree of the graph. Then consider a tour that starts at any vertex $v_0$ and visits every subtree rooted at $v_0$. Then each edge in the tree is traversed twice, once in each direction, one to go down, and one to go up to the start again.

Let $v_0, v_1, v_{2n-2}=v_0$ be the sequence of visisted vertices. Then the expected number of steps to visit every vertex at least once is the sum of the expected number of steps to visit every vertex in the subtree rooted at $v_i$ for $i=0,1,\dots,n-1$. This is equivalent to $h_{uv}=2m$, thereby the upper bound is:

$$
\sum^{2n-3}_{i=0}h_{v_iv_{i+1}} < (2n-2)(2m) < 4mn
$$

---
> Q: Show an example of a strongly connected directed graph in which the cover time is exponential.

The simplest graph would be the line graph, so one where every vertex $v_t$ only has 2 outgoing edges, one to $v_0$ and one to $v_{t+1}$. From each vertex, except the first, there is a $1/2$ probability of resetting progress and going back to $v_0$.

So to reach all vertices you must traverse from $v_0$ to $v_n$ which happens with probability $1/2^{n-1}$. 

You can make it even worse by attachin a self loop of $n/2$ size to one end and letting the back vertices go to the start of said loop, such that it only enters the path after the cycle with probability $1/2$.

The cover time can be shown to be $O(2^{n/2})$

---
> Q: Describe how the algorithm for 2SAT can be analyzed as a random walk on a graph. What is the graph and what is its cover time?

**The problem:**

The 2SAT problem is a boolean formula in conjunctive normal from on $n$ variables with 2 literals in each clause, fx:
$$
(x_1 \vee \overline{x_3}) \wedge (\overline{x_1} \vee x_2) \wedge (\overline{x_2} \vee x_4)\wedge (\overline{x_3} \vee \overline{x_4})
$$

The problem is to find an assignment to the variables such that the formula is satisfied. The example has satisfying assignment $x_1=true, x_2=true, x_3=false, x_4=false$.

**The idea:**

Imagine a satisfying assinment, call it $T$. Then the idea of the algorithm is to pick some assignment called $S$ and make progress towards $T$ by looking at clauses not currently satisfied by $S$.

Since we pick an unsatisfied clause, then we know that we must set at least one of the literals and change it. So if we randomly select one and change its value in $S$ then we have a new assignment $S'$ which with probability $1/2$ comes one variable closer to $T$.

**The process:**

Let $X_t$ be the number of variables assigned correctly in $S_t$ at time $t$. So how many variables in $S_t$ equal $T$. The we have the stochastic process for $1\geq j< n$:

$$
\begin{align*}
    Pr[X_{t+1}=j+1|X_t=j] &\geq \frac{1}{2}\\
    Pr[X_{t+1}=j-1|X_t=j] &\leq \frac{1}{2}\\
\end{align*}
$$

This is a random walk on the integers from 0 to $n$, but is not a Markov Chain as every state does not depend on the previous, this is:

$$
\begin{align*}
    Y_0 &= X_0\\
    Pr[Y_{t+1}=1|Y_t=0] &= 0\\
    Pr[Y_{t+1}=j+1|Y_t=j] &\geq \frac{1}{2}\\
    Pr[Y_{t+1}=j-1|Y_t=j] &\leq \frac{1}{2}\\
\end{align*}
$$

Let $Z_j$ be a random variable representing the number of steps to reach $n$ from $j$, then we have:

$$
h_j = E[Z_j] = E\left[\frac{1}{2}(1+Z_{j-1})+\frac{1}{2}(1+Z_{j+1})\right]
$$

This can be rewritten with the linearity of expectation as:

$$
\begin{align*}
h_n &= 0\\
h_0 &= h_1 + 1\\
h_j &= \frac{h_{j-1}}{2}+\frac{h_{j+1}}{2}+1 \text{ for } 1<j<n
\end{align*}
$$

We can solve for $h_0$ with a lemma that states that $h_j=h_{j+1}+2j+1$ for $0\geq j\geq n-1$ as we can then say:
$$
\begin{align*}
    h_0 &= h_1+1\\
    &= h_2+1+3\\
    &\vdots\\
    &= \sum_{i=0}^{n-1}2i+1\\
    &= n^2
\end{align*}
$$

**Runtime:**

Assuming a 2SAT formula with $n$ variables, that has a satisfying assignment and that the walk is allowed to run until it finds the satisfying assignment, then the expected number of steps is at most $n^2$.

So if we abort after $2n^2$ then by Markovs inequality the probability of not finding the satisfying assignment is at most $1/2$, even if the assignment exists.

# Divide/Conquer and FFT
## Divide & Conquer and the Master theorem
> Q: Give the statement of the Master theorem for recurrence relations of the form $T(n) \leq aT(n/b) + O(n^c)$. Explain which cases can occur depending on $a,b,c$.

** Formally:**

Given a recurrence relation of the form:
$$
T(n) = aT(n/b) + f(n)
$$

- $a$ is the number of subproblems.
- $b$ is the factor by which the problem size is reduced.
- $f(n)$ is the cost of the work done outside the recursive calls.

Where $a\geq 1$, $b>1$ and $f(n)$ is a function, called the driving function. The Master theorem states that the behaviour of $T(n)$ can be characterized by the following cases:

1. If there exists a constant $\epsilon > 0$ such that $f(n) = O(n^{\log_b a - \epsilon})$, then $T(n) = \Theta(n^{\log_b a})$.
2. If there exists a constant $k \geq 0$ such that $f(n) = \Theta(n^{\log_b a} \log^k n)$, then $T(n) = \Theta(n^{\log_b a} \log^{k+1} n)$.
3. If there exists a constant $\epsilon > 0$ such that $f(n) = \Omega(n^{\log_b a + \epsilon})$ and if $a f(n/b) \leq k f(n)$ for some constant $k < 1$ and sufficiently large $n$, then $T(n) = \Theta(f(n))$.
    - The condition $a f(n/b) \leq k f(n)$ is known as the regularity condition.

**Explanation:**
The function $n^{log_b a}$ is called the watershed function. In every case we compare the driving function to this function. In the first case the watershed function grows faster than the driving function. In the second case the driving function grows mostly at the same rate as the watershed function. In the third case the driving function grows faster than the watershed function.

Specifically, in case 1 the watershed function must grow polynomially faster with a factor of $\Theta(n^{\epsilon})$ for some $\epsilon>0$. In case 2 the driving function grows at nearly the same rate as the watershed function, but specifrically it grows faster by a factor of $\Theta(\log^k n)$ for some $k\geq 0$. In case 3 the driving function grows faster than the watershed function by a factor of $\Theta(n^{\epsilon})$ for some $\epsilon>0$.

**Our case**

Take the given case:
$$
T(n) \leq aT(n/b) + O(n^c)
$$

With $a\geq 1, b>1$ and $c\geq 0$ a constant. 

First lets define the critical exponent as $k=\log_b(a)$. Then in our case $f(n)=O(n^c)$, where $c$ is a constant. This means that the driving function grows at a rate of $O(n^c)$. We can then compare this to the watershed function $n^k$. We can simply redefine the cases then to:

1. If $c<k$ then $T(n)=\Theta(n^k)$.
    - The subproblem dominates the cost and the solution is $\Theta(n^{\log_b a})$.
2. If $c=k$ then $T(n)=\Theta(n^c\log n)$.
    - The subproblem and the cost are of the same order and the solution is $\Theta(n^{\log_b a}\log n)$.
3. If $c>k$ then $T(n)=\Theta(n^c)$.
    - The cost dominates the subproblem and the solution is $\Theta(n^c)$.

---
> Q: Sketch a proof for one of the cases.

Let's prove case 1 where $c<k$ and $k=\log_b(a)$, we have the recurrence relation:
$$
T(n) \leq aT\left(\frac{n}{b}\right) + O(n^c)
$$

We want to show that $T(n)=\Theta(n^k)$, where $k=\log_b(a)$,

Let's look at the recursion tree:

- At level 0 the cost is $O(n^c)$.
- At level 1 we have $a$ subproblems of size $\frac{n}{b}$, each with cost $O\left(\left(\frac{n}{b}\right)^c\right)$.
- At level 2 we have $a^2$ subproblems of size $\frac{n}{b^2}$, each with cost $O\left(\left(\frac{n}{b^2}\right)^c\right)$.
- At level $i$ we have $a^i$ subproblems of size $\frac{n}{b^i}$, each with cost $O\left(\left(\frac{n}{b^i}\right)^c\right)$.

The total work at depth $i$ would be the number of subproblems times the cost of each subproblem:
$$
\begin{align*}
a^i \cdot O\left(\left(\frac{n}{b^i}\right)^c\right) &= O\left(a^i \cdot \left(\frac{n^c}{b^{ci}}\right)\right)\\
&= O\left(n^c \cdot \left(\frac{a}{b^c}\right)^i\right)
\end{align*}
$$

Then define the ratio of the sequence as $r=\frac{a}{b^c}$, we know that $c<k$ so $c<\log_b(a)$ which means that $b^c<b^{\log_b(a)}=a$. Therefore $r=a/b^c>1$.

The total cost across all levels is then:
$$
\sum_{i=0}^{\log_b(n)}O\left(n^c \cdot r^i\right)
$$

This is a geometric series, with $r>1$ where the sum would be dominated by last term where $i=\log_b(n)$. This gives us:

$$
\begin{align*}
O\left(n^c \cdot r^i\right) &= O\left(n^c \cdot r^{\log_b(n)}\right)\\
&= O\left(n^c \cdot \left(\frac{a}{b^c}\right)^{\log_b(n)}\right)\\
&= O\left(n^c \cdot \left(\frac{a^{\log_b(n)}}{n^c}\right)\right)\\
&= O\left(n^{\log_b(a)}\right)
\end{align*}
$$

So we've proven that when $c<k$ then $T(n)=\Theta(n^k)$.

Intuitively this makes sense because when the cost is low $c<k$, then the branching cost dominates on each levels total work $O(n^c)$, which makes the cost of the leaves the dominant term.

## Integer Multiplication
> Q: What is Karatsuba’s algorithm? What is its running time?

When multiplying integers, the usual approach is to use the grade-school algorithm, which has a running time of $O(n^2)$, where $n$ is the number of digits in the integers.

Karatsuba's algorithm takes a different approach. It uses divide and conquer by splitting the number and multiplying the parts. Specifically it uses multiplication and addition to handle numbers with half the size of the originals.

Take 2 large numbers $x$ and $y$ represented as $n$ digit strings in base $B$. For any integer $m<n$ one can write $x$ and $y$ as:
$$
\begin{align*}
x &= x_1B^m+x_0\\
y &= y_1B^m+y_0
\end{align*}
$$

where $x_0$ and $y_0$ are less than $B^m$. Then the product $xy$ can be written as:
$$
\begin{align*}
xy &= (x_1B^m+x_0)(y_1B^m+y_0)\\
&= x_1y_1B^{2m}+(x_1y_0+x_0y_1)B^m+x_0y_0\\
&= z_2B^{2m}+z_1B^m+z_0
\end{align*}
$$

where
$$
\begin{align*}
z_2 &= x_1y_1\\
z_1 &= x_1y_0+x_0y_1\\
z_0 &= x_0y_0
\end{align*}
$$

This requires 4 multiplications and 3 additions. Karatsuba's algorithm takes only three multiplications and some additions. If $z_0$ and $z_2$ the same, then we can calculate $z_1$ as:
$$
\begin{align*}
z_2 &= x_1y_1\\
z_0 &= x_0y_0\\
z_3 &= (x_1+x_0)(y_1+y_0)\\
z_1 &= x_1y_0+x_0y_1\\
    &= (x_1+x_0)(y_1+y_0)-x_1y_1-x_0y_0\\
    &= z_3-z_2-z_0
\end{align*}
$$


We can recursively apply this algorithm remember that:

$$
T(n) = aT(n/b) + f(n)
$$

where

- $a$ is the number of subproblems.
- $b$ is the factor by which the problem size is reduced.
- $f(n)$ is the cost of the work done outside the recursive calls.

Then $a=3$ as we have 3 multiplications, $b=2$ as we split the number in half and $f(n)=O(n)$ as we have to do some additions. This gives us:

$$
T(n) = 3T(n/2) + O(n)
$$

Since $c<\log_b(a)=\log_2(3)\sim 1.585$ then we can use the Master theorem to solve this. This gives us $T(n)=\Theta(n^{\log_2(3)})$ which is approximately $O(n^{1.585})$.

# Algorithms based on matrix multiplication
## Matrix multiplication
> Q: Define the matrix multiplication problem. How many arithmetic operations do you need to solve this problem in the standard way?

If $A$ is an $m\times n$ matrix and $B$ is an $n\times p$ matrix, then the product $C=AB$ is an $m\times p$ matrix where each entry $C_{ij}$ is the dot product of the $i$th row of $A$ and the $j$th column of $B$.

Matrix multiplication shares the same properties as regular multiplication, such as associativity and distributivity. But it doesn't share commutativity, as $AB$ is not always equal to $BA$.

Take 
$$
\begin{align*}
A = \begin{bmatrix}
1 & 2 & 3\\
4 & 5 & 6
\end{bmatrix} & & B = \begin{bmatrix}
7 & 8\\
9 & 10\\
11 & 12
\end{bmatrix}
\end{align*}
$$

Then the product $C=AB$ is:
$$
C = \begin{bmatrix}
1\cdot 7+2\cdot 9+3\cdot 11 & 1\cdot 8+2\cdot 10+3\cdot 12\\
4\cdot 7+5\cdot 9+6\cdot 11 & 4\cdot 8+5\cdot 10+6\cdot 12
\end{bmatrix} = \begin{bmatrix}
58 & 64\\
139 & 154
\end{bmatrix}
$$

In the standard, and worst case it requires $n^3$ multiplications and $n^2(n-1)$ additions.

This is because for each element of $C$ we perform $n$ multiplications and $n-1$ additions. The general way of stating it would be that we perform $m*p*n$ multiplications and $m*p*(n-1)$ additions. Which for square matrices gives the operations above.

---
> Q: Describe a way to reduce $n\times n$ matrix multiplication recursively to 8 multiplications of $n/2\times n/2$ matrices.

This is an application of Strassens algorithm, which is a divide and conquer approach that divides matrices into equally sized block matrices. It uses $2^n\times 2^n$ matrices, if the matrices are not square then they are padded with zeros, then we can take the matrices $A$, $B$, and $C$ and turn them into block matrices:

$$
\begin{align*}
A &= \begin{bmatrix}
A_{11} & A_{12}\\
A_{21} & A_{22}
\end{bmatrix} & B &= \begin{bmatrix}
B_{11} & B_{12}\\
B_{21} & B_{22}
\end{bmatrix} & C &= \begin{bmatrix}
C_{11} & C_{12}\\
C_{21} & C_{22}
\end{bmatrix}
\end{align*}
$$

Then we can define the product $C=AB$ as:
$$
C = \begin{bmatrix}
A_{11}B_{11}+A_{12}B_{21} & A_{11}B_{12}+A_{12}B_{22}\\
A_{21}B_{11}+A_{22}B_{21} & A_{21}B_{12}+A_{22}B_{22}
\end{bmatrix}
$$

This reduces the entire thing to 8 multiplications, but this is not the strassen algorithm. Strassens algorithm can reduce it to 7 multiplications by defining:

$$
\begin{align*}
M_1 &= (A_{11}+A_{22})(B_{11}+B_{22})\\
M_2 &= (A_{21}+A_{22})B_{11}\\
M_3 &= A_{11}(B_{12}-B_{22})\\
M_4 &= A_{22}(B_{21}-B_{11})\\
M_5 &= (A_{11}+A_{12})B_{22}\\
M_6 &= (A_{21}-A_{11})(B_{11}+B_{12})\\
M_7 &= (A_{12}-A_{22})(B_{21}+B_22)\\
\end{align*}
$$

Then we can define the blocks of $C$ as:
$$
C = \begin{bmatrix}
M_1+M_4-M_5+M_7 & M_3+M_5\\
M_2+M_4 & M_1-M_2+M_3+M_6
\end{bmatrix}
$$

This reduces the number of multiplications to 7. This process can be done recursively until the matrices are small enough to be multiplied using the standard algorithm. It depends a bit on the implementation some do it at 32 or 128 width matrices but recent developments in hardware do it already at 512.

---
> Q: How many recursive multiplications does Strassen's algorithm require, and what running time does this translate to in the end? Argue for the running time bound.

Stranssens algorithm requires 7 recursive multiplications. This is because we can define the blocks of $C$ as in the previous question.

We can argue for the runnint time bound using the recurrence relation. We know that every step takes $7$ multiplications, and at each step the problem size is reduced by a factor of 2. This gives us the recurrence relation:

$$
T(n) = 7T\left(\frac{n}{2}\right) + O(n^2)
$$

$O(n^2)$ is the cost of the additions and subtractions. We can then use the Master theorem to solve this with the following variables:

- $a = 7$ as we have 7 multiplications.
- $b = 2$ as we reduce the problem size by a factor of 2.
- $f(n) = O(n^2)$ as we have to do some additions and subtractions.

We can then calculate $log_b(a)=log_2(7)\approx 2.807$ and since $f(n)=O(n^c)$ where $c=2$ then $c<log_b(a)$ which means we are in case 1 of the Master theorem. This gives us 

$$
T(n)=\Theta(n^{log_2(7)})\approx O(n^{2.807})
$$

This is an improvement over the standard algorithm which has a running time of $O(n^3)$. This is because the Strassen algorithm reduces the number of multiplications required to compute the product of two matrices.

What the theorem essentially states is that the runtime is dominated by the recursive multiplications, not the work done outside the recursive calls ($O(n^2)$), which logically makes sense.

---
> Q: Define the constant $\omega$. What does the existence of Strassen's algorithm imply for $\omega$? What are the best known lower and upper bounds on $\omega$?

The constants $\omega$ is the exponent of the fastest known matrix multiplication algorithm. So for the naive approach $\omega=3$ and for Strassens algorithm $\omega\approx 2.807$.

Formally $\omega$ is stated as: The smallest real number such that the product of two $n\times n$ matrices can be computed in $O(n^{\omega+\epsilon})$ or $n^{\omega + o(1)}$ arithmetic operations for any $\epsilon>0$.

Currently the best known upper bound is $\omega=2.371552$ as of January 2024, however this is a galactic algorithm (new favourite term). Strassens algorithm is the best known practical algorithm with $\omega\approx 2.8074$. The general upper bound would be $\omega=3$ for the naive approach, it can probably be done slower though.

In general it is believed that $2\leq \omega\leq 3$. It is unknown if $\omega=2$ is possible, but it is known that $\omega\leq 2.371552$.

## Matrix multiplication for cliques
> Q: How can matrix multiplication be used for detecting and counting triangles?

First represent the graph $G=(V, E)$ as an adjacency matrix $A$ where $A_{ij}=1$ if there is an edge between $i$ and $j$, and $0$ otherwise. Then if we multiply the matrix with itself we get:
$$
(A^2)_{ij} = \sum_{k=1}^n A_{ik}A_{kj}
$$

So get get a contribution of one for each index $k$ where there is an edge $ik$ as well as an edge $kj$, in other words, the $ik$ entry of $A^2$ is the number of paths of length 2 from $i$ to $k$. We can extend this to any length parths. So since a triangle is $ijk$ we need the 2 hop paths $ik,kj,ji$, so we can calculate the number of triangles by taking the trace of $A^3$ and dividing by 6. We need to divide by 6 since each vertex can be traversed in each direction, and we count each vertex 3 times. 

---
> Q: How can matrix multiplication be used to detect cliques of a given size $k$?

A clique is a subset of vertices where every vertex is connected to every other vertex.

As with the previous question, the $ij$ entry of $A^k$ is the number of paths of length $k$ from $i$ to $j$. Technically a triangle is a clique, and we can calculate them with $A^3$. 

We cannot directly extend this method to $A^k$ but we can use the idea. So if we consider the matrices $A, A^2\dots, A^{k-1}$ then for a set of vertices $v_1,\dots,v_k$ to form a $k$ clique they must have a path. Then for each length $l$ from $2$ to $k-$ we can check if there is a path $v_i$ and $v_j$ for all $i,j$. If there is then we have a clique. 

Formally, for each $l$ from $2$ to $k-1$ then $A^l_{ij}>0$ for all $i,j$ in the set of vertices $v_1,\dots,v_k$ then we have a clique. We only check up to $k-1$ since a vertex cannot be connected to itself.

Essentially if we create a submatrix of the vertices in the original matrix $A$ this matrix will contain only 1s. The corresponding sub matrices in $A^l$ have all positive entries.

The time complexity of this task is $O(n^{\omega}\log k)$ where $\omega$ is the matrix multiplication constant via exponentiaion by squaring.

Not entirely sure about that last part.

---
> Q: Can you use the clique algorithm to find/count independent sets?

An independent set is a set of vertices where no two vertices are connected by an edge. This is the exact opposite of a clique. So if we define the graph $G'$ as the complement of $G$ where, if 2 vertices are adjacent in $G$ then they aren't in $G'$. Then we can find the independent sets of $G$ by finding the cliques of $G'$.

The algorithm would entail computing $G'$, then finding the cliques of size $k$ in $G'$ and then returning the number of cliques. This would return the number of independent sets of size $k$ in $G$.

It must also be noted that since we compute the complement of $G$ then if $G$ is sparse $G'$ is dense, which could complicate the algorithms running time.


# Exponential-time algorithms
## ETH and SETH (Lecture 27)
> Q: Explain the statement of the exponential-time hypothesis ETH and the strong exponential-time hypothesis SETH. Consider the following:

**ETH:**

ETH stands for the exponential time hypothesis and states that there is no algorithm that can solve 3-CNF boolean problems, also known as 3-SAT in subexponential time, $2^{o(n)}$. 

Formally it's stated as: There is some constant $c>0$ such that no algorithm running in $2^{cn}$ time can solve 3-SAT on $n$ variables with clauses of widht at most 3.

We can reduce to $k$-clique to prove that ETH implies that there is no algorithm that can solve $k$-clique in subexponential time. By grouping clauses in $k$ groups, then for each assignment to the variables in a group make a vertex $v_{i,j=(G_i, a_{i,j})}$. Then add an edge $v_{i,j}v_{i',j'}$ if:

- $i\neq i'$, and
- the assignments $a_{i,j}$ and $a_{i',j'}$ are consistent with each other. AKA not setting the same variable to opposite values.

**SETH:**

SETH stands for the strong exponential time hypothesis and states that there is a constant $k$ such that no algorithm can solve $k$-SAT on $n$ variables with clauses of width at most $k$ in time $2^{(1-\epsilon)n}$.

Informally this means that the time required to solve $k$-SAT inscreases exponentially with the number of variables.

> _Q: Why do they imply P != NP?

Both ETH and SETH imply that there is no algorithm that can solve 3-SAT in subexponential time. This means that 3-SAT is not in P, as P is the class of problems that can be solved in polynomial time. Since 3-SAT is NP-compleust be at most 2k2k leaves inte, according to ETH, this implies that P != NP.

> _Q: Is an algorithm with running time $O(1.0001^n)$ for 3-SAT possible under ETH? 

No. This grows much like $2^{n\log(1.0001)}=2^{O(n)}$ this is still subexponential time.

It would also not be allowed under SETH, the constants may be very small, but it's still not exponential time.

> _Q: Is an algorithm with running time $O(1001^{n/\log n})$ for 3-SAT possible under ETH?    

No. We can simplify this to:
$$
1001^{n/\log n} = 2^{\log(1001) \cdot (n/\log(n))} = 2^{O(n/\log(n))}
$$

This is subexponential time since $O(n/\log(n))=o(n)$ and thus $2^{O(n/\log(n))}=2^{o(n)}$. ETH rules out subexponential time algorithms for 3-SAT, so this is not possible.

This is not possible under SETH as well, since it also implies no algorithm can solve 3-SAT in sub-exponential time. SETH essentially states the same as ETH but for a wider range of problems, and at $k=3$ it is the same.

> _Q: Briefly give two examples for concrete super-polynomial running times for 3-SAT that are ruled out under ETH.

1. $O(2^{n/100})$ this is super-polynomial but sub-exponential time complexity.
2. $O(1.999^n)$ this is super-polynomial but sub-exponential time complexity.

---
> Q: What is the sparsification lemma, and why is it useful?

The sparsification lemma states that any instance of $k$-SAT for $k\geq 3$ can be reduced, in sub-exponential time, to a collection of sparse $k$-SAT instances. Specifically:

Given a $k$-SAT formula $\Phi$ with $n$ variables and $m$ clauses, the lemma allows us to decompose $\Phi$ into a disjunction (logical OR) of $2^{\epsilon n} smaller $k$-SAT formulas $\Phi_1, \Phi_2, \dots, \Phi_t$ where:

- Each $\Phi_i$ has at most $f(k, \epsilon) \cdot n$ clauses for some function $f$ depending on $k$ and $\epsilon$.
- The total size of the decomposition is $O(2^{\epsilon n})$.

In simpler terms, the lemma allows us to "sparsify" a dense kk-SAT formula into a collection of smaller, sparse formulas without significantly increasing the overall complexity of the problem.

This should all take $2^{\epsilon n} \cdot \text{poly}(n)$ time.

**Why is the Sparsification Lemma Useful?**

The Sparsification Lemma has several important implications and applications:

1. **ETH and Lower Bounds:**
   - The lemma is a key tool in proving lower bounds under ETH. It allows us to focus on sparse instances of $k$-SAT, which are easier to analyze, without losing generality.
   - For example, it is used to show that $k$-SAT cannot be solved in sub-exponential time (i.e., $O(2^{o(n)})$) unless ETH fails.

2. **Reduction to Sparse Instances:**
   - The lemma reduces the study of general $k$-SAT instances to the study of sparse instances, where the number of clauses is linear in the number of variables. This simplification is often crucial for proving hardness results or designing algorithms.

3. **Parameterized Complexity:**
   - In parameterized complexity, the lemma is used to show that certain parameterized problems are unlikely to have fixed-parameter tractable (FPT) algorithms. For example, it helps establish the hardness of problems like $k$-SAT under parameterized complexity assumptions.

4. **Algorithm Design:**
   - While the lemma is primarily used for hardness results, it can also guide the design of algorithms. By focusing on sparse instances, researchers can develop more efficient algorithms for special cases of $k$-SAT.

5. **Simplification of Proofs:**
   - The lemma simplifies many proofs in computational complexity by allowing researchers to assume, without loss of generality, that $k$-SAT instances are sparse. This often reduces the technical complexity of arguments.

**Example Application: ETH and 3-SAT**

One of the most important applications of the Sparsification Lemma is in proving that 3-SAT cannot be solved in sub-exponential time unless ETH fails. The lemma allows us to assume that 3-SAT instances are sparse (with $O(n)$ clauses), which makes it easier to analyze the problem and derive lower bounds.

---
> Q: Describe the Orthogonal Vectors problem.

Given two sets $L$ and $R$ of $n$ size vectors from $\{0,1\}^d$ with $d=\text{polylog}(n)$, the problem is to determine if there is a pair of vectors $u\in L$ and $v\in R$ such that $u\cdot v=0$. This generally takes $O(n^2)$ time to check.

> _Q: Which lower bound does SETH yield for this problem? Sketch the lower bound.

We first must reduce the problem to a CNF instance:

- Define $v_1,\dots,v_n$ be boolean variables to a CNF formula on $m$ clauses and $n$ even. This is our vectors.
- Partition them into the sets $L=\{v_1,\dots,v_{n/2}\}$ and $R=\{v_{n/2+1},\dots,v_n\}$.
- For each assignment $a$ to the varis in $L$  we build an $m$ long binary vector where entry $i$ is 1 if $a$ does not make clause $i$ true, and 0 otherwise. Do the same of $R$
- We now have two sets of $2^{n/2}$ binary vectors of length $m$.

We can then reduce the problem to diameter. Diameter in a connected undirected graph is the smallest positive integer $k$ such that every vertex has a path to each other vertex of length at most $k$.

Unless the $OV$ conjecture is false then there is no algorithm that given a sparse graph on $n$ vertices and $O(n^{1+o(1)})$ edges, computes the diameter in time $O(n^{2-\epsilon})$ for any $\epsilon>0$.

> _Q: Is an $O(n^2/\log n)$ algorithm or an $O(n^2/\sqrt{n})$ time algorithm possible under SETH?

**$O(n^2/log n)$**

No. The factor of $\log n$ grows much slower than the polynomial factor of $n^2$, so dividing by it does not significantly reduce the time complexity. Not that it matters since $n^2$ is polynomial and it must be exponential.

**$O(n^2/n^{1/2})$**

On the other hand, the square root factor actually reduces this problem to $n^{3/2}$ which is subquadratic time complexity. This would contradict that the OV problem cannot be solved significantly faster than $O(n^2)$ under SETH.

---
> Q: Describe the k-Dominating Set problem.

A dominating set in an undirected graph is a subset of the vertices such that every vertex is either connected to a vertex in S or is in S itself. A k-dominating set, is a dominating set of size exactly k.

> _Q: Which lower bound does SETH yield for this problem? Sketch the lower bound.

We once again reduce to a CNF instance:

- Partition the variables in $k$ groups $G_1,\dots,G_k$ of size $n/k$.
- For each assignment $a_1$ to the variables in a group $G_i$, add a vertex (a_i, i) to the graph.
    - Results in $k2^{n/k}$ vertices.
- Then add one vertex $s_i$ per group $G_i$, and connect all vertices in the group in a clique manner.
- Add one vertice for every clause $c_j$ in the input CNF formula.
- Add an edge from an assignment vertex $(a_i, i)$ to the vertex representing clause $c_j$ if the assignment $a_i$ satisfies the clause $c_j$.


## Inclusion/Exclusion (Lecture 11 and 12)
> Q: State and explain the inclusion-exclusion principle.

The formal definition is, given $n$ subsets $A_1,\dots,A_n\subseteq U$ of a ground set $U$, then the size of the union of the sets is:

$$
|\bigcup_{i=1}^n A_i| = \sum_{\phi\subset X\subseteq [n]} (-1)^{|X|+1}|\bigcap_{i\in X}A_i|
$$

This is essentially just an expansion. Take 2 sets $A$ and $B$, then the union is:
$$
|A\cup B| = |A|+|B|-|A\cap B|
$$

We take the sum of the sizes of the sets, then subtract the size of the intersection of the sets. This is because the intersection is counted twice, once for each set, so we need to subtract it once.

Expand to 3 sets $A$, $B$, and $C$:
$$
|A\cup B\cup C| = |A|+|B|+|C|-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|
$$

Essentially we add the sizes of the sets, then subtract the sizes of the intersections of the sets, then add the size of the intersection of all sets, this is because we've removed that size twice.

The sum has $2^{n-1}$ terms, so it's not practical to compute by hand.

---
> Q: Describe how to solve the Hamiltonian cycle problem using inclusion-exclusion.

The Hamiltonian cycle problem is the problem of determining whether a given graph contains a Hamiltonian cycle. A Hamiltonian cycle is a cycle that visits every vertex exactly once. This problem is NP-hard.

> _Q: Describe the role of walks and paths.

A closed $k$-walk in a graph is a sequence of $k$ vertices $v_1,\dots,v_{k+1}$ ending in the vertex it started in, such that $v_1=v_{k+1}$. A path is a walk where all vertices are distinct. Therefore a closed $n$-walk is a Hamiltonian cycle, if all vertices are distinct (except the first and last), so it's actually a $n$-path plus one vertex.

> _Q: How can you count walks in polynomial time?

First define the graph as an $n\times n$ adjacency matrix $A$ where $A_{ij}=1$ if there is an edge between $i$ and $j$, and $0$ otherwise. 

We've looked at this before, and if you calculate $A^k$ then the entry at $u,u$ equals the number of closed $k$-walks starting and ending in $u$.

The *trace* then of a matrix, which is the sum of it's diagonal entries, would be a weighted sum of the number of closed walks of length $k$. So $tr(A^n)$ is a weighted sum of the number of $n$-walks. Remember that a walk is not a path, so it can visit the same vertex multiple times, therefore it's not the Hamiltonian cycle.

Also since we have an entry in both directions, every walk is counted twice, so we need to divide the result by $2n$, once per vertex and direction.

Using matrix multiplication and fast exponentiation we can calculate this in polynomial time.

> _Q: Why do you need to count them, and why is deciding existence not enough?

The inclusion-exclusion principle requires us to count the number of structures (e.g., closed walks) that satisfy certain conditions. By counting walks, we can systematically account for all possible ways to form a Hamiltonian cycle.

The inclusion-exclusion principle relies on exact counts to compute the number of valid Hamiltonian cycles. Deciding whether a Hamiltonian cycle exists (a yes/no question) does not provide the necessary quantitative information for this approach.

With all the background information, we can now outline the approach to solving the Hamiltonian cycle problem using inclusion-exclusion:

Let $A(X)$ for a vertex subset $X\subseteq V$ the the adjacency matrix induced by the vertices in $X$, then the number of Hamiltonian cycles is:

$$
\frac{1}{2n}\sum_{X\subseteq V}(-1)^{n-|X|}tr(A(X)^n)
$$

with a running time of $O(2^n\cdot \text{poly}(n))$.

With this formula we only count what we want. The closed $n$-walks that are actually Hamiltonian cycles will be counted only in $tr(A(X)^n)$ where $X=V$, and coutned $2n$ times each.

We also don't count anything else. The closed $n$-walks that revisit some vertices will also miss some vertices, since the walk is of size $n$. Let $W\subset V$ be the vertices visited in the walk. The walk will be counted in $tr(A(X)^n)$, for all $X\supseteq W$, but it will be counted with a factor $-1$ equally often as with the factor $+1$, and hence they will cancel each other.

We can simplify the description of the algorithm to:

1. Count all closed walks of length $n$ in the graph.
2. Subtract the number of closed walks that miss at least one vertex.
3. Add the number of closed walks that miss at least two vertices, to correct over subtraction.
4. Continue this alternating inclusion-exclusion process until all cases are accounted for

We can say that $X$ is the number of vertices that are not excluded in the walk.

> _Q: Briefly compare this approach to the Bellman-Held-Karp dynamic programming algorithm for Hamiltonian cycles. Also outline the DP algorithm.

The Bellman-Held-Karp dynamic programming algorithm is an algorithm for computing the Hamiltonian cycle in a graph. It works as follows:

- For each subset $S$ of vertices and a vertex $v\in S$, let $dp[S][v]$ represent the number of paths that start at a fixed vertex, visit all vertices in $S$ exactly once and end at $v$.
- The base case is $dp[\{v\}][v]=1$ for the starting vertex $v$.
- For each subset $S$ and vertex $v$, compute $dp[S][v]$ by iterating over all predecessors $u$ of $v$ in $S$:
$$
dp[S][v] = \sum_{u\in S, u\neq v}dp[S\setminus \{v\}][u] \cdot A_{uv}
$$
- Finally the number of Hamiltonian cycles is the sum of $dp[V][v]$ for all $v$ adjacent to the starting vertex.

The dynamic programming algorithm is a bottom-up approach that builds up the solution incrementally by considering all possible paths and vertices. It is a more direct and efficient way to compute the Hamiltonian cycle compared to the inclusion-exclusion method, which relies on the principle of inclusion-exclusion to count the number of Hamiltonian cycles.

The time complexity is $O(n^2\cdot 2^n)$. This is essentially combinatorial vs implementation.

---
> Q: Describe how to count perfect matchings in a graph using inclusion-exclusion. Which structures are counted in the individual terms of the inclusion-exclusion formula? How can you speed this up on bipartite graphs, and what are the structures counted there?

A perfect matching in a graph is a set of edges such that every vertex is incident to exactly one edge. Counting the number of perfect matchings in a graph is a combinatorial problem that can be solved using the inclusion-exclusion principle. Finding a perfect matching is a polynomial time problem, but counting them is NP-hard.

From set partioning we have that we can count the number of perfect matchings in a graph $G=(V,E)$ as:

- Let the family $F$ the the edges $E$ of the graph and set $k=n/2$.
- Let $t(X)=|\{f:f\in F, f\subseteq X\}|$ for $X\subseteq V$.
- Then the number of perfect matchings is:
$$
\sum_{X\subseteq U}(-1)^{n-|X|}t(X)^{n/2}
$$

This counts the perfect-matchings with multiplicity $n/2$ and runs in $O(2^n|E|n)$ time with $O(n\log(|E|))$ space.

We can do better via induced subgraphs. Note that $t(X)$ is equal to the number of edges in the induced graph $G[X]$. If we define $a(r,p)$ for $r=1,2,\dots,|E|$ and $p=0,1$ to the number of of $X\subseteq V$ with $t(X)=r$ and $n-|X|\equiv p\mod 2$ then we can rewrite the formula as:
$$
\sum_{r=1}^{|E|}(a(r,0)-a(r,1))r^{n/2}
$$

Which reduces the number of terms to polynomial in $|E|$.

So, now we count the number of induced graphs with $r$ edges. We do this by:

- Dividing the vertices in three sets $V_1\cup V_2\cup V_3=V$.
- Construct a tripartite graph $H$ with:
    - one vertex $v_X$ for every subset $X\subseteq V_1$
    - one vertex $v_Y$ for every subset $Y\subseteq V_2$ 
    - one vertex $v_Z$ for every subset $Y\subseteq V_3$. 
- $H$ now has size $N=3\cdot 2^{n/3}$.
Now add the following edges:
    - A weighted edge between $v_X$ and $v_Y$ with a weight equal to the number of edges in $G[X\cup Y]$ that have at least on endpoint in $X$.
    - A weighted edge between $v_Y$ and $v_Z$ with a weight equal to the number of edges in $G[Y\cup Z]$ that have at least on endpoint in $Y$.
    - A weighted edge between $v_Z$ and $v_X$ with a weight equal to the number of edges in $G[Z\cup X]$ that have at least on endpoint in $Z$.
- We've now created a graph where a triangle with a total weight of $r$ in $H$ corresponds to an induced graph with $r$ edges in $G$.
- Now, in a weighted graph where the integers are in the range $[0,1,M]$ we can reduce to triangle counting in an unweighted graph by iterating all possible combinations of $m_1 + m_2 + m_3 = r$. The number of these will be the number of triangles in the original graph with weight $r$.

We need to count triangles in $O(M^3)$ graphs with each taking $O(N^\omega)=O(2^\frac{\omega n}{3}=O(1.73^n)$ time

So.. the algorithm reduces to:

- Construct a large graph $H$
- Loop all values for $m_1+m_2+m_3=r$ and compute matrix multiplications to count triangles equal to $a(r,0)$ and $a(r,1)$.
- Then compute the number of perfect matchings as:
$$
\sum_{r=1}^{|E|}(a(r,0)-a(r,1))r^{n/2}
$$

This runs in $O(1.73^n)$ time and $O(2^{2n/3})$ space.

---
> Q: How can you speed this up on bipartite graphs, and what are the structures counted there?

The permanent of a $0/1$ square matrix is the number of perfect matchings in a bipartite graph. The permanent can by Ryser's algorithm be computes as:
$$
per(A)=\sum_{X\subseteq[n]}(-1)^{n-|X|}\prod_{i=1}^n\left(\sum_{j\in X}A_{ij}\right)
$$

The permanent differs from the determinant by not accounting for the sign of the permutation.

Calculating the permanent takes $O(2^nn^2)$ time but $n$ is now only half the size of the original graph.

---
> Q: Consider an n-vertex graph G. 

> _Q: How is the chromatic number of G defined? 

Chromatic number is defined as: What is the smallest number of colors needed to color the vertices so that no adjacent pair of vertices have the same color?

- A graph with chromatic number 1 has no edges as all vertices can be colored the same.
- A graph with chromatic number 2 is bipartite.
- A graph with chromatic number $n$ is complete.

> _Q: How can you compute the chromatic number in $O(3^n)$ time? The approach we’ve studied reduces the problem to counting certain structures. What are these structures and how fast can you count them?

We can use independent sets to solve the chromatic number problem. An independent set is a set of vertices where no two vertices are connected by an edges. So every color class is an independent set in the graph.

- Let the ground set $U$ be the vertices of the graph.
- Let $F$ be the independent sets in the graph.
- If $U$ can be convered by $k$ independent sets, then the chromatic number is $k$ or below.
- The smallest $k$ is the chromatic number.

We can do the calculation via induced subgraphs. First define $t(X)$ for a subset $X\subseteq V$ as the number of independent sets in the induced graph $G[X]$, then:

- Precompute $t(X)$ for all $X\subseteq V$.
- Set $k=1$
- While true:
    - Compute $r=\sum_{X\subseteq V}(-1)^{n-|X|}t(X)^k$
    - If $r>0$ then $k$ is the chromatic number.
    - Increment $k$

The running time of this is $O(2^nn)$.

# Graph Structure
## Cordal graphs (Lecture 13, 14 and 15)
> Q: What is a chordal graph and what is an interval graph?

**Interval Graphs:**

An interval graph is a graph that can be represented on a real line. Each vertex corresponds to an interval, fx an airport schedule. And two vertices are adjacent if and only if their intevals overlap. Formally stated as:

An interval model $I$ for a graph $G$ is a collection of intervals on the real line $I_1, I_2, \dots, I_n$ such that $v_iv_j\in E(G) \iff I_i\cap I_j\neq \emptyset$. The graph $G$ is an interval graph if it has an interval model.

Fx. a square is not an interval graph.

A feature of interval graphs is that a set of intervals that do not overlap is an independent set in the graph.

**Perfect Elimination Ordering:**

What is crucial to interval graphs is the order in which we process the vertices. Specifically we have to process them via a perfect elimination ordering. A perfect elimination ordering is an ordering of the vertices $v_1,v_2, \dots,v_n$ in $V(G)$ such that the neighbours of $v_i$ in the induced subgraph $G[\{v_1,\dots, v_{i-1}\}]$ form a clique.

Denote the neighbours of a vertex $v$ as $N(v)$. Then if $N(v_n)$ is a clique in $G$ the $v_n$ is called a simplicial vertex.

**Chordal Graphs:**

A graph is chordal if every cycle of length 4 or more has a chord. A chord is an edge that connects two non-consecutive vertices in the cycle. Say the edge in a square that makes it 2 triangles.

This means a chordal graph has no induced cycles of length 4 or more.

A graph is chordal if and only if it has a perfect elimination ordering.

All interval graphs are chordal graphs, but not all chordal graphs are interval graphs. This also means that an inteval graph has a perfect elimination ordering.

---
> Q: Show that every interval graph is a chordal graph.

If suffices to show that every interval graph has a perfect elimination ordering.

Observe that the cycle graph on $i$ vertices called $C_i$ does not have a perfect elimination ordering for any $i\geq 4$. This is because there is no simplicial vertex in $C_i$.

So, the second observation then is that if a graph has $C_i$ as an induced subgraph, then it does not have a perfect elimination ordering. 

Proof: Let $p_1,p_2,\dots,p_i$ be the vertices of the cycle, and assume for a contradiction that $G$ has a perfect eleimination ordering. The let $p_j$ be the rightmost vertex of the cycle in the perfect elimination ordering. That is, all vertices $\{p_1,p_2,\dots,p_i\}\setminus\{p_j\}$ appear before $p_j$ in the perfect elimination ordering. This leads to a contradiction since $p_{j-1}p_{j+1}\notin E(G)$ and both $p_{j-1}$ and $p_{j+1}$ appear before $p_j$ in the perfect elimination ordering.

---
> Q: Show that a graph is chordal if and only if it has a perfect elimination ordering.

Let $G$ be a chordal graph. We want to show that $G$ has a perfect elimination ordering.

Note that for any $v\in V(G)$, the graph $G-v$ is still chordal as we can never introduce a cycle by removing a vertex. 

It suffices then that if $G$ is chordal, then $G$ has at least one simplicial vertex. We can remove the simplicial vertices one by one from $G$ to obtain the perfect elimination ordering. This would prove that $G$ has a perfect elimination ordering.

---
> Q: Give a polynomial time algorithm to solve the Graph Coloring problem on chordal graphs. Argue for the correctness of the algorithm. What is the running time?

**Algorithm:**

An interesting property of graph coloring on chordal graphs, is that the chromatic number (described earlier) is equal to the largest clique in the graph. We can solve the problem as:

- Given a chordal graph $G=(V,E)$
- Find a perfect elminiation ordering $v_1,v_2,\dots,v_n$ of $V(G)$
    - The guarantee here is that every vertex $v\in N(v_1)$ after $v_1$ in the ordering form a clique.
- Color the vertices in reverse order $v_n,v_{n-1},\dots,v_1$ of the perfect elimination ordering. For each vertex $v_i$ assign the smallest color not used by any of its neighbours $N(v_i)$.
- Output the colors. The chromatic number is the largest color used.

**Correctness:**

The correctness of the algorithm follows from the properties of chordal graphs and perfect elimination orderings. Firstly, since it's a chordal graph it must have a perfect elimination ordering. This ordering ensures that when processing a vertex $v_i$ it's neighbours appear after it in the form of a clique.

We are sure to output an optimal coloring since we always assign the smallest color not used by any of the neighbours of $v_i$. As we process them in the order of a perfect elimination ordering then the number of colors required for $v_i$ and it's neighbours is at most the size of it's clique.

By assigning the smallest color every time, then we ensure that no two adjacencent vertices have the same color.

**Running Time:**

Using lexicographic breadth-first search due to Tarjan et al. we can find the PEO in $O(n+m)$ time.

The coloring algorithm runs in $O(n+m)$ time as well, since for each vertex we have to check the colours of it's neighbours.

The total running time is $O(n+m)$.

---
> Q: What is a clique tree for a chordal graph? Show how to construct a clique tree for a chordal graph in polynomial time.

**Definition:**

A clique tree for a chordal graphs is a tree $T$ with the following properties:

- Each node in $T$ corresponds to a maximal clique in the chordal graph $G$.
- For every vertex $v\in V(G)$, the set of nodes in $T$ whose cliques contain $v$ form a connected subtree in $T$.
- The intersection of any two cliques $C_i$ and $C_j$ in $G$ is contained in every clique on the path between the nodes $i$ and $j$ in $T$.

**Construction:**

We can construct a clique tree for a chordal graph in polynomial time using it's perfect elimination ordering:

- Find a perfect elimination ordering $v_1,v_2,\dots,v_n$ of $V(G)$.
- Find all maximal cliques by iterating over the vertices and savind the cliques formed by each vertex and it's neighbours that appear later in the ordering. A maximal clique is a clique that cannot have more vertices from $V$ added to it.
- Construct a graph $H$ where each maximal clique is a vertex and two vertices are connected if the corresponding cliques intersect on at least one vertex
- Assign a weight to each edge in $H$ equal to the number of vertices in the intersection of the corresponding cliques. Formally $w(C_i,C_j)=|C_i\cap C_j|$.
- Compute a maxmimum spanning tree of $H$ using Kruskal's algorithm.
- The maximum spanning tree is the clique tree.

**Running Time:**

- Finding the perfect elimination ordering takes, as before, $O(n+m)$ time.
- Finding the maximal cliques takes $O(n+m)$ time.
- Constructing the graph $H$ takes $O(k^2)$ time, where $k$ is the number of maximal cliques.
- Computing the maximum spanning tree takes $O(k^2\log k)$ time.

The running time then is polynomial in the size of the graph, since the number of maximal cliques $k$ is at most $n$.


## Solving problems on chordal graphs
> Q: Describe the Maximum Independent Set problem. How can you solve it on trees? How can you solve it on forests?

**Maximum Independent Set:**

An independent set in a graph is a set of vertices where no two vertices are connected by an edge. The Maximum Independent Set problem is the problem of finding the largest possible independent set in a given graph. This is an NP-hard problem.

**Solving on Trees:**

The Maximum Independent Set problem can be solved using dynamic programming on trees. Consider the tree $T$ rooted in a vertex $r$. Then if we pick $v\in V(T)$ that is not a leaf then $\{v\}$ is a separator of $T$.

A separator in a graph is a set of vertices $S\subseteq V(G)$ such that $G-S$ is disconnected. In a tree, a separator is a vertex that is not a leaf. That is, the removal of $v$ disconnects the tree. Indeed if there are no edges between vertices below $v$ then the rest of the vertices of $T$.

Let $T_v$ be the subtree of $T$ induced by $v$ and the descendants of $v$. Now, the key idea of solving problems on trees is to understand how a solution intersects $T_v$. There are two cases:

- A maximum independent set $I$ of $T$ contains $v$
- A maximum independent set $I$ of $T$ does not contain $v$

From this we can define our dynamic programming relations:

- $dp[v, 1]$ is the size of the maximum independent set of $T_v$ that contains $v$.
- $dp[v, 0]$ is the size of the maximum independent set of $T_v$ that does not contain $v$.

We want to calculate $\max(dp[r, 0], dp[r, 1])$ where $r$ is the root of the tree. Our base case for a leaf is 

- $dp[v, 1]=1$
- $dp[v, 0]=0$

Then let $v_1,\dots,v_q$ be the children of $v$. Then we can calculate the dynamic programming relations as:

- $dp[v, 1]=1+\sum_{i=1}^q dp[v_i, 0]$ because if $v$ is in the solution then none of it's children can be.
- $dp[v, 0]=\sum_{i=1}^q \max(dp[v_i, 0], dp[v_i, 1])$ because if $v$ is not in the solution then we can pick the maximum of the children.

**Solving on Forests:**

Since a forest is simply `a series of trees we can actually use the same algorithm. First find every tree, then for each tree run the DP algorithm above and sum the results. As the trees are disjoint the independent sets won't overlap, and it's therefore valid and safe to simply sum the results.

**Solving on nice clique trees**

See next question.

---
> Q: What is a nice clique tree?

First, recall i clique tree is a tree $T$ where every node $X_t$ is a bag of vertices that form a clique in the graph $G$, then we call $G_t$ the subgraph induced by the vertices in $X_t$.

A nice clique tree is a modified clique tree such that each node $t$ is one of the following:

- A leaf node $t$ has no children and is empty, $X_t=\emptyset$.
- An introduce node $t$ has one child $t'$. There then exists a vertex $v\in V(G)$ such that $X_t=X_{t'}\cup \{v\}$ where $v\notin X_{t'}$
    - Simplified: $t$ adds a vertex $v$ that was not in the bag $t'$.
- A forget node $t$ has one child $t'$. There then exists a vertex $v\in V(G)$ such that $X_t=X_{t'}\setminus \{v\}$ where $v\in X_{t'}$
    - Simplified: $t$ removes a vertex $v$ that was in the bag $t'$.
- A join node $t$ has two children $t_1$ and $t_2$. Then $X_t=X_{t_1}=X_{t_2}$
    - Simplified: $t$ is a common ancestor of $t_1$ and $t_2$ and they all have the same bag.

Now to solve the problem we revisit our DP relations, but define cases for each of the node types. First let $dp[t,S]$ be the size of the maximum independent set of $G_t$ that intersects $X_t$ precisely in $S$.

- For a leaf node $t$ we have $dp[t,S]=0$ for all $S$.
    - This is because a leaf node has no vertices.
- For an introduce node $t$ let $v$ be the new vertex, then we have the following cases:
    - $dp[t,\{v\}] = 1 + dp[t',\emptyset]$ because if $v$ is in the solution then none of the vertices in $t'$ can be.
    - $dp[t,\{u\}] = dp[t',\{u\}]$ for all $u\neq v$ because if $v$ is not in the solution then just keep the results of $t'$.
    - $dp[t,\emptyset] = dp[t',\emptyset]$ because if $v$ is not in the solution then just keep the results of $t'$.
        - The latter cases could be written as: $dp[t,S] = dp[t',S]$ for all $S\subseteq X_t,|S|\leq 1$ and $S\neq \{v\}$.
- For a forget node $t$ let $u\in X_t$ be all vertices of $t$ with $v$ being the forgotten vertex, then there are two cases:
    - $dp[t,\{u\}] = dp[t',\{u\}]$ because if $u$ is in the solution, then it must also intersect $t'$ precisely at $\{u\}$.
    - $dp[t,\emptyset] = max(DP[t', \{v\}, dp[t',\emptyset])$ because if $u$ is not in the solution then the solution either intersects $t'$ at $v$ or not at all.
- For a join node $t$ we have two cases:
    - $dp[t,\emptyset] = dp[t_1,\emptyset] + dp[t_2,\emptyset]$ because if the solution doesn't intersect $t$ then it must not intersect $t_1$ or $t_2$.
    - $dp[t,\{v\}] = dp[t_1,\{v\}] + dp[t_2,\{v\}] -1$ foreach vertex $v\in X_t$, because if the solution intersects $v$ then it must intersect both $t_1$ and $t_2$ in that vertex. But since $v$ is counted in both branches, we must subtract 1.

---
> Q: Describe the Feedback Vertex Set problem. Give a polynomial time algorithm to solve this problem on chordal graphs using a nice clique tree. What is the running time of the algorithm?

**Problem:**

In the Minimum Feedback Vertex Set problem the input is a graph $G$ and the task is to compute the minimum size of a set $S \subseteq V(G)$ such that $G - S$ is acyclic. The goal is to find the smallest set of vertices that need to be removed to make the graph acyclic.

**Algorithm:**

We look at the complement of $S$, let's call this $C$. This complement should then be the largest acyclic graph $G'$. So what we are looking for is the largest induced forest on $G$.

In a nice clique tree, $T$, every bag, $B$, contains a clique, therefore if a bag has 3 or more vertices in it, it must be a cycle, so we have to remove vertices until that is the case.

To define our dynamic programming approach, we first define $t$ as the subtree rooted in the given node of the nice clique tree. Then the bag of said node is $B_t$. Then define $dp[t][S]$ as the largest induced forest that intersects the bag $X_t$ exactly in $S$. $S$ is every subset of size 2 or less of the nodes in the bag $B_t$.

To create the DP table, we must then define a set of recurrence relations, split over each type of nice clique tree node:
- **Leaf node** The leaf node is empty, and the largest possible induced forest on 0 vertices is 0, therefore: $dp[t][\emptyset] = 0$ 
- **Introduce node** Let $v$ be the introduced vertex. Then there are 2 cases. Either $v$ is included in the forest, or excluded. So:
$$
dp[ t ][ S ] = \begin{cases}
 dp[ t' ][ S \setminus \{v\} ]+1 &\text{if } v\in S\\
 dp[ t' ][ S ] &\text{if } v\notin S
\end{cases}
$$
- **Forget node** Let $v$ be the forgotten vertex and $t'$ be the child tree. Again there are 2 possibilities. Either exclude $v$ from the forest, in which case the intersection is just $S$. Or include $v$, in which case the intersection then becomes $S\cup \{v\}$. This raises an issue when working with subsets of size 2, as $|S\cup \{v\}|$ would be 3, to solve this assume that a non-existing DP table entry resolves to $-\infty$, therefore the entry for a subset of size 2 would just be the child trees entry. Formally: 
$$
dp[ t ][ S ] = \begin{cases}
 \max\left(dp[ t' ][ S ],\ dp[ t' ][ S\cup \{v\} ]\right) &\text{if } |S| < 2\\
 dp[ t' ][ S ] &\text{otherwise}
\end{cases}
$$
- **Join node** Let $t_1$ and $t_2$ be the respective subtrees rooted in $t$. The DP value here should combine the result of both subtrees and then remove the overlap. The overlap must logically be equal to the size of the set $S$, since both subtrees must intersect in $S$, as they include the same vertices. Therefore the join node relation becomes:
$$
dp[ t ][ S ] = dp[ t_1 ][ S ] + dp[ t_2 ][ S ] - |S|
$$

To retrieve the result take the root node of the clique tree $r$ and take it's maxmimum DP value, $\max(dp[ r ][ S ])$. This is the size of the complement of the minimum feedback vertex set, therefore it must be subtracted from $|V(G)|$ to get the minimum feedback vertex set size. So $|V(G)|-\max(dp[ r ][ S ])$.

**Running Time:**

For each bag $B_t$ we create subsets of size 0,1 and 2. This is equivalent to $|{n \choose 0}|+|{n\choose 1}|+|{n \choose 2}|$ which resolves to $1+n+n^2$ so there are $O(n^2)$ subsets for each bag.

A nice clique tree contains $O(n^2)$ bags, therefore the runtime for computing the DP table is $O(n^2\cdot n^2)=O(n^4)$

# Parameterized algorithms
## Basics and Branching
> Q: What is a parameterized problem? What is an FPT algorithm? For which parameter choices does an FPT algorithm run in polynomial time?

**Parameterized Problem:**

A parameterized problem is a decision problem where input has two parts. The input instance and a parameter. The parameter is typically a number or some function/property of the input instance. Take the Vertex Cover problem, the input instance is a graph $G$ and the parameter is an integer $k$. The question is then: Does $G$ have a vertex cover of size at most $k$?

**FPT Algorithm:**

A Fixed-Parameter Tractable (FPT) algorithm is an algorithm that solves a parameterized problem in time $f(k)\cdot \text{poly}(n)$ or $f(k)\cdot n^c$ where $f$ is a function that depends on the parameter $k$, $poly(n)$ or $n^c$ is a polynomial function of the size of the input instance $n$ and $k$ is the parameter.

The key idea is that the exponential or super-polynomial complexity is confined to the parameter $k$, while the dependence on the input size $n$ remains polynomial. This makes FPT algorithms efficient for small values of $k$, even if the problem is NP-hard in general.

**For which parameter choices does an FPT algorithm run in polynomial time:**

When $k$ is fixed to a constant or a small value, then the function $f(k)$ becomes a constant and the running time simplifies to $poly(n)$ or $n^c$. This is when the FPT algorithm runs in polynomial time in the size of the input.

Fx. if $k$ is fixed to 2, then the running time of the FPT algorithm is $O(n^c)$. 

Fx. if $k=O(\log(n))$ then the running time of the FPT algorithm is $O(n^c\log(n))$, which is still polynomial in the size of the input. So if $k$ just grows slowly then it's also polynomial. 

Problems only arise when $k$ starts growing directly as a function of $n$, fx $k=n$ or $k=n^2$.

---
> Q: Describe how to solve the Vertex Cover problem in running time $O(2^kn)$, where k is the solution size.

The Vertex Cover problem states that given a graph $G=(V,E)$ and a parameter integer $k$, determine whether there exists a subset of vertices $S\subseteq V$ of size at most $k$ such that every edge in $E$ is incident to at least one vertex in $S$.

Within FPT we can solve this using a bounded search tree. The idea is to branch on the vertices of the graph, and at each step, we either include or exclude the vertex in the vertex cover. The branching factor is 2, as we have two choices for each vertex: include it in the vertex cover or exclude it.

Specifically:

- Let $G=(V,E)$ be the input graph and $k\geq 0$ be the parameter.
- Check the base cases:
    - If $k=0$, return True if $E=\emptyset$ and False otherwise.
    - If $E=\emptyset$, return True.
    - If $k<0$ return False, the vertex cover doesn't exist
- Recursive case while $k>0$:
    - Pick an edge $(u,v)\in E$. (For the vertex cover to exist either $u$ or $v$ must be in it)
    - Branch on two cases:
        - Include $u$ in the vertex cover and recursively solve the problem on $G-u$ with $k-1$.
        - Include $v$ in the vertex cover and recursively solve the problem on $G-v$ with $k-1$.
    - If any of the branches return True, return True, otherwise return False.

We can quickly see that the algorithm branches on 2 cases and that the depth of the recursion is at most $k$, therefore there must be at most $2^k$ leaves in the search tree. At each node in the search tree, we spend, in the worst case, $O(n)$ time to remove a vertex and it's edges. Thus the running time of the algorithm is $O(2^kn)$.

---
> Q: How can you improve the running time of the above algorithm?

**Kernelization:**

Kernelization is a technique used to reduce the size of the input instance while preserving the solution. The resulting smaller instance, called the kernel, should depend only on the parameter $k$.

For the Vertex Cover problem we can start by removing all vertices without any edges, so called isolated vertices. These vertices would never be part of the solution anyway.

Secondly, we can immediatly select all high-degree vertices, specifically all vertices with a degree $>k$ since they must be in the vertex cover, if they're not then all it's incident neighbours must be included, exceeding the size of $k$. This step also reduces the size of $k$ and thereby the size of the search tree.

Thirdly, remove all vertices with degree 1. These vertices must have their neighbours in the vertex cover, so just add the neighbour and remove the vertex. This works both for cases where its simply $a--b$ and where the neighbours are part of a larger structure.

The resulting size of the kernel is $O(k^2)$ edges and vertices. This is a polynomial kernel.

The resulting running time then goes from $O(2^kn)$ to $O(2^k k^2)+O(n+m)$ since it takes $O(n+m)$ time to go through the Kernelization step. Also remember that $k$ may have been reduced in the kernelization step.

---
> Q: How can you solve the Independent Set problem on 3-regular graphs in running time $O(4^kn)$?

The Independent Set problem is the problem of finding the largest possible set of vertices in a graph such that no two vertices are adjacent. The problem is NP-hard in general, but we can solve it on 3-regular graphs in time $O(4^kn)$ using a bounded search tree.

The idea is to branch on the vertices of the graph, and at each step, we either include or exclude the vertex in the independent set. The branching factor is 2, as we have two choices for each vertex: include it in the independent set or exclude it. Specifically:

- Let $G=(V,E)$ be the input graph and $k\geq 0$ be the parameter.
- Check the base cases:
    - If $k\leq 0$ return True, a set of size 0 is always independent.
    - If $|V|=0$ return True if $k=0$ and False otherwise.
- Recursive case while $k>0$:
    - Pick a vertex $v\in V$ of degree at most 3.
    - Branch on at most four cases for each vertex $u_1,u_2,u_3\in N(v)$:
        - Include $v$ in the independent set and compute $G'$ by removing $v$ and $N(v)$ from $G$. Recursively solve the problem on $G'$ with $k-1$.
        - Include $u_1$ in the independent set and compute $G'$ by removing $u_1$ and $N(u_1)$ from $G$. Recursively solve the problem on $G'$ with $k-1$.
        - Include $u_2$ in the independent set and compute $G'$ by removing $u_2$ and $N(u_2)$ from $G$. Recursively solve the problem on $G'$ with $k-1$.
        - Include $u_3$ in the independent set and compute $G'$ by removing $u_3$ and $N(u_3)$ from $G$. Recursively solve the problem on $G'$ with $k-1$.
    - If any of the branches return True, return True, otherwise return False.

In each branch we remove at most 4 vertices, and we do this at most $k$ times. This leaves $4^k$ leaves in the search tree. At each leaf we've removed at most $n$ vertices, therefore the running time is $O(4^kn)$.

---
> Q: Define a tournament. How can we solve Feedback Vertex Set on Tournaments in time $O(3^kn^3)$?

**Tournament:**

A tournament is a directed graph retrieved by assigning a direction to each edge in an undirected complete graph. Simplified, for every pair of vertices $u$ and $v$ there is exactly one directed between them, it can be in either direction. Thereby a complete graph is turned into a non complete graph when turned into a tournament. These graphs can be used to model competitions such as round robin tournaments.

**Feedback Vertex Set on Tournaments:**

The Feedback Vertex Set problem is the problem of finding the smallest set of vertices in a graph such that the removal of these vertices makes the graph acyclic. The size of the set of vertices must be at most $k$. The problem is NP-hard in general, but we can solve it on tournaments in time $O(3^kn^3)$ using, once again, a bounded search tree.

- Let $G=(V,E)$ be the input tournament and $k\geq 0$ be the parameter.
- Check the base cases:
    - If $k<0$, return False, the feedback vertex set doesn't exist.
    - If $G$ is acyclic, return True.
- Recursive case while $k>0$:
    - Find a directed cycle $C$ in $G$. If no cycle exists, return True
    - Let $C$ be a directed cycle of length 3. It is guaranteed that such a cycle exists in a tournament. Let $u,v,w$ be the vertices of the cycle.
    - Branch:
        - Include $u$ in the feedback vertex set and remove $u$ from the graph and recursively solve the problem on $G-u$ with $k-1$.
        - Include $v$ in the feedback vertex set and remove $v$ from the graph and recursively solve the problem on $G-v$ with $k-1$.
        - Include $w$ in the feedback vertex set and remove $w$ from the graph and recursively solve the problem on $G-w$ with $k-1$.
    - If any of the branches return True, return True, otherwise return False.

The algorithm will terminate when $k<0$ or the problem is solved. Once again let's calculate the running time. We know that the branching factor is 3, and the depth of the recursion is at most $k$. We can define the recurrence relation as:

$$
T(k,n) = 3T(k-1, n-3)
$$

Solving this gives a max amount of leaves of $O(3^k)$ but we must keep in mind that finding a cycle (triangle) in a graph takes $O(n^3)$ time using a brute-force algorithm, therefore the running time is $O(3^kn^3)$.

## Kernelization
> Q: What is a kernel for a parameterized problem?

A kernel is the result of preprocessing the input instance. Essentially the kernelization step solves the easy parts of the problem efficiently such that the hard parts, the core problem, can be solved more easily. The kernelization process is usually a polynomial-time algorithm.

Specifically, kernelization is the process of transforming an instance $(I, k)$ of a parameterized problem into a smaller instance $(I', k')$ such that:

- $(I, k)$ is a "yes" instance if and only if $(I', k')$ is a "yes" instance.
- The size of $I'$ is bounded by a function $f(k)$ (kernel size).
- The reduction is performed in polynomial time with respect to the input size $n$.

The function $f(k)$ determines the size of the kernel. If $f(k)$ is polynomial in $k$, the problem is said to admit a polynomial kernel. If $f(k)$ is exponential or larger, the kernel is considered less efficient.

Consider the Vertex Cover problem above for an example.

---
> Q: Argue that a parameterized problem has a kernel if and only if it is FPT.

A Fixed-Parameter Tractable (FPT) algorithm is an algorithm that solves a parameterized problem in time $f(k)\cdot \text{poly}(n)$ or $f(k)\cdot n^c$ where $f$ is a function that depends on the parameter $k$, $poly(n)$ or $n^c$ is a polynomial function of the size of the input instance $n$ and $k$ is the parameter.

Let's argue for 2 different cases 

**If a parameterized problem is FPT, then it has a kernel**

Suppose a parameterized problem $\Pi$ is FPT. This means there exists an algorithm that solves any instance $(I, k)$ of $\Pi$ in time $O(f(k) \cdot n^c)$ for some function $f$ and constant $c$.

To show that $\Pi$ has a kernel, we need to construct a polynomial-time algorithm that reduces $(I, k)$ to an equivalent instance $(I', k')$ whose size is bounded by a function of $k$.

1. Run the FPT algorithm for $O(f(k) \cdot n^c)$ steps.
2. If the algorithm terminates within this time, it either accepts or rejects the instance. In this case:
   - If the instance is accepted, reduce it to a trivial "yes" instance of constant size.
   - If the instance is rejected, reduce it to a trivial "no" instance of constant size.
3. If the algorithm does not terminate within $O(f(k) \cdot n^c)$ steps, then $n$ must be bounded by a function of $k$. This is because:
   - If $n > f(k)$, the running time $O(f(k) \cdot n^c)$ would exceed $O(n^{c+1})$, which is polynomial in $n$. However, since the problem is FPT, the algorithm must halt within $O(f(k) \cdot n^c)$ time, implying $n \leq f(k)$.
   - Thus, the original instance $(I, k)$ already has size $n \leq f(k)$, so no further reduction is needed.

This is the argument the book makes, if we flip it around we can argue the other way.


**If a parameterized problem has a kernel, then it is FPT**

Suppose a parameterized problem $\Pi$ has a kernel. This means there exists a polynomial-time algorithm that reduces any instance $(I, k)$ of $\Pi$ to an equivalent instance $(I', k')$ such that:
- $|I'| \leq f(k)$ for some function $f$, and
- $k' \leq g(k)$ for some function $g$.

After kernelization, the size of the instance $I'$ depends only on the parameter $k$, not on the original input size $n$.

We can now solve the kernelized instance $(I', k')$ using any brute-force or exact algorithm. Since $|I'| \leq f(k)$, solving $(I', k')$ takes time $h(f(k))$ for some function $h$.

The total time complexity is:
$$
\text{Time for kernelization} + \text{Time to solve the kernelized instance}.
$$
- Kernelization takes polynomial time, say $O(n^c)$ for some constant $c$.
- Solving the kernelized instance takes $h(f(k))$, which depends only on $k$.

Thus, the overall time complexity is $O(n^c + h(f(k)))$, which is FPT because the exponential part depends only on $k$.

In both cases, the instance $(I, k)$ is reduced to an equivalent instance $(I', k')$ whose size is bounded by a function of $k$. This satisfies the definition of a kernel.

The two directions together prove that a parameterized problem has a kernel **if and only if** it is FPT. This equivalence is a fundamental result in parameterized complexity and highlights the close relationship between kernelization and fixed-parameter tractability.

---
> Q: What is a polynomial kernel?

A kernel is the result of preprocessing the input instance. Essentially the kernelization step solves the easy parts of the problem efficiently such that the hard parts, the core problem, can be solved more easily. The kernelization process is usually a polynomial-time algorithm.

Specifically, kernelization is the process of transforming an instance $(I, k)$ of a parameterized problem into a smaller instance $(I', k')$ such that:

- $(I, k)$ is a "yes" instance if and only if $(I', k')$ is a "yes" instance.
- The size of $I'$ is bounded by a function $f(k)$ (kernel size).
- The reduction is performed in polynomial time with respect to the input size $n$.

The function $f(k)$ determines the size of the kernel. If $f(k)$ is polynomial in $k$, the problem is said to admit a polynomial kernel. If $f(k)$ is exponential or larger, the kernel is considered less efficient.

---
> Q: Give a kernel for the Vertex Cover problem parameterized by the solution size k with $O(k^2)$ vertices.

The Vertex Cover problem states that given a graph $G=(V,E)$ and a parameter integer $k$, determine whether there exists a subset of vertices $S\subseteq V$ of size at most $k$ such that every edge in $E$ is incident to at least one vertex in $S$.

Within FPT we can solve this using a bounded search tree. The idea is to branch on the vertices of the graph, and at each step, we either include or exclude the vertex in the vertex cover. The branching factor is 2, as we have two choices for each vertex: include it in the vertex cover or exclude it.

Specifically:

- Let $G=(V,E)$ be the input graph and $k\geq 0$ be the parameter.
- Check the base cases:
    - If $k=0$, return True if $E=\emptyset$ and False otherwise.
    - If $E=\emptyset$, return True.
    - If $k<0$ return False, the vertex cover doesn't exist
- Recursive case while $k>0$:
    - Pick an edge $(u,v)\in E$. (For the vertex cover to exist either $u$ or $v$ must be in it)
    - Branch on two cases:
        - Include $u$ in the vertex cover and recursively solve the problem on $G-u$ with $k-1$.
        - Include $v$ in the vertex cover and recursively solve the problem on $G-v$ with $k-1$.
    - If any of the branches return True, return True, otherwise return False.

We can quickly see that the algorithm branches on 2 cases and that the depth of the recursion is at most $k$, therefore there must be at most $2^k$ leaves in the search tree. At each node in the search tree, we spend, in the worst case, $O(n)$ time to remove a vertex and it's edges. Thus the running time of the algorithm is $O(2^kn)$.

In terms of kernelization for the Vertex Cover problem we can start by removing all vertices without any edges, so called isolated vertices. These vertices would never be part of the solution anyway.

Secondly, we can immediatly select all high-degree vertices, specifically all vertices with a degree $>k$ since they must be in the vertex cover, if they're not then all it's incident neighbours must be included, exceeding the size of $k$. This step also reduces the size of $k$ and thereby the size of the search tree.

Thirdly, remove all vertices with degree 1. These vertices must have their neighbours in the vertex cover, so just add the neighbour and remove the vertex. This works both for cases where its simply $a--b$ and where the neighbours are part of a larger structure.

The resulting size of the kernel is $O(k^2)$ edges and vertices, assuming it's a yes instance, since if there is more than $k^2$ edges the problem is unsolvable. This is a polynomial kernel.

The resulting running time then goes from $O(2^kn)$ to $O(2^k k^2)+O(n+m)$ since it takes $O(n+m)$ time to go through the Kernelization step. Also remember that $k$ may have been reduced in the kernelization step.

---
> Q: Define the Edge Clique Cover problem. Give a kernel for Edge Clique Cover parameterized by the solution size k. Is this a polynomial kernel?

**Edge Clique Cover:**

Given a graph $G=(V,E)$ and a parameter $k$, the Edge Clique Cover problem is to determine whether there exists a set of $k$ cliques in $G$ such that every edge in $E$ is covered by at least one of the cliques.

Recall that $N(v)$ is the set of neighbours of a vertex $v$. A clique is a set of vertices where every pair of vertices is connected by an edge. $N[v]=N(v)\cup \{v\}$ is the closed neighbourhood of $v$. Then apply the following rules:

- Remove isolated vertices.
- If there is an isolated edge $uv$, delete it and decrease $k$ by 1. Leaving $(G-\{u,v\}, k-1)$ 
- If there is an edge $uv$ whose endpoints have exactly the same closed neighbourhood, that is $N[u]=N[v]$, delete $v$ and decrease $k$ by 1. Leaving $(G-v, k-1)$.
    - The reason for this is that if $N[u]=N[v]$ then $u$ and $v$ can be treated the same in the final solution, so we just not to handle one of them. This bounds the size of the kernel and the vertices are called true twins.

This emits a kernel with at most $2^k$ vertices. This follows from the claim that if $(G,k)$ is a reduced  yes-instance, on which none the reduction rules can be applied, then $|V(G)|\leq 2^k$. To prove this let $C_1,\dots,C_k$ be the edge clique cover of $G$, where to prove by contradiction $|V|\geq 2^k$. Assign each vertex $v\in V$ a binary vector $b_v$ of length $k$ where bit $i$, $1\leq i\leq k$, is 1 if $v\in C_i$ and 0 otherwise. Since there are only $2^k$ possible vectors there must be a case where $u\neq v$ but $b_u=b_v$. If $b_u$ and $b_v$ are zero vectors then they are eliminated when removing isolated vertices. If $b_u=b_v$ and $b_u$ is not the zero vector then $u$ and $v$ are in the same cliques, which would mean that they have the same neighbourhood, therefore either the first or the second reduction applies. So... if $|V|\geq 2^k$ then the reduction rules can be applied, which is a contradiction to the initial assumption that $G$ was reduced proving the claim.

This is not a polynomial kernel, since the size of the kernel is exponential in $k$.

## Treewidth
> Q: Define the treewidth of a graph. Give examples for graph families with small and large treewidth (without proofs). Sketch the tree-decomposition for a grid.

Informally, threewidth is defined as the tree-likeness of a graph. Essentially, how much like a tree does the graph look like. 

Formally the treewidth is defined as the size of the largest vertex set in a tree decomposition, or as the size of the largest clique minus 1.

**Tree decomposition:**

A tree decomposition of a graph $G$ is a tree $T$ where each node $X_1, \dots, X_t$ is a subset of $V$ with the following properties:

- The union of all bags is the vertex set of $G$.
- If $X_i$ and $X_j$ both contain a vertex $v$ then all nodes on the path between $X_i$ and $X_j$ must also contain $v$. So... the nodes containing $v$ form a connected subtree in $T$.
- For every edge $uv$ in $G$ there exists a node $X_i$ containing both $u$ and $v$.

Then the width of a tree decomposition is the size of the largest bag $X_i$ minus 1. The treewidth of the graph $G$ defined as $tw(G)$ is the minimum with over all possible tree decompositions of $G$.

In terms of chordal graphs, the treewidth is the size of the largest clique that can contain $G$ with the smallest clique number. The clique cover number of a graph $G$ is the smallest number of cliques of G whose union covers the set of vertices V of the graph. 

**Examples:**

- The simplest is the tree, it has a treewidth of 1.
- A cycle has a treewidth of 2.
- A complete graph has a treewidth of $n-1$.
- $m\times n$ grid graphs have a treewidth of $min(m,n)$.
- Cliques have a treewidth of $n-1$.

**Sketch of a tree decomposition for a grid:**

Consider a $2\times 2$ grid graph. Square grids have a tree decomposition of size $k$, firstly by our knowledge of the treewidth of a grid graph, we know that the treewidth of a $2\times 2$ grid is 2. We can quickly prove this by using the graph:

```
1 - 2
|   |
3 - 4
```

The bags would be $\{1,2,3\},\{2, 4, 3\}$ and the tree would look like:

```
\{1,2,3\}
  |
\{2,4,3\}
```

We can say that it is size $k$ since the first set ensures we never have to use vertex 1 again, the second vertex 2, and so on. This is a tree decomposition of size 2. Usually the tree decompositions of a square grid is a "snake" path through the grid, take a $2\times 4$ grid for example:

```
1 - 2 - 3 - 4
|   |   |   |
5 - 6 - 7 - 8
```

The bags would be $\{1, 2, 5\}, \{2, 3, 6\}, \{3,7,4\}, \{4, 7, 8\}$

All grids compose into a line, same with cycles.

---
> Q: What is a nice tree-decomposition? Why is it useful?

A nice tree-decomposition is a nice decomposition much like nice-clique trees such that:

- A leaf node $t$ has no children and is empty, $X_t=\emptyset$. This also include the root node.
- An introduce node $t$ has one child $t'$. There then exists a vertex $v\in V(G)$ such that $X_t=X_{t'}\cup \{v\}$ where $v\notin X_{t'}$
    - Simplified: $t$ adds a vertex $v$ that was not in the bag $t'$.
- A forget node $t$ has one child $t'$. There then exists a vertex $v\in V(G)$ such that $X_t=X_{t'}\setminus \{v\}$ where $v\in X_{t'}$
    - Simplified: $t$ removes a vertex $v$ that was in the bag $t'$.
- A join node $t$ has two children $t_1$ and $t_2$. Then $X_t=X_{t_1}=X_{t_2}$
    - Simplified: $t$ is a common ancestor of $t_1$ and $t_2$ and they all have the same bag.

This decomposition is very useful for describing algorithm details. If a tree decomposition exists with a width of at most $k$ then a nice tree decomposition exists with the same width and can be compute in time $O(k^2\cdot \max(|V(T), |V(G)|))$ they can be assumed to have $O(k|V(G))$ nodes.

---
> Q: Describe how to solve the Maximum Independent Set problem on graphs of bounded treewidth.

**Maximum Independent Set:**

An independent set in a graph is a set of vertices where no two vertices are connected by an edge. The Maximum Independent Set problem is the problem of finding the largest possible independent set in a given graph. This is an NP-hard problem.

**Solution on graphs of bounded treewidth:**

First, assume that we have the tree decomposition, and a nice tree decomposition at that. Call the decomposition $T$, a node in the tree $t$ and it's bag $X_t$.. Then store the table $dp[t][S]$ where $S$ is $S\subseteq X_t$ that stores the size of the largest independent set in the subgraph induced by $X_t$ that intersects exactly in $S$.

Define for each node type:

- Leaf node: $dp[t][\emptyset]=0$
    - Since a leaf node is always empty
- Introduce node: Let $v$ be the introduced vertex, then there 2 cases. If $v\in S$ then it must not be adjacent to any vertex in $S$, if not then it can be included in the independent set. So:
    $$
    dp[t][S] = \begin{cases}
    dp[t'][S\setminus \{v\}]+1 &\text{if } v\in S\\
    dp[t'][S] &\text{if } v\notin S
    \end{cases}
    $$
- Forget node: Let $v$ be the forgotten vertex, the for each subset $S$ we can either exclude $v$ from the independent set, in which case the intersection is just $S$. Or include $v$, in which case the intersection then becomes $S\cup \{v\}$. Select the maximum of the two. So:
    $$dp[t][S] = \max(dp[t'][S], dp[t'][S\cup \{v\}])$$
- Join node: Let $t_1$ and $t_2$ be the respective subtrees rooted in $t$. The DP value here should combine the result of both subtrees and then remove the overlap. The overlap must logically be equal to the size of the set $S$, since both subtrees must intersect in $S$, as they include the same vertices. Therefore the join node relation becomes:
    $$dp[t][S] = dp[t_1][S] + dp[t_2][S] - |S|$$

The answer, since we go bottom up, should then be $\max(dp[r][S])$ where $r$ is the root node of the tree decomposition and $S$ is every set in $dp[r][S]$.

**Running Time:**

We have a treewidth of $k$, and since the treewidth is the size of the largest bag minus 1, then the largest bag must be at most $k+1$ vertices. Therefore there are at most $2^{k+1}$ subsets. The number of nodes in the tree decomposition is $O(k|V(G)|)$, so the running time is $O(2^{k+1}\cdot k\cdot |V(G)|)$.

**Vertex Cover is FPT parameterized by treewidth:**

The Vertex Cover problem states that given a graph $G=(V,E)$ determine the smallest subset of vertices $S\subseteq V$ such that every edge in $E$ is incident to at least one vertex in $S$.

This is simply the complement of the independent set. Formally: A set $C$ is a vertex cover if and only if its complement $V\setminus C$ is an independent set. So the size of the minimum vertex cover is $|V|- \text{size of the maximum independent set}$.

Since we have a solution for the maximum independent set on graphs of bounded treewidth, we can use this to solve the vertex cover problem. The running time is the same as for the maximum independent set, $O(2^{k+1}\cdot k\cdot |V(G)|)$.

- The Vertex Cover problem states that given a graph $G=(V,E)$ and a parameter integer $k$, determine whether there exists a subset of vertices $S\subseteq V$ of size at most $k$ such that every edge in $E$ is incident to at least one vertex in $S$.

---
> Q: Describe how to solve the 3-coloring problem on graphs of bounded treewidth.

The 3-coloring problem asks whether the vertices of a graph can be colored using at most 3 colors such that no two adjacent vertices share the same color

First, assume that we have the tree decomposition, and a nice tree decomposition at that. Call the decomposition $T$, a node in the tree $t$ and it's bag $X_t$.. Then store the table $dp[t][c]$ where $c$ is a 3-coloring of $X_t$. $dp[t][c]$ is true if the subgraph induced by $X_t$ can be 3-colored with the coloring $c$, otherwise it's false.

- Leaf node: $dp[t][\emptyset]=\text{True}$, an empty graph can always be 3-colored.
- Introduce node: Let $v$ be the introduced vertex. Then for each coloring $c'$ of the child bag, loop through $\{1,2,3\}$ called $c$. Check if assigning the color $c$ to $v$ is valid in $c'$, if valid then set $dp[t][c' \cup \{v\rightarrow c\}]=true$, otherwise false.
- Forget node: Let $v$ be the removed vertex. Then for each coloring $c'$ of the child bag, if $dp[t'][c'\setminus \{v\}]$ is true then set $dp[t][c']=true$, otherwise false.
- Join node: Let $t_1$ and $t_2$ be the respective subtrees rooted in $t$. Then for each coloring $c$ of the child bags, if $dp[t_1][c]$ and $dp[t_2][c]$ are true then set $dp[t][c]=true$, otherwise false.

The answer is then $\text{True}$ if there exists a coloring $c$ of the root node such that $dp[r][c]=true$.

**Running Time:**

Each bag has at most $k+1$ vertices, with each vertex having 3 possible colors. Therefore each bag has at most $3^{k+1}$ colorings, there are $O(k|V(G)|)$ nodes in the tree decomposition. The running time is then $O(3^{k+1}\cdot k\cdot |V(G)|)$.

---
> Q: Describe how to solve the MaxCut problem on graphs of bounded treewidth.

See assignment 5 exercise 3.

---
> Q: Describe the idea of a win-win approach to design parameterized algorithms.

In parameterized complexity, the following win/win approach is commonly exploited. Given some computational problem, let us try to construct a good tree decomposition of the input graph. If we succeed, then we can use dy- namic programming to solve the problem effeciently. On the other hand, if we fail and the treewidth is large, then there is a reason for this outcome. This reason has the form of a combinatorial obstacle embedded in the graph that forbids us to decompose it expeditiously. However, the existence of such an obstacle can also be used algorithmically. For example, for some problems like Vertex Cover or Feedback Vertex Set, we can immediately con- clude that we are dealing with a no-instance in case the treewidth is large. For other problems, like Longest Path, large treewidth implies that we are working with a yes-instance. In more complicated cases, one can examine the structure of the obstacle in the hope of finding a so-called irrelevant vertex or edge, whose removal does not change the answer to the problem. Thus, regardless of whether the initial construction of a good tree decomposition succeeded or failed, we win: we solve the problem by dynamic programming, or we are able to immediately provide the answer, or we can simplify the problem and restart the algorithm.

---
> Q: What does it mean that H is a minor of G? What does the Excluded Grid Minor Theorem say? How is it helpful to the win-win approach?

A minor $H$ is a graph that can be obtained from $G$ by performing a sequence of:

- Edge deletion
- Vertex deletion
- Edge contraction: Contract an edge, merging its two endpoints into a single vertex and preserving all connections to the rest of the graph.

If $H$ can be obtained from $G$ then we say that $G$ contains a minor $H$, denoted $H\preceq G$.

**Excluded Grid Minor Theorem:**

The Exluded Grid Minor Theorem states that there is a function $f=O(t^{98+o(1)})$ such that for every integer $k$, every graph $G$ of treewidth at least $f(k)$ contains a $k\times k$ grid as a minor.

**Win-Win Approach:**

The theorem allows us to focus on the grids in the case that the tree-width is large. Grids are fx. pretty useful when talking about the cycle packing problem, since a grid is a set of cycles.

This picture means i have given up.....

![image](./pictures/FScreenshots_133.png)

---
> Q: What does the Planar Excluded Grid Minor Theorem say? How is it helpful to design subexponential parameterized algorithms on planar graphs? (Recall, in this case subexponential algorithms are those with running time $2^{O(\sqrt{k})}n^{O(1)}$ where $k$ is the solution size.

*This entire thing is completely bullshit/wrong i'm very tired*

Let $t$ be a nonnegative integer. Then every planar graph $G$ of treewidth at least $9t/2$ contains $\boxplus_t$ as a minor. Furthermore, for every $\epsilon > 0$ there exists an $O(n^2)$ algorithm that, for a given n-vertex planar graph $G$ and integer $t$, either outputs a tree decomposition of G of width at most $(9/2 + \epsilon )t$, or constructs a minor model of $\boxplus_t$ in $G$.

In other words. The function $g$ is linear. Since $\boxplus_t$ has $t^2$ vertices, every graph containing $\boxplus_t$ has at least $t^2$ vertices. This leads to a second conclusion: The treewidth of an $n$ vertex planar graph $H$ is less than $\frac{9}{2}\sqrt{n+1}$ and can be constructed in time $O(n^2)$.

The theorem helps designing parameterized algorithms usin a win-win approach. Given a planar graph $G$ and a parameter $k$ compute it's treewidth $t$. Then by the theorem we have 2 cases:

- If $t\leq 9k/2$ then we can compute a tree decomposition of width at most $(9/2+\epsilon)k$ in time $2^{O(\sqrt{k})}n^{O(1)}$
- If $t>9k/2$ then $G$ contains $\boxplus_k$ as a minor, and we can in many instances, like vertex cover, conclude that $G$ is a no-instance from such a large grid minor

Both approaches work since we emit a sub-exponential algorithm in the first case and a quick answer in the second case.

---
> Q: How can we solve Vertex Cover and k-Path in time $2^{O(\sqrt{k})}n$ on planar graphs?

**Vertex Cover:**

First compute the treewidth of the graph $G$. If the treewidth is at most $9k/2$ then compute a tree decomposition of width $O(k)$ and use dynamic programming to solve the problem. The running time is $2^{O(\sqrt{k})}$.

On the other hand if the treewidth is larger than $9k/2$ then the graph contains a $\boxplus_k$ minor. Since $\boxplus_k$ requires a vertex cover of size at least $k$, then it depends on the input parameter whether the answer is yes or no. Let the param be $k'$, then the answer is no if $k'>k$ and yes if $k'\leq k$. The running time is $O(n^2)$.


Same case with $k-path$.

## Color-coding
> Q: Describe the “color-coding” algorithm for deciding whether a graph has a path of length k. Make sure to explain the role of random colorings and walks. What changes if you want to decide the existence of cycles rather than paths?

*I have officially given up. My brain has the same consistency as oatmeal*

The color-coding algorithm is a randomized approach that works as follows:

1. Random Coloring Phase:
    - Randomly assign each vertex in the graph one of $k$ colors
    - Each color is chosen independently and uniformly at random
    - This creates a vertex-colored graph
2. Dynamic Programming Phase:
    - Search for a "colorful" path - a path where each vertex has a distinct color
    - Use dynamic programming to find such a path efficiently:
      - For each vertex $v$ and each subset $S$ of colors
      - Compute whether there exists a path ending at $v$ that uses exactly the colors in $S$
      - Build up from smaller color sets to larger ones
      - Can find a colorful path in $O(2^k * n)$ time if it exists


Since each vertex needs a different color, then if a $k$-length path exists, the probability that our random coloring makes it colorful is $k!/k^k$. By repeating the random coloring $e^k$ times, we get a high probability of success.

For cycles instead of paths:
- The main modification is in the dynamic programming phase
- Need to keep track of both:
  - The starting vertex of the potential cycle
  - The current vertex we're at
- When completing a potential cycle, check if we can return to the starting vertex
- Still look for colorful sequences, but now need to return to the start
- The probability analysis remains similar since we're still looking for k distinct colors

The beauty of this algorithm is that it converts the problem of finding a specific substructure (k-length path) into finding a colorful path in a randomly colored graph, which turns out to be easier to solve using dynamic programming.

The algorithm runs in $2^{O(k)} * n^{O(1)}$ time and succeeds with high probability, making it an FPT (Fixed-Parameter Tractable) algorithm with parameter k.

---
> Q: How can you determine the existence of a colorful k-path in a vertex-colored graph in time $(k+1)!*n^{O(1)}$ or $2^kn^{O(1)}$ (For the second running time, modify the DP for Hamiltonian paths.)

no clue

# Approximation algorithms
## Formalizing approximation problems
> Q: What is an NP-optimization problem?

: This involves finding the best solution from a finite set of possible solutions. The "best" solution is typically defined by an objective function that needs to be maximized or minimized. Examples include:

- Graph Coloring: What is the least number of colors needed to color the vertices in a graph so that no two adjacent vertices have the same color?
- Independent Set: What is the size of the largest subset of vertices such that no two vertices in the set are adjacent?
- Vertex Cover: What is the size of the smallest subset of vertices such that every edge has at least one endpoint in the set?
- Maximum Cut: What is the maximum number of edges going from one part to the other in a vertex bipartition?
- Euclidean TSP: Given set of points in the Euclidean plane, find the length of the shortest closed tour visiting every vertex.
- Minimize makespan on two identical machines: Given $n$ jobs with individual processing times $t_1, t_2,\dots, t_n$, partition them on two machines so that the time to process all jobs is minimized.
- Boolean MAX-3-CNF Satisfiability: Given a Boolean formula in conjunctive normal form, with three literals per clause, find an assignment that satisfies as many clauses as possible. 
- Set Cover: Given a universe set $U$ on n elements and a family $F$ of subsets of $U$. What is the least number of sets from $F$ needed to cover $U$? 

An NP-hard problem is one where the solution can be verified in polynomial time, but there is no known polynomial-time algorithm to find the solution. Approximation algorithms are used to find near-optimal solutions to NP-hard optimization problems.

An optimization problem $P=(I, SOL, m, goal)$, where:

- $I$ is the set of instances
- $SOL$ is a function that maps an instance $x\in I$ to a set of feasible solutions $SOL(x)$
- $m$ is a function that maps an instance $x$ and a solution $y$ to a real number $m(x, y)$, the measure of the solution. (i think)
- $goal$ is either "min" or "max" to indicate whether the goal is to minimize or maximize the measure function $m$.

belongs to the class of NP-Optimisation problems if:

- The set of instances $I$ is recognized in polynomial time.
- There exists a polynomial $q$ such that given any instance $x\in I$, for any $y$ such that $|y|\leq q(|x|)$, it can be decided in polynomial time whether $y$ is a solution to $x$, $y\in SOL(x)$.
    - Informally this means that we can verify a solution in polynomial time.
- The measure function $m$ is computable in polynomial time.
- The goal is to minimize or maximize the measure function $m$.

---
> Q: What is the definition of approximation ratio?

The approximation ratio of an algorithm for an optimization problem is a measure of how well the algorithm approximates the optimal solution. It is defined as the ratio of the value of the solution produced by the algorithm to the value of the optimal solution. Specifically:

- For a minimisation problem, the approximation ratio is the value of the algorithm's solution divided by the value of the optimal solution: $\alpha=\frac{\text{APX}}{\text{OPT}}$.
- For a maximisation problem, the approximation ratio is the value of the optimal solution divided by the value of the algorithm's solution: $\alpha=\frac{\text{OPT}}{\text{APX}}$.

The approximation value will always be greater than or equal to 1. The closer the approximation ratio is to 1, the better the algorithm's approximation of the optimal solution.

---
> Q: What is a PTAS and what is an FPTAS? Which one is more desirable in theory? Give examples for running times that match the definitions of PTAS and FPTAS algorithms.

**PTAS (Polynomial-Time Approximation Scheme):**

For every $\epsilon > 0$, there is an $O(n^{f(\epsilon^{-1})}$ algorithm with approximation ratio $\alpha=(1+\epsilon)$.

**FPTAS (Fully Polynomial-Time Approximation Scheme):**

For every $\epsilon > 0$, there is a polynomial-time ($poly(\epsilon^{-1}, n)$) time algorithm with approximation ration $\alpha=(1+\epsilon)$.

Also, if it is a randomized algorithm, only obtaining the approximation guarantee with some nonzero constant probability, we call it a FPRAS (Fully Polynomial Randomized Approximation Scheme).

**EPTAS (Efficient Polynomial-Time Approximation Scheme):**

For every $\epsilon > 0$, there is a $f(\epsilon^{-1}poly(n)$ time algorithm with approximation ration $\alpha=(1+\epsilon)$.

Note that an EPTAS could have much worse dependence on $\epsilon$ than a FPTAS, but it is still polynomial in $n$.

**Desirability:**

In theory FPTAS is more desirable as it's running time scales polynomially in both $\epsilon$ and the input size $n$. The approximation ratio in  these algorithms is defined by $\epsilon$, so, compared to the other algorithms, FPTAS actually still remains computationally feasible when high levels of precision is required, aka when $\epsilon$ is small. PTAS is still useful as it's polynomial in the size of the input size but may be exponential in $\epsilon^{-1}$.

(Quick note: $\epsilon^{-1} = \frac{1}{\epsilon}$))

**Examples:**

- Euclidean TSP has a PTAS ruuning in $O(n^{O(\epsilon^{-1})})$, fx. if $\epsilon=0.1$ the running time is $O(n^{O(10)})$, so it's polynomial in $n$ but exponential in $\epsilon^{-1}$.
- Knapsack has a FPTAS running in $O(n^{3}/\epsilon)$. IF we take $n=1000$ and $\epsilon=0.1$ then the running time is $O(1000^3/0.1)=O(10^9)$, which is polynomial in both $n$ and $\epsilon$.

## Approximating vertex-cover
> Q: Describe the matching-based algorithm for finding a vertex-cover in a graph that is at most twice as large as the minimum vertex-cover. 

The vertex cover problem is to find the smallest subset of vertices in a graph such that every edge is incident to at least one vertex in the subset. 

The matching-based algorithm works by finding a maximal matching $M$ in the graph. A maximal matching is a matching that cannot be extended by adding more edges. Compared to the maximum matching, which is the largest possible matching in the graph, the maximal matching is easier to find and is not guaranteed to be optimal. Every maximum matching is maximal, but not every maximal matching is maximum:

![image](./pictures/FScreenshots_137.png)

When we have a maximal matching $M$, we can let the vertex cover be all vertices adjacent to an edge in $M$. This is a vertex cover because every edge in in the graph, by definition, has at least one vertex in a maximal matching $M$. Therefore if we take both endpoints of every such edge, then we have a vertex cover.

If we were to find a minimum vertex cover, then we also know that for each of the edges in the matching, at least one of the endpoints must be in the minimum vertex cover. Therefore the size of the vertex cover is at most twice the size of the maximal matching.

Since the size of a maximal matching is less thant the size of a maximum matching we get the approximation ratio 2.

We can define the algorithm as:

1. Given a graph $G=(V,E)$.
2. Find a maximal matching $M$ in the graph $G$.
3. Include both endpoints of each edge in the matching in the vertex cover. Specifically for every edge $(u,v)\in M$, add both $u$ and $v$ to the vertex cover $C$
4. Return the vertex cover $C$.

> _Q: What does the existence of a k-edge matching imply for the minimum size of a vertex-cover?

If there exists a k-edge matching in a graph, then the minimum size of a vertex cover is at least $k$, since each edge in the matching must have at least one endpoint in the vertex cover.

> _Q: How does it matter whether you consider maximum matchings or maximal matchings in the algorithm? Which is the better choice?

Both will work, by definition "Every maximum matching is maximal, but not every maximal matching is maximum". But, in this case a maximal matching will do the job, and is far easier to find. IT can be found greadily in $O(|E|)$ time, while a maximum matching requires more complex algorithms.

But, the maximum matching will be bigger, by definition, and therefore results in a smaller potentital vertex cover. But in our algorithm we will output a larger vertex cover.

> _Q: Give an infinite family of example graphs on which the algorithm indeed outputs only a 2-approximate solution. Also give a family of example graphs on which the algorithm outputs an optimal solution.

- Bipartite graphs: In this graph type there will be two sets of vertices where every vertex in the set $A$ is connected to every vertex in the set $B$. A maximal matching will be the size of the smallest set, and the vertex cover will be outputted as the size of both sets. So if we say both sets are $n$ size it will output $2n$
- Star graphs: A start graph is a graph with a center vertex, and $n$ outer vertices. A maximal matching will be the center vertex and 1 outer vertex, and the vertex cover will be the center vetex. So the output will be $2$.

## Coloring 3-colorable graphs
> Q: Given a 3-colorable n-vertex graph, show how you can in polynomial time find a proper $O(\sqrt{n})$-coloring of the graph.

As input we get an $n$-vertex graph $G$ that we are promised to admit a proper 3-coloring. We want to find a proper $k$-coloring of $G$ in polynomial time in $n$ with as small a $k$ as possible

We know that since the graph is 3-colorable, every vertex neighborhood must be bipartite. We can color a bipartite graph fast by:

1. Pick a vertex with more than $\sqrt{n}$ uncolored neighbors.
2. Color all of them with 3 new colors
3. Repeat until there are no such vertices left
4. Greadily color the remaining vertices using $\sqrt{n}$ colors.

This all uses $O(\sqrt{n})$ colors.

![image](./pictures/FScreenshots_138.png)

The key insight here is that we are looking at the graphs independent set. In a 3-colorable graph, at least one color class must contain at least 1 third of the vertices ($n/3$), which provides us with the strategy of repeatetedly finding a large independent set and coloring it with new colors. So if we rewrite our algorithm:

1. Find a large independent set of size at least $\sqrt{n}$
2. Color all vertices in the independent set with a new color
3. Remove the vertices from the graph
4. Repeat until the graph is empty


## Metric problems and TSP
> Q: What does it mean that a graph has metric costs/weights?

A graph has metric costs if the edge weights satisfy the triangle inequality. The triangle inequality states that given a graph $G=(V,E)$ with edge weights $w:E\rightarrow \mathbb{R}_{\geq 0}$, the weights are metric if for any three vertices $u,v,x\in V$ the following holds:

$$
w(u,v)\leq w(u,x)+w(x,v)
$$

![image](./pictures/FScreenshots_139.png)

Implications:

1. **Triangle Inequality**: The direct edge between two vertices $u$ and $v$ is no longer than any indirect path through a third vertex $w$. This ensures that the shortest path between two vertices is always the direct edge (if it exists).
2. **Non-Negativity**: Metric weights are non-negative ($w(u, v) \geq 0$), which is a standard requirement for edge weights in most graph algorithms.
3. **Symmetry**: Metric weights are symmetric, meaning $w(u, v) = w(v, u)$ for all $u, v \in V$. This is often assumed in undirected graphs.
4. **Reflexivity**: The weight from a vertex to itself is zero ($w(u, u) = 0$).

---
> Q: What is the Steiner Tree problem?

Given a graph $G=(V,E)$ with edge weights $w:E\rightarrow \mathbb{R}_{\geq 0}$, and a set of required vertices $\subseteq V$. The Steiner Tree problem is to find a minimum-total-weight tree containing all the vertices in $R$. The tree may use some or all of the vertices in $V$, but the goal is to minimize the total weight of the tree.

![image](./pictures/FScreenshots_140.png)

> _Q: How can it be reduced to a version in which the input graph is required to have metric costs?

Given an instance $I=(G, w, R)$ to the Steiner Tree problem, we can construct an instance $I'=(G', w', R')$ with metric costs as follows:

1. Keep the same vertices in $I'$ as in $I$, but let $G'$ be the complete graph on $V$.
    - A complete graph has an edge between every pair of vertices.
2. Let $w(u,v)$ be equal to the length of the shortest path between $u$ and $v$ in the original graph $G$.
    - This ensures that the edge weights satisfy the triangle inequality.
3. Let $R'=R$ be the same set of required vertices.

We can then solve the Steiner Tree problem on the instance $I'$ with metric costs, using minimum spanning trees, in polynomial time:

![image](./pictures/FScreenshots_141.png)

> _Q: Give a 2-approximation for Metric Steiner Tree.

A minimum spanning tree is actually a 2-approximation for the Metric Steiner Tree problem. Given a graph $G=(V,E)$ with metric costs, and a set of required vertices $R\subseteq V$, the algorithm works as follows:

1. Consider the subgraph $G'$ induced by the vertices in $R$.
2. Compute the minimum spanning tree $T$ of $G'$.
3. Output the tree $T$ as a 2-approximation for the Metric Steiner Tree.

We can see that this works:

1. Consider an optimal Steiner Tree:

![image](./pictures/FScreenshots_142.png)

2. Double all edges and construct an Euler tour, the lenght of the tour will be $2*OPT$:

![image](./pictures/FScreenshots_143.png)

3. Relax the Euler tour to a Hamiltonian cycle of the required vertices. Due to the triangle inequality, the length of the Hamiltonian cycle is at most $2*OPT$, as it can never be larger than the Euler tour:

![image](./pictures/FScreenshots_144.png)

4. Remove an edge from the Hamiltonian cycle to get a spanning tree of the required vertices. The Minimum Spanning Tree can never be of larger weight than this tree, as it by definition is the minimum tree. And this tree will be at most $2*OPT$.

![image](./pictures/FScreenshots_145.png)

---
> Q: Define the TSP and argue that it is NP-complete.

TSP (Traveling Salesman Problem) is an optimization problem where the goal is to find the shortest possible tour that visits every vertex exactly once and returns to the starting vertex. The tour must be a cycle that visits every vertex in the graph.

Formally, given a complete undirected graph $G=(V,E)$ with positive edge weights $w:E\rightarrow \mathbb{R}_{>0}$, the TSP problem is to find a cycle that visits every vertex in $V$ exactly once and returns to the starting vertex, minimizing the total weight of the cycle.

This problem is special in the fact that it cannot be approximated. We can argue for that by embedding a graph $H=(V,F)$ in the complete undirected graph $G$ with edge weights $w(u,v)=1$ if $(u,v)\in F$ otherwise set $w(u,v)=M$ for an abritrarily large $M$. The result of this would be that any TSP tour that does not correspond to a Hamiltonian cycle in H, must have weight at least $M+(n-1)$. 

---
> Q: Show that TSP remains NP-complete on metric instances.

Firstly define the metric TSP problem:

Given a complete undirected graph $G=(V,E)$ with metric costs, the metric TSP problem is to find a cycle that visits every vertex in $V$ exactly once and returns to the starting vertex, minimizing the total weight of the cycle. The edge weights satisfy the triangle inequality. As before:

The answer essentially remains the same. We can reduce the Hamiltonian cycle problem to the metric TSP problem by constructing a complete graph with metric costs. So let's do that:

- Let $G=(V,E)$ be an instance of the Hamiltonian cycle problem.
- Construct a complete graph $G'=(V,E')$ with metric costs:
    - For each edge $(u,v)\in E(G')$:
        - If $(u,v)\in E(G)$, set $w(u,v)=1$
        - If $(u,v)\notin E(G)$, set $w(u,v)=2$
    - Then a target weight for the solution to TSP would be $|V|$.
- Ensure the metric property:
    - For any three vertices $u,v,x$ in $V$, the triangle inequality holds:
        - If $u,v\in E(G)$, then $w(u,v)=1$ and $w(u,x)+w(x,v)=1+1=2\geq 1=w(u,v)$
        - If $u,v\notin E(G)$, then $w(u,v)=2$ and $w(u,x)+w(x,v)=1+1\geq 2=w(u,v)$
- If $G$ has a Hamiltonian cycle, then the same cycle in $G'$ will have weight $|V|$ and be a solution to the metric TSP problem.
- If $G$ does not have a Hamiltonian cycle, then any cycle in $G'$ must use at least one edge of weight 2, making the total weight at least $|V|+1$.

---
> Q: How do the general TSP and the metric TSP differ in terms of approximability? Argue that the general TSP cannot be approximated within a constant factor unless P=NP.

We can do the same reduction as before, and then twist it at the end

1. Consider a minimum spanning tree on the TSP problem instance
2. Double all edges and construct an Euler tour, the length of the tour will be $2*OPT$, but remember that the minimum spanning tree will be less than the minimum TSP tour, since the tree will not contain the edge that goes back to the starting vertex:

![image](./pictures/FScreenshots_146.png)

3. Relax the Euler tour to a Hamiltonian cycle of the required vertices. The hamiltionian cycle will be no longer than twice the weight of the spanning tree:

![image](./pictures/FScreenshots_147.png)

This would compute a 2. approximation of the metric TSP, but we can improve this to a $1.5$ approximation by:

1. Compute a minimum spanning tree $T$ of the graph $G$.
2. Find a minimum weight matching between odd degree vertices in the tree. The cost of this matching will be at most $OPT/2$ as any TSP tour shortcutted to the odd degree vertices can be divided in two matchings, and one of them must be less than $OPT/2$:

![image](./pictures/FScreenshots_148.png)

3. Find an Euler tour in the resulting graph. Such a tour must exist as all vertices now have even degree and the graph is connected. The length of the Euler tour will be at most $OPT+OPT/2=1.5*OPT$:

![image](./pictures/FScreenshots_149.png)

4. Convert it to a Hamiltonian cycle by removing repeated vertices. The length of the Hamiltonian cycle will be at most $1.5*OPT$.

This is the best approximation we can get for the TSP problem, and it is a $1.5$ approximation. The follwing is an example of the optimality of this approximation:

![image](./pictures/FScreenshots_150.png)

> _Q: Argue that the general TSP cannot be approximated within a constant factor unless P=NP.

We can argue for that by embedding a graph $H=(V,F)$ in the complete undirected graph $G$ with edge weights $w(u,v)=1$ if $(u,v)\in F$ otherwise set $w(u,v)=M$ for an abritrarily large $M$. The result of this would be that any TSP tour that does not correspond to a Hamiltonian cycle in H, must have weight at least $M+(n-1)$. 

Now let's suppose you COULD approximate TSP within a constant factor $c$. Then any approximate solution would distinguish between a valid Hamiltonian cycle with a cost of $n$ or a non-Hamiltonian cycle with a cost much greater than $cn$ due to the large $M$ value. This would then solve the Hamiltonian cycle problem exactly in polynomial time, which is NP-complete. Therefore, unless P=NP, TSP cannot be approximated within a constant factor.

---
> Q: Describe how to obtain a 2-approximation for the metric TSP. Highlight where you use the metric property.

1. Consider a minimum spanning tree on the TSP problem instance
2. Double all edges and construct an Euler tour, the length of the tour will be $2*OPT$, but remember that the minimum spanning tree will be less than the minimum TSP tour, since the tree will not contain the edge that goes back to the starting vertex:

![image](./pictures/FScreenshots_146.png)

3. Relax the Euler tour to a Hamiltonian cycle of the required vertices. The hamiltionian cycle will be no longer than twice the weight of the spanning tree:

![image](./pictures/FScreenshots_147.png)

This would compute a 2. approximation of the metric TSP, but we can improve this to a $1.5$ approximation by:

---
> Q: Describe how to obtain a (3/2)-approximation for the metric TSP.

1. Compute a minimum spanning tree $T$ of the graph $G$.
2. Find a minimum weight matching between odd degree vertices in the tree. The cost of this matching will be at most $OPT/2$ as any TSP tour shortcutted to the odd degree vertices can be divided in two matchings, and one of them must be less than $OPT/2$:

![image](./pictures/FScreenshots_148.png)

3. Find an Euler tour in the resulting graph. Such a tour must exist as all vertices now have even degree and the graph is connected. The length of the Euler tour will be at most $OPT+OPT/2=1.5*OPT$:

![image](./pictures/FScreenshots_149.png)

4. Convert it to a Hamiltonian cycle by removing repeated vertices. The length of the Hamiltonian cycle will be at most $1.5*OPT$.

This is the best approximation we can get for the TSP problem, and it is a $1.5$ approximation. The follwing is an example of the optimality of this approximation:

![image](./pictures/FScreenshots_150.png)

## Semidefinite Programming
> Q: What is a semidefinite program? How fast can we find a solution to a semidefinite program in n variables?

A semidefinite program (SDP) is an optimization problem where the goal is to minimize or maximize a linear function subject to linear constraints. It generalizes linear programming and quadratic programming. Generalized we can express a semidefinite program as:
$$
\begin{aligned}
\text{minimize} & \quad C \cdot M \\
\text{subject to} & \quad A_i \cdot M = b_i, \quad i=1,\dots,m \\
& \quad M \succeq 0
\end{aligned}
$$

Where:

- $M$ is a symmetric $n\times n$ matrix, called the decision or optimization variable.
- $C$ is an $n\times n$ matrix.
- $A_i$ are $n\times n$ matrices.
- $b_i$ are scalars.
- $M\succeq 0$ means that $M$ is positive semidefinite.
- $C\cdot M$ denotes the inner product $\text{tr}(C^T\cdot M)$.

A symmetric square matrix $M$ is positive semidefinite for all vectors $x\in \mathbb{R}^n$ if $x^T\cdot M\cdot x\geq 0$. This is a generalization of the concept of non-negativity to matrices.

If, and only if, $M$ is positive semidefinite, then there exists a matrix $P$ such that $M=P^T\cdot P$. This is known as the Cholesky factorization. If $P$ exists, then it can be found in polynomial time.

Less formally, we are solving an optimization problem, where the objective function is linear in the entries of a symmetric matrix $M$. The constraints to the problem require that $M$ is positive semidefinite, and there may then be additional linear constraints on $M$.

We can solve semidefinite programs using methods like the Ellipsoid method or the interior point method. Most algorithms consider some value $\epsilon>0$ and then solve the problem to within an additive error of $\epsilon$. Usually in polynomial time in the size of the input and $\log(1/\epsilon)$.

"Surprisingly, if we let the n vectors be unit vectors in n-dimensional Euclidean space, then there is a polynomial time algorithm!"

---
> Q: For a positive semidefinite matrix M, what is the name of the algorithm that computes a triangular matrix L so that LL^T=M? What is its running time?

A symmetric square matrix $M$ is positive semidefinite for all vectors $x\in \mathbb{R}^n$ if $x^T\cdot M\cdot x\geq 0$. This is a generalization of the concept of non-negativity to matrices.

If, and only if, $M$ is positive semidefinite, then there exists a matrix $P$ such that $M=P^T\cdot P$. This is known as the Cholesky factorization. If $P$ exists, then it can be found in polynomial time.

sing Cholesky decomposition, a real symmetric matrixcan be decomposed, in polynomial time, as $A = UAU^T$, where $A$ is a diagonal matrix whose diagonal entries are the eigenvalues of $A$. Now $A$ is positive semidefinite iff all the entries of $A$ are nonnegative, thus giving a polynomial time test for positive semidefiniteness. The decomposition $WW^T$ is not polynomial time computable because in general it may contain irrational entries. However, it can be approximated to any desired degree by approximating the square roots of the entries of $A$. In the rest of this chapter we will assume that we have an exact decomposition, since the inaccuracy resulting from an approximate decomposition can be absorbed into the approximation factor. This takes $O(n^3)$ time.

---
> Q: Name two combinatorial problems that can be approximated with the help of semidefinite programming.

**Max-Cut:**

Given a graph $G=(V,E)$, the goal is to partition the vertices into two sets to maximize the number of edges between the two sets. This is a classic NP-hard problem that can be approximated using semidefinite programming.

$$
\begin{aligned}
\text{maximise} & \quad \frac{1}{2}\sum_{ij\in E}(1-M_ij) \\
\text{subject to} & \quad M \text{ is positive semidefinite} \\
& \quad M_{ii}=1, \quad 1\leq i\leq n
\end{aligned}
$$

Algorithm:

- Find an optimal solution $M$ to the semidefinite program.
- Find the Cholesky factorization $M=LL^T$.
- The row vectors of $P$ are the vectors of the vertices
- Repeat several times:
    - Pick a random vector $r$ uniformly at random
    - Partition the vertex $i$ depending on $\text{sgn}(p_i^T\cdot r)$
    - Pick the partition $L,R$ that gets the highest cut
- Output $L,R$


**3-coloring:**

What is the least number of colors needed to color the vertices in a 3-colorable graph so that no two adjacent vertices have the same color?

There is a very long example in the slides for lecture 25.

---
> Q: How do you get from the vectors obtained from a solution to the semidefinite program to a solution to the combinatorial problem?

We essentially do some sort of rounding scheme, but it heavily depends on the algorithm. As in most linear programming problems we find a solution that is close to the optimal solution, but not necessarily an integer solution. We then need to round the solution to get an integer solution. This is done by using the vectors obtained from the solution to the semidefinite program.

In the Max-Cut algorithm from before the rounding scheme is the "repeat several times" part. Which is a rounding procedure. Goemans and Williamson simply choose a uniformly random hyperplane through the origin and divide the vertices according to which side of the hyperplane the corresponding vectors lie.  

The most important part of a round scheme is to preserve the quality of the SDP solution as much as possible. 


