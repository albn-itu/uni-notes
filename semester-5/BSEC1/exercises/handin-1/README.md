---
title: Mandatory hand-in 1
author: Albert Rise Nielsen (albn@itu.dk)
date: 02-10-2022
---

# Mandatory hand-in 1
## Preface
The code in this assignment will be written in Python, version 3.10.4. Every code snippet assume the snippets before it exist in the scope. The best way to run the code is the full program at the end of the document.

There is a helper function that will be used in the code snippets. It's purpose is to represent $a^b\mod c$ in a way that avoids integer overflow. While that is not necessarily a problem in Python, this is also ultimately faster with large numbers, compared to computing the power and then applying modulo, while being much more memory efficient.
```python
def mod_pow(base, exp, mod):
    res = 1
    while(exp > 0):
        if (exp % 2 == 1):
            res = (res * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return res
```
The method of modular exponentation shown here is the right-to-left binary method [1].

**The numbers shown in this document should never be used in real world applications. They are artificially small to make examples, and bruteforcing feasible.**

The information given in the assignment: 
- Shared base $g=666$, will be denoted as $\alpha$ for the rest of the document
- Shared prime $p=6661$
- Public key $PK=2227$, will be denoted as $k$ for the rest of the document

## ElGamal
This assignment revolves around the ElGamal public-key encryption scheme.

ElGamal, in this case, uses the multiplicative group $\mathbb{Z}^*_q$ of integers modulo $p$.

### Key generation
The algorithm for key generation in ElGamal is as follows:
- Generate a large random prime $p$ and a generator $\alpha$ of the group
- Select a random integer $a$, $1\leq a\leq p-2$
- Compute $k=\alpha^a\mod p$
- $A$'s public key is $(p, \alpha, k)$
  - Given to us as $(p=6661, \alpha=666, k=2227)$
- $A$'s private key is $a$

### Encryption
For a party $B$ to encrypt a message $m$ for $A$, the algorithm is:
- Obtain $A$'s public key $(p, \alpha, k)$
- Transform $m$ to an integer representation within the range ${0,1,\dots,p-1}$
- Select a random integer $r,1\leq r\leq p-2$
- Compute $c_1=\alpha^r \mod p$
- Compute $c_2=m\cdot k^r\mod p$
- Communicate the cipher text $c=(c_1, c_2)$ to $A$

### Decryption
For a party $A$ to decrypt a message $m$ from $B$, encrypted with $A$'s public key $(p, \alpha, k)$, compute:
$$
  m=\frac{c_2}{((\alpha^r)\mod p)^a\mod p}=\frac{c_2}{c_1^a\mod p}
$$ 

#### Proof
Proof decryption works, take the decryption algorithm:
$$
  \frac{c_2}{((\alpha^r)\mod p)^a\mod p}
$$

Replace variables and eliminate:
$$
  \frac{m\cdot k^r\mod p}{((\alpha^r)\mod p)^a\mod p}=\frac{m\sout{\cdot (\alpha^a\mod p)^r\mod p}}{\sout{((\alpha^r)\mod p)^a\mod p}} =m
$$

## 1
To send the message we apply the algorithm above:
- $A$'s public key: $(p=6661, \alpha=666, k=2227)$
- $m$ is an integer, assumed to be sent as an integer: $m=2000$
- Select a random integer: $r=22$
- Compute $c_1=\alpha^r \mod p=666^{22}\mod 6661 = 2422$
- Compute $c_2=m\cdot k^r\mod p=2000 \cdot (2227^{22}\mod 6661)=6288000$
- The cipher text then is: $c=(c_1=2422, c_2=6288000)$


### Code
The code for the algoritm is as so:
```python
from random import randint

alpha = 666
p = 6661
k = 2227 # mod_pow(alpha, x, p)

def encrypt(m):
    r = randint(1, p-2) # Assume r=22 for these results
    c1 = mod_pow(alpha, r, p)
    c2 = m * mod_pow(k, r, p)

    return (c1, c2)

c = encrypt(2000)
print(c) # (2422, 6288000)
```

