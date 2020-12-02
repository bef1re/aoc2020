#!/usr/bin/env python3
import itertools

fn = "numbers.txt"

with open(fn, "r") as f:
    numbers = [int(l.strip()) for l in f]

for a, b in itertools.permutations(numbers, 2):
    if a + b == 2020:
        print(a * b)
        break
