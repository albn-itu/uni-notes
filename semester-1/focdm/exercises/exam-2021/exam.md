# Re-exam - 2020

### Question 11 - Predicate logics

> Construct a valid judgment (derivation) for the following predicate: $\exists \ x\ (P(x)) \to \exists \ y\ \exists \ z\ (P(y) \vee P(z))$ 

Proved in the form of a prooftree, seen in the image below:

![img](https://lh3.googleusercontent.com/-072Shu4htLpmp_1AMspYJts3FA7c_jepTaOsTDBRK0fBfcaBsfNPSRqdqukcQBVazm7t5ab6lrGUJDJ9KGoZu4d1u4nZKPJCB96B9LJhB1VBKcjcYVRnewmwkExiuIv3s_g4K8pmwM9yZrlfN3wpz9ZOMT_UErDFmdnw6gKHcZa4PxDySCmsJO-RuawoXcoFN6LqSrSzQ3mcnvxJAdwbEOvJzxtM6Os_ZBK4VreUOongzbNZhZR2R2Hef1HC7b_eQ0HWYPmQozVpZieqiD4XueD-XzfqtgomzL7REhCfNR3aN1B-FGTfrkgN_T1G2YM_M4X_ASPe-AlJCPaNDXNqc9SOS7pLaTlTbF6ChQy8UDA3tt4y_9_6cCYdKHjjNJ2ZnM9tQkt_GnTx55XHpAqmxy0tUVIeNWMhGdYaGD4rv_RLYBQh-vQy34dkayrdGBPsLIHa7bvm7q5sZ0db6EF_5-XfcLl34CH5e6-T_Ax2D_ZfleL3zmRx1ozB1ASqCBNPHSgJsMJT7nzPllNGKQTvZJkEbby-MPelgl3fmSoKX_Kz_3hIqwPbWa7beWDtPz-A7W-CkO-t6mt6eYXImqHvd8efLpNkWuxql19D62ZZAphzPbxHIPdHazJwccY-1kNHmvkE7edYOSVnLYwRyvAW0TQ_1Qb6HA3zRI6sKiTL02egjlsmgkivnK8LEVNZ6t2B76cnhnaHh2f1Pf544-6daEHiw=w2424-h1366-no?authuser=0)

### Question 11 - Direct proof

> Let $n \in \mathbb N$. Assume that $n$ is odd. Prove that there exists a $Q\in \mathbb{N}$ such that $n^2 = 4 \cdot q + 1$

By definition of odd $n=2k+1$. Therefore 
$$
\begin{align*}
 n^2 &= (2k+1)^2\\
  n^2 &= (2k^2)+2 \cdot 2k\cdot 1 + 1^2\\
  n^2 &= (2k)^2+4k + 1\\
  n^2 &= 4k^2+4k + 1\\
\end{align*}
$$
Substitute and isolate $Q$
$$
\begin{align*}
  4 \cdot q + 1 &= 4k^2+4k + 1\\
  \frac{4 \cdot q}{4} &= \frac{4k^2+4k}{4}\\
  q &= \frac{4k(k+1)}{4}\\
  q &= k(k+1)\\
\end{align*}
$$
Thereby showing the $q$ for some value $k$ 

$n^2 = 4 \cdot (k(k+1)) + 1$



### Question 11 - Proof by induction

>Let $n \in \mathbb Z^+$. Prove by induction that $\sum _{i = 1}^n i^3 = \left ({n(n+1)\over 2}\right )^2$

First we must show that $P(1)$ is true:
$$
\begin{align*}
	\sum _{i = 1}^1 i^3 &= \left ({1(1+1)\over 2}\right )^2\\
	1^3 &= \left ({1(1+1)\over 2}\right )^2\\
	1 &= \left ({2\over 2}\right )^2\\
	1 &= 1\\
\end{align*}
$$

Thereby proving $P(1)$, then we establish our inductive hypothesis $P(k)$:
$$
\sum _{i = 1}^k i^3 = \left (\frac{k(k+1)}{2}\right )^2
$$
Then we must prove that $P(k+1)$ is true if $P(k)$ is true for every integer $1 \leq k$:
$$
\begin{align*}
	\sum _{i = 1}^{k+1} i^3 &= \left (\frac{(k+1)(k+2)}{2}\right )^2\\
	\sum _{i = 1}^k i^3 + (k+1)^3 &=\frac{(k+1)^2(k+2)^2}{4}\\
\end{align*}
$$

Then we substitute our inductive hypothesis:
$$
\begin{align*}
	\sum _{i = 1}^k i^3 &+ (k+1)^3\\
		&= \left (\frac{k(k+1)}{2}\right )^2 + (k+1)^3\\
		&= \frac{k^2(k+1)^2}{4} + (k+1)^3\\
		&= \frac{(k+1)^2(k+2)^2}{4}\ \ \ \ \ \ \text{Factor out the common factors}\\
\end{align*}
$$
Thereby proving the statement





### Question 11  - Formal languages

>Construct a phrase-structure grammar that recognizes the language $\{0^n(10)^{n+1} \mid n \in \mathbb N\}$. Is your grammar regular, context-free, context sensitive or recursively enumerable? explain why.

We construct the Phrase structure grammar $G=\{V,T,S,P\}$:
$$
\begin{align*}
	V &= \{S,A,B,1,0\}\\
	T &= \{0\}\\
    P &= \{S\rightarrow ASB, S\rightarrow AB10, A\rightarrow 10, B\rightarrow 0\}
\end{align*}
$$
By constructing our grammar this way we ensure that A and B occur the same amount of times (in the main "loop"), and are constantly constructed around $S$. We then end the grammar with $AB10$ which removes the $S$ and thereby ensures that no more occurences can happen, and end's the grammar with 10 thereby ensuring $10$ occurs $n+1$ times. If one was so inclined the last step could be $ABB$, but i thought the other method was clearer in meaning. 

This grammar is context sensitive as it fullfils the production rule $\alpha A\beta \rightarrow  \alpha\gamma\beta$. We constantly build around the non terminal S, by adding non terminals and terminals on the left and right side of it, until we replace it with a terminal. Thereby making it context sensitive





















