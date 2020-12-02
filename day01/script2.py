#!/usr/bin/env python3
import itertools

fn = "numbers.txt"

with open(fn, "r") as f:
    numbers = [int(l.strip()) for l in f]

for a, b, c in itertools.permutations(numbers, 3):
    if a + b + c == 2020:
        print(a * b * c)
        break
