# Day 2

## Part 1

Two tests are used:

- monotonicity: all elements should be increasing or decreasing
- delta: all differences should be between 1 and 3, inclusive in both sides

## Part 2

A list containing the delta values between pairs of points is computed. In addition, a brute-force approach is used, in which a point from the sequence is removed and compared against the aforementioned tests. Adding 2 delta values is equivalent to removing the middle point. One must also take into account that the points at the extremities can be removed as well. In this case, not considering the delta value is enough.
