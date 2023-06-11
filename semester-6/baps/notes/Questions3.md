---
title: Questions3
tags: [ hello, world ]
date: 2023-06-11
---

See also: [[OtherNote]]

# Questions3
## Problem solving techniques

- Describe 2 techniques to enumerate all subsets of the set $\{1, ..., n\}$.
  - Recursive
  - Bit shifting technique
- How do you solve [Geppetto](https://itu.kattis.com/problems/geppetto) using complete search?
  - First create a list of pairs
  - Call search (1)
  - search(k)
    - If k == n, add the pizza to the complete subset
    - Search with (k+1), aka without the current ingredient
    - Check for all pairs (k, l) or (l, k) if l is in the current search list
      - If it is, just continue 
      - If it isn't add k to the current subset, and call search(k+1) then remove it again
- How do you solve the `n x n`-queens problem using backtracking?
  - Create 3 arrays, col, diag and diag2
  - Call search(1)
  - search(r):
    - Iterate the columns (c)
      - If possible place, according to the arrays, place a queen and call(r+1), then remove it again
      - If you got to the end of the columns without placing any, then backtrack
    - If r==n+1 where n is the amount of rows, add it as a solution 
- How does the general outline of a greedy algorithm look like?
  - Take input
  - Sort by some criteria
  - Take from the input until you have the solution
- Describe the greedy algorithm for the `coin exchange problem`. What is its running time? Describe the central step in the correctness argument ("It's never wrong to take the largest coin that is at most as large as the current value")
  - First take an input such as [1,2,5,10,20,50,100,1000]
  - Iterate from right to left, taking a coin if the sum gets below or equal to the goal
  - O(n) in the worst case, where n is the length of the array
  - Taking the largest coin will always bring you closer to the goal, since there will only be smaller coins below it.
- Describe the greedy algorithm for `Task Scheduling`. What is its running time?
  - Sort the input by duration
  - That's it

## Dynamic programming

- Explain: How do you find the `n-th Fibonacci number` using dynamic programming? How does memoization work in this case?
  - Create a memoization array
  - Set the base case memo[0] = 0, memo[1] = 1
  - fib(n):
    - Check if memo[n] is set
    - If not calc memo[n] = fib(n-1)+fib(n-2)
    - Return memo[n]
- Why does the greedy algorithm not work for the [Exact Change](https://open.kattis.com/problems/exactchange2) problem?
  - Exact change requires you to possibly go above the change, which will not work in greedy.
  - Also greedy would select 1400 immediatly when there are smaller numbers that would fit better
- How would you solve the problem [Knapsack](https://open.kattis.com/problems/knapsack) using Dynamic programming?
- Describe: What is the difference between an iterative and a recursive implementation of a DP algorithm?
  - Iterative is more complex to implement, but is usually more memory efficient and faster
  - Recursive is easier to read and write, especially because dynamic programming usually works with recursion. But it requires knowledge of recursion limits.

## Graph algorithms

- Describe different data structures to store a graph. What are the pros and cons of each data structure?
  - Adjacency matrix: Easy to write and think about, also easy to access reverse edges. Very memory inefficient
  - Adjacency list: Same thing as adjacency matrix, harder to find reverse edges. Much more memory efficient
  - Structs and classes: Less memory efficient, easier to store more data
    - Can also be done in an adjacency list for some cross action
  - Hashmaps: Adjacency list, but with better lookup times of neighbors, or with less memory
- Given an undirected/directed graph, carry out `DFS` from a starting node.
  - Easy
- Carry out `BFS` on a given directed/undirected graph from a starting node.
  - Easy
- What is the running time of `DFS` and `BFS`?
  - O(V+E)
- Define: What is a topological sorting of a directed graph? How do you find one using `DFS`?
  - A topological sorting is a list of nodes, such that any node are guaranteed that all nodes pointing to it, is before it.
  - Takes O(V+E)
  - To find:
    - Make a visited list and a list for the result
    - Iterate every node in the graph (n)
      - Run dfs(n, visited, result)
        - Make a FILO stack
        - Add n with a temporary mark to it
        - While stack is not empty
          - Pop last element (n)
          - If temporary mark, add it to the stack again with a permanent mark, and add all it's neighbors with temporary marks
          - If permanent mark, add it to the result
          - If visited, ignore
    - Reverse the result
- Describe a kattis problem that can be solved by computing a topological sort.
  - Ours
  - Build dependencies

## Network flow

- Define: What is a flow in a graph? What is the value of a flow? What is the maximum flow?
  - Flow is hard to define. But it's a value that is on an edge, it must be under the capacity that edge has, and in some cases above the demand
  - The maximum flow is the max flow from the source to the sink, while respecting the capacities
- Define: What is a cut in a graph? How is the value of the cut defined? What is a minimum cut?
  - A cut is a set of edges that, when removed, make flow from a to b impossible
  - The value is the capacity of the removed edges
  - The min cut is the smallest possible value
- Given a directed, weighted graph and a pair of vertices `(s,t)`, how is the graph augmented for running a flow algorithm? (edges in opposite directions are added)
  - Ford-Fulkerson would add reverse edges with a capacity of zero to keep track of what's been used.
- Given a flow graph and some flow on edges, carry out one step in the algorithm: (1) `Ford-Fulkerson`, (2) `Capacity Scaling`, (3) `Edmonds-Karp`.
  - Ford-Fulkerson is hard to do, but take a path through the graph and add the min capacity to all the reverse edges of that path
  - For Edmonds-Karp run a BFS to find the path
  - For capacity scaling use DFS but with a threshold value
- What is the relation between the maximum flow value and the size of a minimum cut?
  - The min cut value is the same as the max flow, since a cut that blocks all flow from a to b, is the same as the flow from a to b
- Given a maxflow, find a minimum cut.
  - Find a set of edges that have their capacity filled (satisfied) and whose sum is equal to the max flow
- What is the running time for the different flow algorithms seen in class?
  - Ford-Fulkerson doesn't have one since it's up to the pathing algorithm
  - Edmonds-Karp is O(V*E^2)
  - Capacity scaling is O(E^2*log c) where c is the initial threshold value
- How do you solve a matching problem in a given undirected graph using a flow algorithm?
  - Make the graph bipartite, get the 2 sets of nodes
  - Make the edges between them directed in the direction of the sink
  - Create a source that connects to each node of the first set, with a capacity of 1
  - Create a sink that has a connection from each node of the other side with a capacity of 1
- Describe: How do you solve the [King of the North](https://open.kattis.com/problems/kingofthenorth) problem?

## Geometric algorithms

- Define: Given a set of points in the plane, what is their convex hull?
  - The convex hull is the smallest enclosing polygon around the points
- Describe the sweepline algorithm to find a convex hull.
  - Sort all the points by their x coordinate, then their y coordinate
  - Take the closest and furthest point and observe them as if there is a line between them, that line constitutes the upper and lower hull.
  - Iterate each point (p)
    - Add p to the hull
    - If the line between p and p-1 turns left, then pop p-1 until it doesnt.
    - If the last point has been reached, redo with the lower hull.
  - Append the 2 hulls, omitting the last point from the first, and the first point from the last
- What is the running time of the algorithm? Why?
  - O(3p log p) or just O(p log p). 2p or p, because we loop every point, p log p, because we sort
- In the sweep line algorithm, it is important to find out if a line turns "left/right". How do you do this algorithmically?
  - The cross product between 2 vectors says that if it's positive, left, negative, right, neutral, straight
- Given a polygon defined by a sequence of points, how do you compute its area?
  - For each point p
    - Draw a trapezoid with one edge being p-1 to p and the other being the y=0 plane
    - Calculate it's area and add it to the sum. This area is just the cross product
  - Sum all the areas and half the absolute value
- How do you solve [witchdance](https://open.kattis.com/problems/witchdance)?

## Interval queries

In the following, sparse table refers to the "square root" data structure.
- Given an array of integers, e.g., `[2, 8, 12, 1, 23, 56, 3, 10]`, and for the operations `min` or `sum`, 
   (i) build a sparse table with two blocks and (ii) build a segment tree. Carry out a query for two positions, e.g., `(3, 5)` in the respective data structures. Update the value of an element and carry out the query again.
  - Done
- Given an array of integers build a Fenwick tree from it. What is the meaning of the operation `i & -i`? Which operations are supported by the Fenwick tree? Show how to compute the `sum` of an interval. Why does it make sense that the array is 1-indexed?
  - The operation retrieves the least significant digit
  - Sum, or min up to r
  - We can manipulate i directly with bit operations when 1 indexed
- For all three data structures (Sparse Table, Segment Tree, Fenwick Tree), how long does it take to build the array representation for a given array? How long does a query take? How long does a single update take? 
  - Fenwick: Build takes O(n), query takes O(log n) and update takes O(log n)
  - Segment: Build takes O(n), query takes O(log n) and update takes O(log n)
  - Sparse : Build takes O(n), query takes O(sqrt n) and update takes O(1)
- How do you solve [_Supercomputer_](https://itu.kattis.com/problems/supercomputer) and [_Frosh Week_](https://itu.kattis.com/problems/froshweek) using a Segment or Fenwick tree?

## String algorithms

- Describe: How do you solve [Bing](https://itu.kattis.com/problems/bing) using a trie. Which augmentations do you need to apply to a standard trie? 
  - Augment the trie by saving how many time it has been accessed in each node
  - For each string s
    - Add to tree, when hitting a node, if it already exists, increment it's counter
    - If it's not there, add a node with the counter set at 0
- Describe: How does string hashing compute the hash code of a string. What is the role of `a` and `p`? 
  - $\sum_{i=0}^n s[i]\cdot a^{n-1-i}\mod p$
  - `a` and `p` are constants used for calculating, a is a multiplier and p is usually a prime
- Let's say `a` is 11 and `p` is 37. How does the polynomial for the string "APS" look like? (no evaluation, not important to get the ordinal representations of the characters right.)
  - $'A'\cdot a^2 + 'P'\cdot a^1 + 'S'\cdot a^0 \mod p$
- What is the probability that two _different_ strings of length `m` hash to the same integer? 
  - $1/p$
- What is an efficient way to compute the coefficients `a^{i}` for `i` in `{0, ..., m - 1}`?
  - Store them in an array
  - $p[0]=1$
  - $p[i]=p[i-1]\cdot a\mod p$
- Discuss: How can dvaput be solved using string hashing?

## Randomized algorithms

- Given a binary string $x$ of length $d$, how do you choose a MinHash hash function $h$ and what is the hash value $h(x)$?
  - Create an index array $[0,1,\dots,d-1]$ and shuffle it with some algorithm
  - Iterate the shuffled array and take the value $i$, check if $x[i]$ is a 1, if it is then the hash value is $i$. 
- Given two strings $x$ and $y$ with Jaccard similarity $J(x,y)$, what is the probability that $x$ and $y$ hash to the same value?
  - Proportional to $J(x,y)$
  - To find $J(x,y)$ count how many 1's are in the both arrays in the same place, and how many are just in 1 of the arrays, then $J(x,y)=\text{intersect}/\text{union}$
- How do you build a data structure to find a correlated pair using MinHash?
  - Hashmap

## Testing

This topic spans the entire course and the questions below applies to all Kattis problems. You might consider the [Geppetto](https://itu.kattis.com/problems/geppetto), [Coast](https://itu.kattis.com/sessions/sn33uo/problems/coast), and [Paintball](https://itu.kattis.com/sessions/jqxkhd/problems/paintball) problems as practice. 

- How would you evaluate the running time of your solution?
  - Count number of loops, and how much the loop proportional to the input
- Describe: What can you do to test the correctness of your solution? Does your approach differ depending on the problem?
  - Test cases
  - Ensure that for each step, if some precondition is known, then the postcondition matches the expected result
- Given a correct but slow implementation, how can you generate input to test the correctness of your solution?
  - Smaller inputs
  - Evaluate on a step level
