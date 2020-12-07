#!/usr/bin/env python3

"""
We recurse, but remember the valid bags
So we check everything max once
"""

dead_ends = set()
valid = {"shiny gold"}

bags = {}

def check(bag):
    if bag in valid:
        return True
    elif bag in dead_ends:
        return False

    if bags[bag] & valid:
        valid.add(bag)
        return True
    else:
        for item in bags[bag]:
            if item in valid:
                valid.add(bag)
                return True
            elif item in dead_ends:
                continue
            elif check(item):
                valid.add(bag)
                return True

        dead_ends.add(bag)
        return False
        
with open("input.txt", "r") as f:
    for line in f:
        name, content = line.strip().split(" bags contain ")

        if name in valid:
            continue

        if content == "no other bags.":
            dead_ends.add(name)
        else:
            bags[name] = set()
            for bag in content.split(", "):
                amount, prefix, color, _ = bag.split()
                bags[name].add(f"{prefix} {color}")

for bag in bags:
    check(bag)

ordered = list(valid)
ordered.sort()

print(len(valid) - 1)
