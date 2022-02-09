# Graphs, DFS and BFS

## Undirected graphs

> A graph is a set of vertices(nodes) and a collection of edges that each connect a pair of vertices

>A path in a graph is a sequence of vertices connected by edges. A simple path is one with no repeated vertices. A cycle is a path with at least one edge whose first and last vertices are the same. A simple cycle is a cycle with no repeated edges or vertices (except the requisite repetition of the first and last vertices). The length of a path or a cycle is its number of edges

>A graph is connected if there is a path from every vertex to every other vertex in the graph. A graph that is not connected consists of a set of connected components, which are maximal connected subgraphs. 

> A tree is an acyclic connected graph. A disjoint set of trees is called a forest. A spanning tree of a connected graph is a subgraph that contains all of that graph’s vertices and is a single tree. A spanning forest of a graph is the union of spanning trees of its connected components. 

> A tree follows five conditions in a graph G with V vertices:
>
> - G has $V-1$ edges and no cycles
> - G has $V-1$ edges and is connected
> - G is connected, but removing any edge disconnects it
> - G is acyclic but adding any edge creates a cycle
> - Exactly one simple path connects each pair of vertices in G







## Directed graphs

> A directed graph (or diagraph) is a set of vertices and a collection of directed edges. Each directed edge connects an ordered pair of vertices.

> A directed path in a digraph is a sequence of vertices in which there is a (directed) edge pointing from each vertex in the sequence to its successor in the sequence. A directed cycle is a directed path with at least one edge whose first and last vertices are the same. A simple cycle is a cycle with no repeated edges or vertices (except the requisite repetition of the first and last vertices). The length of a path or a cycle is its number of edges

> A directed acyclic graph (DAG) is a diagraph with no directed cycles

> Two vertices v and w are strongly connected if they are mutually reachable: that is, if there is a directed path from v to wand a directed path from w to v. A digraph is strongly connected if all its vertices are strongly connected to one another.

> The transitive closure of a digraph G is another digraph with the same set of vertices, but with an edge from v to w in the tran-sitive closure if and only if w is reachable from v in G.