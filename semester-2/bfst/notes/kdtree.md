# KD-tree
Unbalanced binary tree

## Insert
- Shuffle
- Insert every node indivdually
- Find the split line
- Insert on the appropriate side of the split line
  - Insert on the right if that is not possible

## Search
Returns a list, which uphold a lambda expression
- Recursively walk tree on left and right side
  - checking if the nodes are inside the search range
  - checking if the nodes uphold the lambda expressionb
- If the entirety of a node is contained in the search range, we can just add the entire thing to our result

## NN
- Check each node if it's the closest to the input node
- If one side's node is clearly closer, use that side, instead of the other side

## Improvements
- Bulk loading
- Using buckets, so kinda of an R-tree style, with nodes, instead of just 2 children 