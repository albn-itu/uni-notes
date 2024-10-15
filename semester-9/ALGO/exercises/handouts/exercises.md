# Lecture 5
## Q1
> You flip an unbiased coin (heads are as likely as tails) 10 times. What is the probability that you get as many tails as heads? What is the probability that you get all heads? 

Denote the number of heads as $X$. Then $X \sim Bin(10, 0.5)$. We want to find $P(X = 5)$. We calculate this as follows:
$$
\begin{align*}
    P(X = k) &= \frac{(n \choose k)}{2^n} \\
    P(X = 5) &= \frac{(10 \choose 5)}{2^{10}} \\
    &= \frac{\frac{10!}{5!\cdot(10-5)!}}{2^10}\\
    &= \frac{252}{1024} = 0.25\\
    &= 25\%
\end{align*}
$$

Do the same for $P(X = 10)$:
$$
\begin{align*}
    P(X = 10) &= \frac{(10 \choose 10)}{2^{10}} \\
    &= \frac{\frac{10!}{10!\cdot(10-10)!}}{2^10}\\
    &= \frac{1}{1024} = 0.00098\\
    &= 0.098\%
\end{align*}
$$

## Q2
> You throw three ordinary 6-sided unbiased dice. What is the expected sum of the dice? What is the expected product of the dice? 

For the sum we can simply use the linearity of expectation, such that the expected value of one die is:
$$
\begin{align*}
    E(X) &= \sum_{i=1}^6 i \cdot P(X = i) \\
    &= (1 \cdot \frac{1}{6}) + (2 \cdot \frac{1}{6}) + (3 \cdot \frac{1}{6}) + (4 \cdot \frac{1}{6}) + (5 \cdot \frac{1}{6}) + (6 \cdot \frac{1}{6})
    &= \frac{7}{2} = 3.5
\end{align*}
$$

Then we can simply multiply this by 3 to get the expected sum of the dice:
$$
\begin{align*}
    E(X) &= 3 \cdot E(X) \\
    &= 3 \cdot 3.5 \\
    &= 10.5
\end{align*}
$$

We cannot use the same method for the product but can instead use the definition of expectation, where we sum over all possible values of the random variable. If we consider this for a moment, that means taking every possible die value, 3 times, and multiplying them together. This is a bit more complicated, but we can still do it:
$$
\begin{align*}
    E(X) &= \sum_{x\in \left\{1,2,3,4,5,6\right\}^3} \frac{1}{6^3} \prod_{i=1}^3 x_i \\
    \intertext{Move the terms around}
    &= \frac{1}{6^3} \prod_{i=1}^3\sum_{x_i=1}^6  x_i \\
    \intertext{Use the known sum of the die}
    &= \frac{1}{6^3} \prod{i=1}^3 21 \\
    &= \left(\frac{21}{6}\right)^3 \\
    &= \left(\frac{7}{2}\right)^3 = 42.86
\end{align*}
$$

## Q3
> Suppose you want to sample a random permutation of the first n positive integers uniformly (meaning that all of the n! permutations are equally likely to be the outcome). How can you use an unbiased coin to sample such a permutation. How many coin flips do you need? 
