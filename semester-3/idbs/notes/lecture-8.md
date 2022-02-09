

# Lecture 8

## Indexes

- Clustered indexes
  - Faster
  - More optimized in data structure
  - Harder to keep updated
  - One disk read
- Unclustered indexes
  - Less efficient in smaller dataset
  - Lots of random disk reads
- Index scan vs full table scan
  - Clustred is optimized for point and range queries, and  is really good at
  - Unclustered are best for high selectivity queries, that are quite rare.
  - Full tble scan = Reading the entire table and querying
  - Index scan = Retrieving a record or range from an index, much much faster, but qeruires manually configuring it.
- Covering index
  - When ALL attributes, including select, are covered by an index
  - Needs 0 disk reads, only the index is read
  - Should be non clustered
  - Fast as fuck
- 