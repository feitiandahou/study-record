# Transaction And MVCC

## Scope

- ACID
- transaction isolation levels
- dirty read, non-repeatable read, phantom read
- undo log and read view
- snapshot read vs current read

## Must Know

- MVCC is mainly used to reduce read-write conflicts
- repeatable read in InnoDB depends on read view behavior
- current reads may still use locks
- phantom read handling is tied to both MVCC and locking behavior

## Practice Targets

- explain each isolation level with a concrete example
- describe how repeatable read is achieved in InnoDB
- distinguish snapshot read from current read

## Interview Prompts

- What problems do the four isolation levels solve?
- How does MVCC work in MySQL?
- Why can repeatable read still need gap or next-key locks?