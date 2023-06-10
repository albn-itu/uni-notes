---
title: Algoritms on arrays
tags: [ hello, world ]
date: 2023-06-09
---

# Algorithms on arrays
## Range queries
A range calculates a value based on a subarray of the array. Such a query can be the sum, min and max. Easy in linear time.

```python
def range_sum(arr, a, b):
    sum = 0
    for i in range(a, b+1):
        sum += arr[i]
    return sum
```

### Static arrays
The following sections assume the array is static

#### Prefix sums
A prefix sum is the sum of all elements up to a certain index. This can be calculated in linear time.

```python
def prefix_sum(arr):
    prefix = [0] * len(arr)
    prefix[0] = arr[0]
    for i in range(1, len(arr)):
        prefix[i] = prefix[i-1] + arr[i]
    return prefix
```

Retrieving the sum from 0 then is easy, it can be done in O(1) time by simply retrieving the element at that point. Calculating a range query is also pretty simple by calculating sum(0,b) - sum(0, a-1) since the b'th element contains the sum of everything up to that point, so we just remove the extra from outside the query.

```python
def sum(prefix, a, b):
    if a == 0:
        return prefix[b]
    return prefix[b] - prefix[a-1]
```

#### Minimum queries
A minimum query can be more difficult to answer than sum queries, but there is a O(n log n) processing step that can be done. The solution is to calculate all values of possible range queries where b-a+1 (the length of the range) is a power of 2. I have yet to get this code to work.

### Dynamic arrays
#### Binary indexed tree (Fenwick tree)
A binary indexed tree can be used as a dynamic variant of the prefix sum. It supports updating and processing a range sum in O(log n). Usually represented as an array despite it's name. Stored as `tree[k] = sum(k-p(k)+1, k)` each position k contains the sum of values in a range of length p(k) and which ends at position k. So `p(6)=2` means `tree[6]=sum(5,6)`. Since it ends in k and contains 2 values.

The values of array
![](../../../../Zettelkasten/img/pasted_img_20230609120137.png)
are calculated as
![](../../../../Zettelkasten/img/pasted_img_20230609120117.png)
We can then calculate the sum of a range by adding the values of the tree together. The sum of a range is the sum of the values of the tree at the end of the range. Since ever 2nd contains values up to that point we can calculate with them and the individual one.
![](../../../../Zettelkasten/img/pasted_img_20230609120315.png)

```python
# 1 indexed array
tree = [0] * (len(arr)+1)

def create_tree(arr):
    for i in range(1, len(arr)+1):
        tree[i] += arr[i-1]
        # Calculate what others this value must be part of. there will always only be one closest to it
        k = i + (i & -i)
        if k < len(arr)+1:
            tree[k] += tree[i]

def sum(k):
    sum = 0
    # Go by k steps to find the other making up values
    while k >= 1:
        sum += tree[k]
        k -= k & -k
    return sum

def add(k, x):
    # Go up by k steps to find the other making up values
    while k <= len(tree):
        tree[k] += x
        k += k & -k
```

#### Segment tree
A segment tree supports two operations, processing a range query and updating a value. The queries can be sum and min and max while all being in O(log n) time. The primary difference from the binary indexed tree is that it supports more than just the sum query, therefore being much more general. It does though require more memory and is more complex.

The tree is built such that the bottom most elements (the leaves) are the values of the array. The array must be zero indexed and be a power of 2 in size, or more elements has to be appended to it. The nodes themselves contain information needed for processing the range queries

The array
![](../../../../Zettelkasten/img/pasted_img_20230609122615.png)
is represented as
![](../../../../Zettelkasten/img/pasted_img_20230609122628.png)

Each node corresponds to an array range whose size is a power of 2. In the example the tree is used for sum queries. The tree is built on the principle that any range can be divided into O(log n) ranges. When calculating a sum at most 2 nodes in the tree are required. And when an update is required it's the simplest path to the leaf that is updated, which always consists of O(log n) nodes. 

The tree is stored such that each level is stored after each other. Hence tree[1] is the root, tree[2] and tree[3] are it's children etc.

