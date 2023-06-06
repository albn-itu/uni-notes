---
title: Graph Algorithms
tags: [ hello, world ]
date: 2023-06-06
---

See also: [[OtherNote]]

# Graph Algorithms
A graph conists of nodes and edges, also known as vertices and arcs. A path goes from on node to another, the length is the number of edges in it. A cycle is if the first and last node in a path is the same. It's a simple path if each node in the path appears at most once. 

A graph is connected if there is a path between any two nodes. The disconnected parts of a graph are called components. A tree is a connected graph with n nodes and n-1 edges, aka it has multiple nodes with only in edges.

A graph is directed if the edges have a direction. An edge can have a weight, these are often lengths, but can be capacity, price etc.

Two nodes are adjacent/neighbors if there is an edge between them.

## Representation
A graph can be represented as an adjacency list or an adjacency matrix. The adjacency list is a list of lists, where each list contains the neighbors of the node. The adjacency matrix is a matrix where each row and column represents a node, and the value is the weight of the edge between them.

A graph can also be represented as a list of edges, where each edge is a tuple of the two nodes and the weight. This can be hard to look up in.

## Traversal
### Depth-first search
A depth-first search starts at a node and goes as deep as possible before backtracking. Keeps track of visited nodes to ensure only visiting once.

```python
visited = set()
N = 10
adj = [[]]*N

def dfs(s):
    if s in visited:
        return
    visited.add(start)

    for next in adj[s]:
        dfs(next)
```

Iterative:
```python
def dfs(s):
    stack = [s]
    visited = set()

    while stack:
        node = stack.pop()
        if not node in visited:
          visited.add(node)

        for next in adj[node]:
            if not next in visited:
              stack.append(next)
```

### Breadth-first search
Same principle, but visists all neighbors before going deeper. Makes it easier to calculate distance to starting node, making it suitable for shortest path. Slightly harder to implement.

```python
adj = [[]]*N

def bfs(s, N):
  visited = set()
  distance = [0]*N
  queue = [s]

  while queue:
    node = queue.pop(0)

    for neighbor in adj[node]:
      if neighbor in visited:
        continue
      visited.add(neighbor)
      distance[neighbor] = distance[node] + 1
      queue.append(neighbor)
```

## Topological sorting 
Topological sorting is a way to order nodes in a directed acyclic graph. It's not possible if there is a cycle. It's usually done with a depth first search.


## Shortest path
### Dijkstra's algorithm
Dijkstra's algorithm finds the shortest path by keeping track of distances to nodes. Then using a priority queue it picks the one with the smallest distance to visit next. It has problems with negative weights.

It's time complexity is O(n+m log m) where n is the number of nodes and m is the number of edges.

```python
N = 10 # number of nodes
adj = [[]]*N

def dijkstra(start, end):
  visited = set()
  distance = [float('inf')]*N
  distance[start] = 0

  pq = [(0, start)]

  while pq:
    dist, node = pq.pop(0)

    if node in visited:
      continue
    visited.add(node)

    for next, weight in adj[node]:
      if distance[node] + weight < distance[next]:
        distance[next] = distance[node] + weight
        pq.append((-distance[next], next))

  return distance[end]
```




