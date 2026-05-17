# Index

## Scope

- B+ tree basics
- clustered index and secondary index
- covering index
- back to table lookup
- leftmost prefix rule
- index invalidation cases

## Must Know

- InnoDB uses clustered storage around the primary key
- secondary index leaf nodes store primary key values
- covering indexes avoid extra table lookups
- functions, implicit conversions, and leading wildcards can disable index usage

## Practice Targets

- design compound indexes for common filters
- explain why a query used or skipped an index
- compare `select *` with covered-column queries

## Interview Prompts

- Why does MySQL commonly use B+ trees for indexes?
- What is the difference between clustered and non-clustered indexes?
- What does the leftmost prefix rule mean?
- In what cases does an index fail to take effect?