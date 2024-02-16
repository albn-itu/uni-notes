# Exercise 1
## a)
> Explain why $h_G$ is at least as accurate as $h_1$.

According to $h_1$ every tile must be reachable with enough moves, even if not blank, since one can move the tile on square B away, to make space for the tile on square A.

According to $h_G$ the square B must already be blank.

Therefore, $h_G$ is at least as accurate as $h_1$. Because $h_G$ is a more restrictive condition than $h_1$, therefore $h_1$ might overshoot the number of moves required to solve the puzzle.

## b)
> Show cases where $h_G$ is more accurate than both $h_1$ and $h_2$.

Take the goal state:
| 1 | 2 | 3 |
| 4 |   | 5 |
| 6 | 7 | 8 |

And the state:
| 1 | 2 | 3 |
| 4 |   | 7 |
| 6 | 8 | 5 |

The manhattan distance here is: $


## c)
> Explain how to calculate $h_G$ efficiently 

Imagine that the blank tile is in the correct position. Then just keep moving the misplaced tiles into it. Then find the tile that should go in the new blank space and teleport it there. Repeat until all tiles are in the correct position.

The value is the amount of moves.
