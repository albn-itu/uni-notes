---
title: Questions2
tags: [ hello, world ]
date: 2023-06-10
---

# Questions2
## Problem solving techniques

- Describe 2 techniques to enumerate all subsets of the set $\{1, ..., n\}$.
  - Recursion
  - Iterative bit technique
- How do you solve [Geppetto](https://itu.kattis.com/problems/geppetto) using complete search?
  - Keep a list of ingredients
  - For each call loop available ingredients
    - Loop pairs and check if the ingredient currently being evaluated is in there, and if it's on the pizza
    - If it is, continue without it
    - If it isn't add it
- How do you solve the `n x n`-queens problem using backtracking?
  - Keep 3 arrays, one for if there is a queen on the column, one for diagonal, and another for the other diagonal
  - Define a method search that takes a row number
  - On search loop all columns, checking if a queen can be added via the arrays
    - If it can, add it and call search(row+1)
    - It it can't continue
    - If it isn't possible at all to place any queens, just return as the configuration isn't working.
- How does the general outline of a greedy algorithm look like?
  - Read input and sort by some parameter that would solve the greedy algorithm
  - Iterate the input and just take until the problem is solved
- Describe the greedy algorithm for the `coin exchange problem`. What is its running time? Describe the central step in the correctness argument ("It's never wrong to take the largest coin that is at most as large as the current value")
  - You have [1,2,5,10,20,50,100,1000] coins
  - Already sorted
  - Take a goal
  - Iterate from reverse taking the first coin that is below or equal to the goal
  - Iterate from that point again, taking a coin if it' brings the total to or above the goal
  - Return the total
- Describe the greedy algorithm for `Task Scheduling`. What is its running time?
  - Sort the input based on it's duration
  - Repeadetly take the one with the smallest duration, the sorted list is actually the solution
  - O(n log n) because of the sorting

## Dynamic programming

- Explain: How do you find the `n-th Fibonacci number` using dynamic programming? How does memoization work in this case?
  - Define the base case, fib(0) = 0 and fib(1) = 1
  - When fib is called, check if memo[n] is set, if not call fib(n-1)+fib(n-2)
  - When calculated set memo[n] to the result
  - Return the result
- Why does the greedy algorithm not work for the [Exact Change](https://open.kattis.com/problems/exactchange2) problem?
  - The greedy algorithm won't find the most optimal solution since it would select 1400 immediatly, but the solution is 1000+5000
  - The better solution would be to run a complete search with some dynamic programming in it. Fx. by creating a table of the most optimal amount of coins to get to the sum x. 
    - First create a table with the max value 10000 + 1 (to also store the base case 0)
    - Iterate every coin
      - Iterate from the max value - coin to 0 (i)
        - Set table[i+coin] to the minimum of the value currently in it (the amount needed to create that value) and table[i]+1, the amount of coins needed to create the current value, with a coint added.
        - You essentially check if you can make the coin amount smaller by using the current coin
    - Iterate from the goal to the max, finding the first value that is not the default value
- How would you solve the problem [Knapsack](https://open.kattis.com/problems/knapsack) using Dynamic programming?
- Describe: What is the difference between an iterative and a recursive implementation of a DP algorithm?
  - An iterative is usually faster and less memory hungry, but it's more complex to write
  - An iterative can be easier in languages withou global states

## Graph algorithms

- Describe different data structures to store a graph. What are the pros and cons of each data structure?
  - Adjacency matrix: Easy to think about and write, uses a lot of memory
  - Adjacency list: Easy to think about and write, uses much less memory. Can be harder to look up reverse edges
  - List of tuples: Hard to quickly look up in, in both directions
  - Hashmap: Adjacency list with even less memory.
  - Classes or structs: Allows for storing more data than just integers
- Given an undirected/directed graph, carry out `DFS` from a starting node.
  - Easy
- Carry out `BFS` on a given directed/undirected graph from a starting node.
  - Easy
- What is the running time of `DFS` and `BFS`?
  - BFS: O(V+E)
  - DFS: O(V+E)
- Define: What is a topological sorting of a directed graph? How do you find one using `DFS`?
  - Topological sorting is a sorting where each node a has all incoming edges coming from nodes before it in the sorting.
  - From every node, run DFS. Add the path in reverse to the sorting
  - If you hit a vertex you have already hit, to the same
- Describe a kattis problem that can be solved by computing a topological sort.
  - Ours
  - Build dependencies?

## Network flow

- Define: What is a flow in a graph? What is the value of a flow? What is the maximum flow?
  - Flow is a value of some kind, could be liquid, that is increased across the graph
  - The value is something that is under the capacity
  - Maximum flow is the maximum allowed flow to go through the graph while respecting capacities
- Define: What is a cut in a graph? How is the value of the cut defined? What is a minimum cut?
  - A cut is a certain amount of removed edges that make it impossible to flow from node a to node b
  - The value is the sum of the capacities/flow of the removed edges
  - Minimum cut is the set of edges with the smallest possible value to block flow from a to b
- Given a directed, weighted graph and a pair of vertices `(s,t)`, how is the graph augmented for running a flow algorithm? (edges in opposite directions are added)
  - Reverse edges are added, and in some cases the flow is set
- Given a flow graph and some flow on edges, carry out one step in the algorithm: (1) `Ford-Fulkerson`, (2) `Capacity Scaling`, (3) `Edmonds-Karp`.
  - Done
- What is the relation between the maximum flow value and the size of a minimum cut?
  - The value is the same, since to get some amount of flow to the sink, it has to flow over the cut
- Given a maxflow, find a minimum cut.
  - Find edges that all have their flow satisfied
  - Check their sum is maxflow
- What is the running time for the different flow algorithms seen in class?
  - Ford-Fulkerson (Edmond): O(m^2 * n)
  - Capacity: O(m^2 * log c) where c is the initial capacity
- How do you solve a matching problem in a given undirected graph using a flow algorithm?
  - Bipartite graph, a graph that can be split into 2 sets, where each set only depends on the other side
  - Find the bipartite graph, and create 2 sets of nodes on each side
  - Create a source and sink
  - Connect the source to all nodes in one set with a capacity of 1
  - Connect the sink to all nodes in the other set with a capacity of 1
  - Make the existing edges directed away from the source
  - The flow over the graph is the maximum matching amount of pairs
- Describe: How do you solve the [King of the North](https://open.kattis.com/problems/kingofthenorth) problem?

## Geometric algorithms

- Define: Given a set of points in the plane, what is their convex hull?
  - The smallest possible polygon that contains all the points
- Describe the sweepline algorithm to find a convex hull.
  - Sort all the points by their x coordinate, then their y-coordinate
  - Select the leftmost and rightmost points, the line between these 2 points split the hull in the upper and lower hull
  - To find the upper iterate all points (p)
    - Add point p to the hull
    - If the line from the previous points to p turns left, then pop all points before it, unless it's the start point
    - Do this until you hit the end point, and add it
  - To find the lower do exactly the same from the end point to the start point
  - Concat the 2 arrays, emitting the end from the first list, and the end from the last list
- What is the running time of the algorithm? Why?
  - O(2n log n) or just O(n log n). n log n because we sort and then we loop through all the points
- In the sweep line algorithm, it is important to find out if a line turns "left/right". How do you do this algorithmically?
  - Take the cross product of the point and the point before, if the result is positive it turns left, negative it turns right, and if it's 0 it's straight
- Given a polygon defined by a sequence of points, how do you compute its area?
  - Create a trapezoid from each edge to the plane y=0. Calculate the sum of their lengths, half the absolute sum and you have the result
  - The lengths of the edges is the cross product between the 2 points, so it can be simplified to $0.5\cdot abs(sum(cross(point))))$
- How do you solve [witchdance](https://open.kattis.com/problems/witchdance)?

## Interval queries

In the following, sparse table refers to the "square root" data structure.
- Given an array of integers, e.g., `[2, 8, 12, 1, 23, 56, 3, 10]`, and for the operations `min` or `sum`, 
   (i) build a sparse table with two blocks and (ii) build a segment tree. Carry out a query for two positions, e.g., `(3, 5)` in the respective data structures. Update the value of an element and carry out the query again.
  - Done
- Given an array of integers build a Fenwick tree from it. What is the meaning of the operation `i & -i`? Which operations are supported by the Fenwick tree? Show how to compute the `sum` of an interval. Why does it make sense that the array is 1-indexed?
  - The operation is the binary way of finding the least significant digit
  - Fenwick can sum or min or max, and update
  - Take the sum up to a point, and then the sum to the other, subtract from each other
- For all three data structures (Sparse Table, Segment Tree, Fenwick Tree), how long does it take to build the array representation for a given array? How long does a query take? How long does a single update take? 
  - Spare table: build takes O(n+sqrt n), query takes O(sqrt n) and update takesO(1)
  - Segment tree: build takes O(n+log n), query takes O(log n) and update takes O(log n)
  - Fenwick tree: build takes O(n+log n), query takes O(log n) and update takes O(log n)
- How do you solve [_Supercomputer_](https://itu.kattis.com/problems/supercomputer) and [_Frosh Week_](https://itu.kattis.com/problems/froshweek) using a Segment or Fenwick tree?

## String algorithms

- Describe: How do you solve [Bing](https://itu.kattis.com/problems/bing) using a trie. Which augmentations do you need to apply to a standard trie? 
  - Create a trie with a counter of how many times it's been accessed
  - For each word, add it to the trie
    - If the node has been added earlier, increase it's counter
    - Otherwise add it with a counter of 0
    - If the entire word is already in the trie, print the counter on the end node
- Describe: How does string hashing compute the hash code of a string. What is the role of `a` and `p`? 
  - String hashing uses the formula $(\sum_{i=0}^n s_i\cdot a^{n-i-1}) \mod p$
  - `a` is one of the constants, the multiplier
  - `p` is the other constant, the modulo, should be a prime.
  - `a` and `p` should be sufficiently large to ensure that no collisions happen
- Let's say `a` is 11 and `p` is 37. How does the polynomial for the string "APS" look like? (no evaluation, not important to get the ordinal representations of the characters right.)
  - $'A'\cdot 11^2 + 'P'\cdot 11^1 + 'S'\cdot 11^0$
- What is the probability that two _different_ strings of length `m` hash to the same integer? 
  - $1/p$
- What is an efficient way to compute the coefficients `a^{i}` for `i` in `{0, ..., m - 1}`?
  - `p[0]=1`
  - `p[i]=a^i mod b`
- Discuss: How can dvaput be solved using string hashing?

## Randomized algorithms

- Given a binary string $x$ of length $d$, how do you choose a MinHash hash function $h$ and what is the hash value $h(x)$?
  - Create an index array $[0,1,....,d]$
  - Shuffle it
  - Iterate the index array and apply it to the binary string, the first time it hits 1 is the hash value
- Given two strings $x$ and $y$ with Jaccard similarity $J(x,y)$, what is the probability that $x$ and $y$ hash to the same value?
  - The probability is equal to $J(x,y)$
  - J(x,y) is calculated by dividing all the positions that both have 1 and all that just have a 1 somewhere
- How do you build a data structure to find a correlated pair using MinHash?
  - Create a hashmap of buckets. The key can be a single or a list of hash values

## Testing

This topic spans the entire course and the questions below applies to all Kattis problems. You might consider the [Geppetto](https://itu.kattis.com/problems/geppetto), [Coast](https://itu.kattis.com/sessions/sn33uo/problems/coast), and [Paintball](https://itu.kattis.com/sessions/jqxkhd/problems/paintball) problems as practice. 

- How would you evaluate the running time of your solution?
  - Figure out what loops go through the input, and how much they do so
- Describe: What can you do to test the correctness of your solution? Does your approach differ depending on the problem?
  - Test cases?
- Given a correct but slow implementation, how can you generate input to test the correctness of your solution?
  - Generate large inputs that show the problems
  - Generate small inputs with edge cases

