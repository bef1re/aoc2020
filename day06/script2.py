#!/usr/bin/env python3
"""
This time we're using sets again, but in a different way.

The question boils down to:
- Every line in a group is a set.
- What is the intersection of those sets?
"""

groups = []
with open("input.txt", "r") as f:
    group = []
    for line in f:
        if line == "\n":
            groups.append(group)
            group = []
            continue

        group.append(set(line.strip()))

total = 0
for group in groups:
    answer = len(set.intersection(*group))
    print(answer)
    total += answer

print(total)
