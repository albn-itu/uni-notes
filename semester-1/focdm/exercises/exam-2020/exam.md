# Exam - 2020

### 1. - Correct

$S$ can complete it instantly

$P$ can too

$Q\and R$ proves that both $R$ and $Q$ are true, which is unclear with the $\or$

### 2. - Correct

The powerset of an empty set, will include the empty set, as a power set always includes the empty set.

### 3. - Correct

If we assume $a=4, b=7,m=3$

Here $a\mod m=1$ and $b\mod m=1$ proving $a\equiv b(mod\ m)$ but $(a+b)\mod m=2$ thereby disproving it

### 4. - Correct

Bijective

### 5. - Correct

A partial order is reflexive, antisymmetric, transitive. Meaning there will never be two edges in the opposite direction, it loops on every vertex and two edges imply the same.

Which is true for $R=\{(1,1),(1,4),(2,2),(2,4),(3,1),(3,2),(3,3),(3,4),(4,4)\}$ is a partial order on $S=\{1,2,3,4\}$

### 6. - Correct

One could simply check. But what we can observe is that the fibonacci sequence is the exact same formula, only with the added constraint that it starts with 0,1,1 (1,1) not 3,3. Which would mean that of course this is the fibonacci sequence times 3

### 7. - Correct

Let's observe this as the sequences

$[æ][ø][å][][][]$

$[][æ][ø][å][][]$

$[][][æ][ø][å][]$

$[][][][æ][ø][å]$

Which means that for each of these cases we have 3 letters to play with, so since the alphabet has 23 remaining letters it is:

$26\cdot 25\cdot 24=15600$

Which there, by our sequences before can be 3 versions of. Therefore:

$15600\cdot 4=62400$

### 8. - Correct

Let the event that a patient tests positive for covid be $A$

Then the event that a person actually has Covid be $B_1$  and let $B_2$ be the event that the person does not. The case that the person actually has the disease be 90% as that is 100% - the false negative rate of 10%. The case that person does not have the disease then is 1% therefore:

$P(B_1|A) = 0.90\%, P(B_2|A) = 0.01\%, P(B_1^c|A) = 0.10\%, P(B_2^c|A) = 0.99\%$

On top of that we know that 4% of the people coming are infected so $P(B_1)=0.04, P(B_2)=0.96$

Which means that when we apply bayes theorem we get 0.79 or 79%

### 9. - Correct

We can take the graph and split it into the two sets $\{a,c,e\}, \{b,d,f\}$ which have no internal connections making it a bipartite graph. A good way to test is to just take a point and keep switching sides.

### 10. - Correct

We split it up into the two elements first we have $(1\cup 0)*$ which would have to be some self looping with 1 or 0, and some way to end it. It has to have 10 in the middle, ending the first loop. Then there is the last one which is just 10 looping, the first choice $P=\{S\rightarrow A10B,A\rightarrow 0A,A\rightarrow 1A,A\rightarrow\lambda,B\rightarrow B01,B\rightarrow\lambda\}$

### 11. - Correct

![image-20210322221501227](C:\Users\alber\AppData\Roaming\Typora\typora-user-images\image-20210322221501227.png)

```proofweb
Require Import ProofWeb.

Parameter P R Q : D -> Prop.

Theorem exercise_2 : all x, (P(x)/\Q(x) -> not (R(x))) -> exi y, (P(y)/\R(y)) -> exi z, (Q(z) -> False).
Proof.

imp_i h1.
imp_i h2.
exi_e (exi y, (P(y)/\R(y))) a h3.
exact h2.
exi_i a.
imp_i h4.
neg_e (R(a)).
imp_e (P(a)/\Q(a)).
all_e (all x, (P(x)/\Q(x)-> not (R(x)))).
exact h1.
con_i.
con_e1 (R(a)).
exact h3.
exact h4.
con_e2 (P(a)).
exact h3.

Qed.
```

### 12. - Correct

So lets assume that $n$ is odd, by definition then $n=2k+1$ which must mean that $n^3 =(2k+1)^3$ let's simplify that:

$n^3 =(2k+1)^3=(2k)^3+3(2k)^2\cdot 1+3\cdot 2k\cdot 1^2+1^3=8k^3+12k^2+6k+1=(8k^2+12k+6)\cdot k+1$ therefore $n^3$ is odd. Which must mean that $n^3+13$ is odd by the simple fact that adding two odd numbers is an even number. Disproving our contradiction hypothesis, proving that $n$ is even.

### 13. - Correct

First let's prove the base case 0:
$$
\begin{align*}
\sum_{i=0}^a(i\cdot i!) &= (a+1)!-1\\
\sum_{i=0}^0(i\cdot i!) &= (0+1)!-1\\
(0\cdot 0!) &= 1-1\\
0 &= 0\\
\end{align*}
$$
Thereby proving the base case $P(0)$ now we define our hypothesis $P(k+1)$
$$
\begin{align*}
	\sum_{i=0}^{k+1}(i\cdot i!) &= ((k+1)+1)!-1\\ % Expand the (k+1) seperatly
	(k+1)!-1 + (k+1)\cdot (k+1)! &= (k+2)!-1\\ % Substitute hypothesis
    (k+2)(k+1)!-1 &= (k+2)!-1\\ % Simplify
    (k+2)!-1 &= (k+2)!-1\\ % Simplify
\end{align*}
$$

### 14. - Correct 	