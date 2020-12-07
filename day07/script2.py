#!/usr/bin/env python3

"""
We recurse, but remember the count
So we check everything max once

Kind of lazy loading
"""

bags = {}

def count_bags_inside(bag):
    if bag["value"] > 0:
        return bag["value"]

    for child in bag["children"].copy():
        bag["value"] += count_bags_inside(bags[child]) + 1
        bag["children"].remove(child)

    return bag["value"]


with open("input.txt", "r") as f:
    for line in f:
        name, content = line.strip().split(" bags contain ")

        bags[name] = {"value": 0, "children": []}

        if content != "no other bags.":
            for bag in content.split(", "):
                amount, prefix, color, _ = bag.split()
                bags[name]["children"] += [f"{prefix} {color}"] * int(amount)

print(count_bags_inside(bags["shiny gold"]))
