---
title: String algorithms
tags: [ hello, world ]
date: 2023-06-09
---

See also: [[OtherNote]]

# String algorithms
## Terminology
- **Substring**: A sequence of consecutive characters in a string.
- **Subsequence**: A sequence of characters in a string, not necessarily consecutive, but in the same order as they appear in the string.
- **Prefix**: A substring that starts at the beginning of a string.
- **Suffix**: A substring that ends at the end of a string.
- **Rotation**: A string formed by moving the characters of a string one at a time from the beginning to the end.
- **Period**: A prefix of a string that can be repeated to form the string. The last period may not be complete.
- **Border**: A prefix that is also a suffix.
- **Lexicographical order**: The order in which words are listed in a dictionary. Essentially alphabetical order.

## Tries
A tree data structure that stores strings. Each string is a chain that starts at the root. If 2 strings have a common prefix, they follow the same start chain in the tree. Each node stores whether or not a string ends there. The tree allows for O(n) lookups where n is the length of the string. Same with addition.

## String hashing
String hashing allows for fast checking if strings are equal by calculating a hash for a string that can be compared. There are many methods, one is polynomial hashing where the hash value is 

$$
h(s) = \sum_{i=0}^{n-1} s[i] \cdot A^{n-1} \mod B
$$

where $s$ is the string, $n$ is the length of the string and $A$ and $B$ are chosen constants.

### Preprocessing
If we want to check the equality of many strings, that are prefixes to one we have stored, we can preprocess the string by creating an array of $k$ size that contains the hashvalue up to that point, a prefix sum array essentially. Calculate using:

$$
h[0] = s[0] \\
h[k] = h[k-1] \cdot A + s[k] \mod B
$$

aditionally calculate an array $p$ where $p[k] = A^k \mod B$. 

$$
p[0] = 1 \\
p[k] = p[k-1] \cdot A \mod B
$$

then the hash of a substring $s[l..r]$ is

$$
h[l..r] = h[r] - h[l-1] \cdot p[r-l+1] \mod B
$$

This is an O(n) construction but allows O(1) lookups.

### Collisions
When using hash values there is a guarantee that if 2 values are different, the strings definetly are different, but if they are equal, they are only probably equal. There is always a possibility that 2 hash values are the same, but if big enough constants are chosen that risk is very small.

There are 3 different scenarios:
- String $x$ is compared with string $y$, the probability of a collision is $1/B$, where $B$ is  the constant
- String $x$ is compared with string $y_1, y_2, ...., y_n$, the probability of a collision is $1-(1-1/B)^n$, where $B$ is  the constant
- All pairs of strings $x_1, x_2,....,x_n$ are compared, the probability of a collision is $1-(B\cdot(B-1)\cdot(B-2)\cdot\cdot\cdot(B-n+1))/(B^n)$, where $B$ is  the constant

The 2 first scenarios have an almost 0 probability of a collision, but the last one has a much higher probability, in some cases guaranteed with a small enough B. To fix this one can alternate constants, making the probability much smaller. This is essentially the birthday paradox. 




