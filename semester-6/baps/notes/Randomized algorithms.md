---
title: Randomized algorithms
tags: [ hello, world ]
date: 2023-06-09
---

# Randomized algorithms
## Correlated elements
Can map large images, documents, etc to digestable vectors which makes them easier to compare. Therefore similar things should stay similar and different things should stay different when the algorithm has run.

On bit vectors similarity is measured by how many bits are the same. So when given a list of vectors and a similarity, how do we find the pair with at least that similarity?

Of course we can loop them, but that's slooooooow.

### MinHash
MinHash is an algoritm for hashing bit vectors while retaining information about their similarity. In our version we hash a vector into a bucket, if there are multiple vectors in that bucket, then they collide. 

- Create a list of indexes simply increasing eg. [0, 1, 2, 3, 4, 5, 6, 7]
- Shuffle it (random.shuffle in Python)
- Iterate the index vector and use the index to look into the bit vector. The first time the hit is 1, that's the hash value.

The idea is that if two vectors are similar, they will have the same hash value. The probability of this is the Jaccard similarity of the two vectors. As in the probability that they hash together is proportional to similarity(x,y).

Problematically this can cause more collisions than we may want. The solution is simply to take a bucket that has many colissions in and hash them multiple times using that method, then only match those that all fit the multiple hash values. If there are no matches, simply try with a different hash.