```python
tree = [0] * (2 * len(arr) + 1) # 1 indexed array

def create_tree(arr):
    # The leaves are the values of the array, and are the last elements, they are stored at tree[len(arr):]
    for i in range(len(arr)):
        tree[len(arr) + i] = arr[i]
    # The rest of the tree is built from the bottom up
    for i in range(len(arr)-1, 0, -1):
        # The value of a node is the sum of it's children
        # The rule essentially is that the left child is 2*i and the right child is 2*i+1
        tree[i] = tree[2*i] + tree[2*i+1]

def sum(a,b):
    a += len(arr)
    b += len(arr)
    sum = 0
    
    # Maintain a range [a+n, b+n] where n is the size of array
    # Then at each step, move one level higher in the tree and add the values of the nodes that are not in the higher range
    while a <= b:
        if a % 2 == 1:
            sum += tree[a]
            a += 1
        if b % 2 == 0:
            sum += tree[b]
            b -= 1
        
        a //= 2
        b //= 2
    return sum

def add(k, x):
    # Start at the leaf
    k += len(arr)
    tree[k] += x
    # Move up the tree, updating the values of the nodes
    while k >= 1:
        k //= 2
        tree[k] = tree[2*k] + tree[2*k+1]
```

##### Top to bottom
Alternative to the bottom up standard search in O(log n) time

```python
# Searches in O(log n) time
def sum_top_btm(a,b):
    def top_btm(k, lo, hi):
        # The range is completely outside the currently searched range
        if b < lo or a > hi:
            return 0
        # The range is completely inside the currently searched range
        if a <= lo and b >= hi:
            return tree[k]
        # The range is partially inside the currently searched range
        mid = (lo + hi) // 2
        # Search in both children
        return top_btm(2*k, lo, mid) + top_btm(2*k+1, mid+1, hi)
    return top_btm(1, 0, len(arr)-1)
```

##### Lazy propagation
The idea here is to not update the tree immediately, but instead store the values in the nearest node that contains all the elements that need to update with that value. When you then do the top down range query you update the nodes that you visit, if you have to go further down the tree.

![](../../../../Zettelkasten/img/pasted_img_20230609144753.png)

##### Dynamic segment trees
Store everything as a struct or class with references to neighbors. Can be more complex or memory ineffecient, but allows dynamically adding more leaves. Can be useful when creating sparse segment trees since you technically don't need to create everything. This is only necessary if you don't know how many nodes you are going to need. This also does not support index compression.

![](../../../../Zettelkasten/img/pasted_img_20230609145042.png)

## Square root algorithms
A square root algorithm is an algorithm with O(sqrt(n)) complexity. These are usually not as optimal as other solutions, but can be easier to implement, and are quite adequate.

For something lige range queries we simply create a few blocks of size sqrt(n) which contain the sum of it's members. Updating these are O(1) complexity and the sum operation is O(sqrt(n)) time since we just sum the blocks and individual elements that fall outside them.

```python
from math import sqrt, ceil, floor
blocks = [0] * int(len(arr) // sqrt(len(arr)) + 1)

def create_blocks(arr):
    for i in range(len(arr)):
        blocks[int(i // sqrt(len(arr)))] += arr[i]

def sum(a,b):
    block_size = int(sqrt(len(arr)))
    sum = 0
    # Sum the blocks
    for i in range(ceil(a / block_size), floor(b / block_size)):
        sum += blocks[i]
    # Sum the individual elements
    for i in range(a, ceil(a / block_size) * block_size):
        sum += arr[i]
    for i in range(floor(b / block_size) * block_size, b):
        print(i)
        sum += arr[i]
    return sum

def add(k, x):
    blocks[floor(k // sqrt(len(arr)))] += x
    arr[k] += x
```

### Integer partitioning
An observation of integers is that an integer n which is represented as a sum of positive integers always contains at most O(sqrt n) distinct numbers. We can reason this by choosing as small numbers as possible 1,2,...,k the sum then is `(k(k+1))/2`. Thus the max amount of distinct numbers is k=O(sqrt n).

We can solve knapsack using this observation, decreasing time from O(n^2) to O(n sqrt n).

