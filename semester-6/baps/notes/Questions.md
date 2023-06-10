---
title: Questions
tags: [ hello, world ]
date: 2023-06-06
---

See also: [[OtherNote]]

# Questions
## Problem solving techniques

- Describe 2 techniques to enumerate all subsets of the set $\{1, ..., n\}$.
  - Recursion
  - Iterative Bit sequence
- How do you solve [Geppetto](https://itu.kattis.com/problems/geppetto) using complete search?
  - See gepetto.py. Essentially just check on each loop if the new element has a pair, and if that pair is already in the list, if it is, ignore it and search without it.
- How do you solve the `n x n`-queens problem using backtracking?
  - Create 3 arrays, one of columns, one of diagonals, and one of anti-diagonals. Then, for each row, check if the column, diagonal, and anti-diagonal are free. If they are, place a queen there, and move on to the next row. If they are not, move on to the next column. If there are no columns left, backtrack to the previous row and move on to the next column.
- How does the general outline of a greedy algorithm look like?
  - Read input
  - Sort input by some criteria
  - Iterate the sorted input
    - Add the element to the solution if it is valid
    - Ignore the element if it is not
  - Return the solution
- Describe the greedy algorithm for the `coin exchange problem`. What is its running time? Describe the central step in the correctness argument ("It's never wrong to take the largest coin that is at most as large as the current value")
  - Sort the coins
  - Pick the biggest coin that places you at or below the target value
  - Repeat until you reach the target value
  - Return the number of coins used
  - The central step is that if you have a coin that is larger than the target value, you can always replace it with a smaller coin and get a better solution.
  - Running time is `O(n log n)` for sorting, and `O(n)` for the actual algorithm.
- Describe the greedy algorithm for `Task Scheduling`. What is its running time?
  - Sort the elements by their duration
  - Pick the element with the smallest duration
  - By doing this you push other tasks by a minimal amount every time

## Dynamic programming
- Explain: How do you find the `n-th Fibonacci number` using dynamic programming? How does memoization work in this case?
  - Create an array of the first two fibonacci numbers
  - When asked to get the n-th fibonacci number, check if it is in the array
    - If it is, return it
    - Else calculate it, and all the numbers up to it, and save them in the array
- Why does the greedy algorithm not work for the [Exact Change](https://open.kattis.com/problems/exactchange2) problem?
  - Because the first solution would be 1400+500 which would bring you to 1900 instead of 1500 which is desired.
  - We have to consider more solutions to the problem to get the optimal solution.
- How would you solve the problem [Knapsack](https://open.kattis.com/problems/knapsack) using Dynamic programming?
  - Create an array of size n and m where n is the max weight and m is the number of items
  - Iterate over the items
    - Iterate over the weights
      - If the item fits in the weight, check if the value of the item + the value of the remaining weight is greater than the value of the current weight
        - If it is, set the value of the current weight to the value of the item + the value of the remaining weight
- Describe: What is the difference between an iterative and a recursive implementation of a DP algorithm?
  - Iterative can be faster, use less memory and not run into max recursion depth errors.
  - A recusrive solution is usually easier to understand though, but also requires more checking of the input, to check limits
  - In some languages it can be annoying to work with a recursive method as you can't declare global variables, and you have to pass the memoization array around.

## Graph algorithms

- Describe different data structures to store a graph. What are the pros and cons of each data structure?
  - Adjacency list, simple to implement, but slow to check if two nodes are connected, can be nice on memory
  - Adjacency matrix, simple, tough on memory
  - Edge list, simple, but slow to check if two nodes are connected
  - Fancy stuff with hashmaps and sets, can be fast, but tougher to implement
- Given an undirected/directed graph, carry out `DFS` from a starting node.
  - Using the example on the slides 0-1-4-5-3-5-6-7-10
- Carry out `BFS` on a given directed/undirected graph from a starting node.
  - Using the example on the slides 
- What is the running time of `DFS` and `BFS`?
  - `O(|V| + |E|)`
- Define: What is a topological sorting of a directed graph? How do you find one using `DFS`?
  - A topological sorting is a sorting of the nodes in a graph such that if there is an edge from `u` to `v`, then `u` comes before `v` in the sorting. In other words, every node appears before any node it points to.
  - Start from a node and do DFS, when you are done, add all the nodes you visited to the topological sorting in reverse order. If there are unvisited nodes, start from one, then add those in reverse order. The reversed list is the topological sorting.
- Describe a kattis problem that can be solved by computing a topological sort.
  - Ours :/
  - Build dependencies?

## Network flow

- Define: What is a flow in a graph? What is the value of a flow? What is the maximum flow?
  - Flow is an amount of something that goes through a capacity. An edge can have a capacity of how much flow can go through it.
  - A flow value is the amount it takes from the capacity
  - Maximum flow is the largest possible amount of flow from one edge to another
- Define: What is a cut in a graph? How is the value of the cut defined? What is a minimum cut?
  - A cut is a removal of some set of edges that blocks flow from one node to another.
  - The value of the cut is the sum of the edges it removes
  - A minimum cut, is the minimum sum of the edges removed to block flow from one node to another. It has the same value as max flow.
- Given a directed, weighted graph and a pair of vertices `(s,t)`, how is the graph augmented for running a flow algorithm? (edges in opposite directions are added)
  - You add edges in the opposite direction of zero capacity. These can later be used to cancel flow.
- Given a flow graph and some flow on edges, carry out one step in the algorithm: (1) `Ford-Fulkerson`, (2) `Capacity Scaling`, (3) `Edmonds-Karp`.
  - Ford-Fulkerson would create a residual graph. But it's essentially finding an augmenting path first then setting the values.
  - Capacity scaling would sum all the edges then find a path with that threshold, then do it again with half, etc.
  - Edmonds-Karp would be the same as Ford-Fulkerson but with a BFS
- What is the relation between the maximum flow value and the size of a minimum cut?
  - They have the same value, since the maximum flow from one node to another is the minimum sie of the cut.
- Given a maxflow, find a minimum cut.
  - Find all edges from one set of nodes to another that has all it's capacity used, and which summed give the maxflow.
- What is the running time for the different flow algorithms seen in class?
  - Edmonds-Karp is O(VE^2), because you visit most edges at least twice, but each time an edge is satisfied, the length of the paths are limited by V.
- How do you solve a matching problem in a given undirected graph using a flow algorithm?
  - Identify the bipartite graph
  - Create a source connected to one set of nodes
  - Create a sink connected to the other set of nodes
  - Run maxflow
- Describe: How do you solve the [King of the North](https://open.kattis.com/problems/kingofthenorth) problem?

## Geometric algorithms

- Define: Given a set of points in the plane, what is their convex hull?
  - A convex hull is the minimum sorrounding line around the points
- Describe the sweepline algorithm to find a convex hull.
  - Get the left most and rightmost points. A line can be constructed between these which will separate the top and bottom hull
  - Sort points by x coordinate, then by y coordinate 
  - For the top iterate every point and add it to the hull line, if the last line segment turns left, pop points from before it until it no longer doesn't. Do so until you hit the end point.
  - Do the same for the bottom hull, going from the end to the start
  - Concat the lists, emitting the last and first from the lists
- What is the running time of the algorithm? Why?
  - O(n log n). n because you have to iterate every point, and n log n comes from the sorting algorithm. The result then is O(n+n log n), or just O(n log n)
- In the sweep line algorithm, it is important to find out if a line turns "left/right". How do you do this algorithmically?
  - The cross product between the new line and the old. If it's positive, negative if right, and straight if zero
- Given a polygon defined by a sequence of points, how do you compute its area?
  - You can use the method where you calculate the area between a trapezoid from each side to the y = 0 line.
- How do you solve [witchdance](https://open.kattis.com/problems/witchdance)?

## Interval queries

In the following, sparse table refers to the "square root" data structure.
- Given an array of integers, e.g., `[2, 8, 12, 1, 23, 56, 3, 10]`, and for the operations `min` or `sum`, (i) build a sparse table with two blocks and (ii) build a segment tree. Carry out a query for two positions, e.g., `(3, 5)` in the respective data structures. Update the value of an element and carry out the query again.
  - See book
- Given an array of integers build a Fenwick tree from it. What is the meaning of the operation `i & -i`? Which operations are supported by the Fenwick tree? Show how to compute the `sum` of an interval. Why does it make sense that the array is 1-indexed?
  - It makes sense to have it 1 indexed because it makes it far easier to calculate with 2's complement
  - The operation `i & -i` is the least significant bit of i.
- For all three data structures (Sparse Table, Segment Tree, Fenwick Tree), how long does it take to build the array representation for a given array? How long does a query take? How long does a single update take? 
    - Sparse table: O(sqrt n) to build, O(sqrt n) to query and O(1) to update
    - Segment tree: O(n) to build and O(log n) to query and update
    - Fenwick tree: O(n) to build and O(log n) to query and update
- How do you solve [_Supercomputer_](https://itu.kattis.com/problems/supercomputer) and [_Frosh Week_](https://itu.kattis.com/problems/froshweek) using a Segment or Fenwick tree?

## String algorithms

- Describe: How do you solve [Bing](https://itu.kattis.com/problems/bing) using a trie. Which augmentations do you need to apply to a standard trie? 
  - Add a value to the node that can be incremented each time it is visited
- Describe: How does string hashing compute the hash code of a string. What is the role of `a` and `p`? 
  - `a` and `p` are constants used in calculating the hash, which is the sum of the characters multiplied by `a` to the power of the index of the character, modulo `p`
- Let's say `a` is 11 and `p` is 37. How does the polynomial for the string "APS" look like? (no evaluation, not important to get the ordinal representations of the characters right.)
  - `(s[0]*11^2 + s[1]*11^1 + s[2]*11^0) mod 37`
- What is the probability that two _different_ strings of length `m` hash to the same integer? 
  - `1/p`
- What is an efficient way to compute the coefficients `a^{i}` for `i` in `{0, ..., m - 1}`?
  - `p[k] = p[k-1] * a mod m`
- Discuss: How can dvaput be solved using string hashing?
  - Calculate a hash for every substring of every length, start from longest to shortest. If it appears in the set you've found it.

## Randomized algorithms

- Given a binary string $x$ of length $d$, how do you choose a MinHash hash function $h$ and what is the hash value $h(x)$?
  - Choose a random permutation of the set of all possible characters, then find the first character in the string that is in the permutation. The hash value is the index of that character in the permutation.
- Given two strings $x$ and $y$ with Jaccard similarity $J(x,y)$, what is the probability that $x$ and $y$ hash to the same value?
  - `J(x,y)`
- How do you build a data structure to find a correlated pair using MinHash?
  - Create a hashmap of the hash values of the strings, and the strings themselves. If a hash value is already in the map, you've found a correlated pair.
