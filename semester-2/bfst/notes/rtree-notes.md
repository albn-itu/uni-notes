# R*-tree

## Notes

### Principles of R-tree

![R-tree - Wikipedia](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6f/R-tree.svg/1200px-R-tree.svg.png)

#### Leaf nodes and non leaf nodes

A non leaf node contains entries of the form *(cp, Rectangle)* where *cp* s the address of the child node in the R-tree an *Rectangle* is the minimum bounding rectangle of all rectangles which are entries in that child node.

A leaf node contains entries of the form *(Oid, Rectangle)* where *Oid* refers to a record in the database describing a spatial object (circle, square, line, point, etc) and *Rectangle* is the enclosing rectangle of that spatial object.

Let $M$ be the maximum number of entries in a node, and let $m$ specify the minimum number of entries in a node ($2 \leq m\leq M/2$. Then an R-tree satisfies

- The root has at least two children unless it's a leaf
- Every non-leaf node has between $m$ and $M$ children unless it is the root
- Every leaf node contains between $m$ and $M$ entries unless it is the root
- All leaves appear on the same level

#### Optimization criteria

> The area covered by a directory rectangle should be minimized

AKA the area covered by a bounding rectangle NOT covered by a child rectangle should be minimized

> The overlap between directory rectangles should be minimized

This also decreases the number of search paths

> The margin of a directory rectangle should be minimized

The margin is the sum of the rectangles edge lengths. If fixed area then the smallest margin is a square, thus minimizing margin but not area. This improves the structure as quadratic objects are easier to pack into squares.

> Storage utilization should be optimized

Higher storage utilization will reduce the query cost as the height of the tree will be kept low, and the width will be higher.

### Algorithms

#### Values

##### Overlap

> Technically not an algorithm

Let $E_1,\ ,E_p$ be the entries in the current node
$$
\text{overlap}(E_k) = \sum_{i=1,i\neq k}^{p} \text{area}(E_k\text{Rectangle}\cap E_p\text{Rectangle})\ , 1\leq  k\leq p
$$

#### Distributions

``bb`` denotes the bounding box of a set of rectangles
$$
\begin{align*}
\text{area-value} &= \text{area}[\text{bb}(\text{first group})] + \text{area}[\text{bb}(\text{second group})]\\
\text{margin-value} &= \text{margin}[\text{bb}(\text{first group})] + \text{margin}[\text{bb}(\text{second group})]\\
\text{overlap-value} &= \text{area}[\text{bb}(\text{first group})\cap \text{bb}(\text{second group})]\\
\end{align*}
$$


#### ChooseSubtree

> Finds the most suitable subtree, on every level, for a new entry

```
Set N to be the root
If N is a leaf,
	Return N
Else
	If the childpointers in N point to leaves
		Choose the entry in N whose rectangle needs least overlap enlargement to indlude the
		- new data rectangle. Resolve ties by choose the entry whose rectangle needs least area
		- enlargement then then the entry with the rectangle of smallest area
	If the childpoiters in N do not point to leaves
		Choose the entry in N whose reactangle needs least area enlargement to include the
        - new data rectangle. Resolve ties by choosin the entry with the rectangle of smallest
        - area
Set N to be the childnode pointed to by the childpointer of the chosen entry and repeat
```



#### ChoseSplitAxis

```
For each axis
	Sort the entries by the lower then by the upper value of their rectangles and determine all
	- distributions as describe above compute the sum of all margin values of the different
	- distributions and denote it S
Choose the axis with the minimum S as split axis
```



#### ChooseSplitIndex

```
Along the chosen split axis, choose the distribution with the minimum overlap-value.
- Resolve ties by choosing the distribution with minimum area-value
```



#### Split

> Distributes $M+1$ rectangles into two nodes in the most appropriate manner

```
Invoke ChooseSplitAxis to determine the axis perpendicular to which the split is performed
Invoke ChooseSplitIndex to determine the best distribution into two groups along that axis
Distribute the entries into two groups
```



#### InsertData

> Inserts an entry

```
Invoke Insert starting with the leaf level as a parameter to insert a new data rectangle
```



#### Insert

```
Invoke ChooseSubtree with the level as a parameter to find an appropriate node N in which to
- place the new entry E
If N has less than M entries:
	Place E in N.
If N has M entries:
	Invoke OverflowTreatment with the level  of N as a parameter
If OverflowTreatment was called and a split was performed:
	Propagate OverflowTreatment upwards if necessary
If OverflowTreatment caused a split of the root:
	Create a new root
Adjust all covering rectangles in the insertion path such that they are minimum boundix boxes
- enclosing their children rectangles
```



#### OverflowTreatment

>  Adjust bounding box to remove overflow

```
If the level is not the root level and this is the first call of OverflowTreatment in the given
- level during the insertion of one data rectangle:
	Invoke ReInsert
Else:
	Invoke Split
```



#### ReInsert

> Removes entry and inserts it again to force correct insertion. Basically the principle of insertion sort.
>
> - Forced reinsert changes entries between neighboring nodes and thus decreases the overlap
> - As a side effect storage utilization is improved
> - Due to more restructuring less splits occur
> - Since the outer rectangles of a node are reinserted the shape of the directory rectangles will be more quadratic

```
For all M+1 entries of a node N:
	Compute the distance between the centers of their rectangles
	- and the center of the bounding rectangle of N
Sort the entries in decreasing order of their distances computed above
Remove the first p entries from N and adjust the bounding rectangle of N
In the sort starting with the maximum distance(far reinsert)
- or minimum distance (close reinsert) invoke Insert to reinsert the entries
```

$p$ can be tuned for better performance, but a good start is 30%



#### PickSeeds

> Find the two rectangles which would waste the largest area put in one group



#### DistributeEntry

> Assigns the remaining entires by the criterion of minimum area

```
Invoke PickNext to choose the next entry to be inserted
Add it to the group whose covering rectangle will have to be enlargened least to accomadate it.
- Resolve ties by adding the entry to the group with the smallest area
- then to the one with the fewer entries
- then to either
```



#### PickNext

> Chooses the entry with the best area-goodness-value in every situation

```
For each entry E not yet in a group:
	Calculate d_1 = the area increase required in the covering rectangle of Group 1
	- to include E Rectangle
	Calculate d_2 anagolously for Group 2
Choose the entry with the maximum difference between d_1 and d_2
```



### STRPack

> Packs rectangles into nodes and creates the tree bottom up

$r$ is the number of source rectangles  (entries)

$n$ is the number of rectangles a node can hold

Then we calculate $P$ the number of leaf level pages by $P=\lceil\frac{r}{n}\rceil$ and $S=\lceil\sqrt{P}\rceil$ 

```
Sort the entries by minimum X coordinate
Partition the rectangles into S slices (a slice contains S*n entries)
Sort each slices entries by min y
Pack each slices entries into nodes

```



