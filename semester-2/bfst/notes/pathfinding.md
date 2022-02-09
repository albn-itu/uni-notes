# Pathfinding
## Graph
Adjancy list, you get a list of all the edges pointing out from a vertex.

### Adding to graph
- Parse the way
- Calculate the distance to the to coordinate from the from coordinate, like the crow flies.
- Add to graph, with the distance as the weight

### Route
Using MinPQ
- Insert start point in PQ
- Loop while PQ is not empty
  - Stop of end is found
  - Travel the path that results in the shortest path, by selecting the way with the lowest weight
  - If the distTo[f] is lower than distTo[t] use distTp[f], where f and t are from and to from the current edge
  - If it exists in the pq
    - decrease it's value, as it is a bad path
  - else
    - Insert in the PQ, using the heuristic

**Heuristic**

The heuristic is the distance dividied by the max speed on that road, which would be the best possible time, assuming 0 acceleration time.

## Route planner
- Get the closest road to the given point, no matter the name of the point
- Get the closest edge and coordinate to the given point
- Use vector calculation to determine whether or not we are turning

## Graph compressor
If we have 3 points, that are connected, but do not branch out, simplify to 2 points.
Such as A -> B -> C = A -> C

If they do branch out, fx in an intersection, do not simplify.
This is done on all the intermediary points in a way

## Improvements
- Represent 2 way roads with a single edge, instead of the 2 currently being used
- We don't compress the graph while building, only after.
- Merge large roads together
- Multithreaded