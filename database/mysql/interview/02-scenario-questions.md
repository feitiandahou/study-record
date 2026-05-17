# Scenario Questions

## Slow SQL

- A query suddenly becomes slow after data growth. What do you inspect first?
- An index exists but the optimizer still scans many rows. What are your hypotheses?

## Concurrency

- An order creation flow occasionally deadlocks. How do you locate the root cause?
- A transaction timeout increased after a new feature launch. What would you verify?

## Data Growth

- A table reached tens of millions of rows. What optimization path would you evaluate?
- Offset pagination is too slow for later pages. What alternatives would you propose?

## Architecture

- Reads are much higher than writes. How would you redesign access patterns?
- A replica is delayed by several seconds. How do you decide whether the delay is acceptable?