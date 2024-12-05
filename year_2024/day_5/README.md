# Day 5

## Part 1

The first section of the input contains the ordering rules. For example, `47|53` dictates that 53 can only appear in the sequence AFTER 47 (if 47 is in the sequence). A sequence is valid if it is not invalid. To check whether a sequence is invalid, a violation in one of the rules must be found.

`violation_rules` is a dictionary that specifies which numbers must not appear after the key appears in the sequence. For example, `53: {47}` specifies that if a 47 is found after 53, then the sequence is invalid. In other words, the dictionary values are sets containing values that must not appear in the sequence after the key is found in said sequence.

When processing a sequence, the respective list of violation sets is determined. Consider the following input:

```text
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
```

The execution context is as follows:

```text
violation_rules: defaultdict(<class 'set'>, {53: {97, 75, 61, 47}, 13: {97, 75, 47, 61, 53, 29}, 61: {97, 75, 47}, 47: {97, 75}, 29: {97, 75, 47, 53, 61}, 75: {97}})

sequence: [75, 47, 61, 53, 29]

violation_sets: [{97}, {97, 75}, {97, 75, 47}, {97, 75, 61, 47}, {97, 75, 47, 53, 61}]
```

Note that each set in `violation_sets` contains the values that violate the rules for each respective element in `sequence`.

For each element in `sequence`, if a match is found in one of the previous sets, the sequence is invalid. Only valid sequences should have their middle values added up.

## Part 2

The same principle outlined in `Part 1` still applies. The new requirement is: if a violation is found, the sequence values are swapped, as well as their respective violation sets. If a violation is found, the index of the set in `violation_sets` dictates the element in `sequence` that should be swapped. Only the middle values of previously invalid sequences should be added up.
