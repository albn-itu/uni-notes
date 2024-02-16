# Mandatory 1
## a)
For $w=1$ we get the function $f(n) = 0*g(n) + 1*h(n) = h(n)$, which is just the greedy best-first search algorithm.

For $w=0.5$ we get the function $f(n) = 0.5*g(n) + 0.5*h(n)$, which is just the A* algorithm, since each estimated cost is equally weighted.

## b)
Weighted A* trades off optimality for speed, so it is not guaranteed to find the optimal solution unless the weights are either $w=0$ or $w=0.5$. In the case of $w=0$ the algorithm is just Dijkstra's algorithm, which is guaranteed to find the optimal solution. And in the case of $w=0.5$ the algorithm is just the A* algorithm, which is also guaranteed to find the optimal solution.

Both of these are much slower than weighted A*, but they are guaranteed to find the optimal solution.
