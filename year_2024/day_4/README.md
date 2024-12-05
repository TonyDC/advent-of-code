# Day 4

## Part 1

The pattern positions are pre-computed and the values at those positions are checked against the expected values. 3 patterns are considered:

- horizontal
- vertical
- diagonal left
- diagonal right

Assume the following  system:

```text
 + -> y
 |
 v x
```

For the horizontal pattern, each input line is checked against the expected value. For the remaining patterns, a buffer is used whose size is equal to the minimum number of lines required to perform the match (since `XMAS`/ `SAMX` is 4 characters, a buffer of 4 lines is required). A FIFO strategy is used for the cache to evict the oldest line.

## Part 2

A similar approach is used in the second part. The novelty is in matching a cross (X).