## 2
### Private key
Bob's private key can be found by simply bruteforcing it. The numbers are so small that the ineffeciency of bruteforce is neglible. The target will be the public key as we know it, and all the other elements necessary to compute it. Those being the base and prime number. The code for bruteforcing it is as so:

#### Code
The code for bruteforcing:
```python
def get_a():
    # Bruteforce
    for i in range(1, p-1): # Range is non inclusive, so instead of p-2 it's p-1 
        # If the calculation of the public key matches, we assume that must be the private key
        if mod_pow(alpha, i, p) == k:
            return i

a = get_a()
print(a) # 66
```

Running the method informs us the private key is $a=66$

### Decryption
Compute the decryption algorithm above:
$$
  m=\frac{c_2}{c_1^a\mod p}=\frac{6288000}{2422^{66}\mod 6661}=2000
$$

#### Code
The code for the algoritm is:
```python
def decrypt(c1, c2, a):
    m = c2 / mod_pow(c1, a, p)
    # Due to the fraction python assumes it to be a decimal, just remove the .0
    return round(m)

decrypted = decrypt(c[0], c[1], a)
print(decrypted) # 2000
```

## 3
Assuming the decryption algorithm above. If we were to multiply $c_2$ by some integer $x$, we would get:
$$
\frac{c_2\cdot x}{c_1^a\mod p}
$$

Replace and eliminate:
$$
  \frac{m\cdot k^r\mod p\cdot a}{((\alpha^r)\mod p)^a\mod p}=\frac{m\cdot (\alpha^a\mod p)^r\mod p\cdot a}{((\alpha^r)\mod p)^a\mod p} =m\cdot a
$$

In practice:
$$
  \frac{c_2\cdot x}{c_1^a\mod p}=\frac{6288000\cdot 3}{2422^{66}\mod 6661}=\frac{18864000}{3144}=6000
$$

### Code
The code for modifying the message:
```python
def modify(c2, x):
    return c2 * x

modified = modify(c[1], 3)
print(modified) # 18864000
print(decrypt(c[0], modified, a)) # 6000
```

# Sources
[1] Alfred J. Menezes, Paul C. van Oorschot, and Scott A. Vanstone. *Handbook of applied cryptography*. 1st ed. Crc Press, 1996. *Ch. 14, page 614, algorithm 14.76*

# Appendix
## The full program
The full code of the program. The structure has been slightly altered from the snippets, but the content is the same.

```python
from random import randint

# util method
def mod_pow(base, exp, mod):
    res = 1
    while(exp > 0):
        if (exp % 2 == 1):
            res = (res * base) % mod
        exp = exp >> 1
        base = (base * base) % mod
    return res

alpha = 666
p = 6661
k = 2227 # mod_pow(alpha, x, p)

def encrypt(m):
    r = randint(1, p-2)
    c1 = mod_pow(alpha, r, p)
    c2 = m * mod_pow(k, r, p)

    return (c1, c2)

def get_a():
    # Bruteforce
    for i in range(1, p-1): # Range is non inclusive, so instead of p-2 it's p-1 
        # If the calculation of the public key matches, we assume that must be the private key
        if mod_pow(alpha, i, p) == k:
            return i

def decrypt(c1, c2, a):
    m = c2 / mod_pow(c1, a, p)
    # Due to the fraction python assumes it to be a decimal, just remove the .0
    return round(m)

def modify(c2, x):
    return c2 * x

if __name__ == '__main__':
    c = encrypt(2000)
    print(c)

    a = get_a()
    print(a)

    decrypted = decrypt(c[0], c[1], a)
    print(decrypted)

    modified = modify(c[1], 3)
    print(modified)
    print(decrypt(c[0], modified, a))
```
