# Week 7

## 4.1.1

> What is the maximum number of edges in a graph with $V$ vertices and no parallel edges? What is the minimum number of edges in a graph with $V$ vertices, none of which are isolated?

Since the graph needs to be connected there has to be an edge between every node we have $n$ edges. But since the graph doesn't have to be connected, aka $start = end$ it must be $n-1$ edges

The maximum on the other hand has to be every node is connected to every other node. Which is $n + (n-1) + (n-2)\dots + (n-n)$ which then would be $\frac{n\cdot (n-1)}{2}$ .

## 4.2.1

> What is the maximum number of edges in a diagraph with $V$ vertices and no parallel edges? What is the minimum number of edges in a diagraph with $V$ vertices, none of which are isolated?

There should be no difference from the previous answer, there is still no parallel edges, so the same rules apply, the only difference is that the edges are now directed.

To clarify this answer. Usually in a directed graph there would be $n\cdot (n-1)$ edges. But since there are no parallel edges it would be half of those. There can't be parallel edges in an undirected graph, which is why the answer for that is the same.

## 4.1.28

> Two graphs are isomorphic if there is a way to rename the vertices of one to make it identical to the other. Draw all the nonisomorphic graphs with two, three and four vertices.

![img](D:\Uni\ALGO\exercices\Images\IMG_20210315_150637.jpg)

## 4.2.8

> Draw all the nonisomorphic DAGs with two, three and four vertices.

![img](D:\Uni\ALGO\exercices\Images\IMG_20210315_151542.jpg)

## 4.1.12

> What does the BFS tree tell us about the distance from $v$ to $w$ in an(undirected) graph when neither is at the root?

The shortest path between the two nodes

## 4.1.16

**Describe how to find**

> The eccentricity of a vertex (the length of the shortest path from that vertex to the furthest vertex from it)

One could do one of two things. First find the node the furthest away and find the shortest path. Or compare the shortest paths to all the nodes and take the largest one. The last of these possibilites is the most used.

> The diameter of a graph (the maximum eccentricity of any vertex in the graph

For every vertex/node do the above and select the largest accentricity

> The radius of a graph (the smallest eccentricity of any vertex in the graph)

For every vertex find the shortest path to every other node. And then select the smallest one

> A center of a graph (a vertex whose eccentricity is the radius of the graph

Do the above to get the radius of the graph. Then check every nodes eccentricity until you have one which is equal to the radius.

## 4.1.21





## 4.1.32

> Describe a linear-time algorithm to count the parallel edges in a graph.

```python
def f(adj: int[]):
    in = int[len(adj)]
    out = int[len(adj)]
    
    for i in range(0, range(adj)):
        for k in adj[i]:
            out[i] += 1
            in[k] += 1
```

The above algorithm is linear in number of edges

## 4.1.32

Remove an edge and run BFS each time. If we don't reach all nodes after removing we know it was a bridge