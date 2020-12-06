#!/usr/bin/env python3
"""
Let's use the behaviour of sets.

Sets can have only unique elements, 
so we just .add() everything to a set
and count the length.
"""

answers = []
with open("input.txt", "r") as f:
    current = set()
    for line in f:
        if line == "\n":
            answers.append(current)
            current = set()
            continue

        for c in line.strip():
            current.add(c)


total = 0
for answer in answers:
    total += len(answer)
    print(len(answer))

print(total)
