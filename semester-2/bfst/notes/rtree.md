# RTree - Running time
## STR
### Worst and average case
Our worst and average are the same, as the only differing case, is that of the best case, which is pretty rare.

Let's define some variables:

$r_x$ is the amount of entries on the $x$'th level

$n$ number of entries a node can hold

$p_x$ the amount of nodes on each level, calculated by $\lceil\frac{r_x}{n}\rceil$

$s_x$ the amount of slices on each level, calculated by $\lceil\sqrt{p_x}\rceil$

$d_x$ the size of each slice, calculated by $s_x \cdot n$

$h$ is the height of the tree calculated by $\log_n r_0$

Before the recursion, every data element is looped through, which adds linear in all data elements.

For each level all the entries are sorted using modified timsort ([src](https://docs.oracle.com/javase/8/docs/api/java/util/List.html#sort-java.util.Comparator-)), assuming standard timsort, $O(r\log r)$ ([src](https://en.wikipedia.org/wiki/Timsort))

Then they are cut into slices, which takes $O(r_x)$ time. All those slices are then, internally, sorted, which means sorting $s_x * (d_x \log d_x)$

After that each slice is partitioned into nodes, which creates new arraylists, from the existing ones, another linear operation over every data point, twice, as new ArrayList and clear are linear

So the full equation for a level is, in order of operations:

$$
r_x\log(r_x) + s_xd_x + s_xd_x^2 + 2s_xd_x\log(d_x)+2s_xd_xM + \frac{d_x}{M} 
$$

$$
h\cdot\left(r\log(r) + sd + sd^2 + 2sd\log(d)+2sdM + \frac{d}{M}\right) 
$$

$$
O(\log_M(h)\cdot  sd^2)
$$
### Best case
$O(n)$, as you only have to create the first root level node and the data entries, which takes $n + 1$ time.

## Query
### Best case
The best case is $n\leq M$, which would be $O(n)$

### Worst case
Worst case is $O(\log M \cdot n)$, where $M$ is max entries in a node, and $n$ is the amount of data entries, on the leaf level.

$\log M\cdot n$ represents the theoretical amount of nodes in the tree.

## NN
### Best case
The best case is $n\leq M$, which would be $O(n)$

### Average case


### Worst case
Visiting every single entry in the tree:
$O(\log(M)\cdot n)$

## Improvements
- Do not insert ~10% of the data in STR bulk loading, insert that with the normal insert method, this would force the tree to be more R-tree like.
- Attempt OMT bulk loading
  - Minimizes overlap in DIRECTORY nodes, not in leaf nodes [src](http://ceur-ws.org/Vol-74/files/FORUM_18.pdf)
  - Uses a top down strategy
  - Could result in better query times, as the directory rectangles basically do not overlap.
- Research other methods of bulk loading, or modify existing versions to resemble and R*-tree more
- Remove sublist.clear, and use an offset instead, as that line uses $n^2$ time, where $n$ is the size of the sublist
- NN
  - Remove the priority queue
  - Add the object you are currently looking at to the PQ 
- Fix that we have 2 ways of calculating distance, which could result in the wrong result

## Standard vs R*
- Standard is based on minimizing the area of the enclosing node, so having the closes rectangles together
- R* is based on
  - the area, as before
  - the overlap of directory rectangles, which minimizes the paths to traverse
  - the margin of the directory rectangles, assuming fixed area, the smallest margin (the sum of the side lengths) is more square
  - Storage utilization, use the maximum amount of entries in nodes, to minimize tree height.
  
  - Area and overlap, require more freedom in storage, thus decreasing storage utilization
  - Those also require more freedom in shape, thus decreasing the margin
  - Area might decrease overlap, as the sheer size of the rectangle is decreased
  - Margin will also decrease storage utilization, but could theoretically increase it as well, as they are easier to pack together