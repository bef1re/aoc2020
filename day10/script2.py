#!/usr/bin/env python3

values = []
with open("input.txt", "r") as f:
    for line in f:
        values.append(int(line))

values.sort()
values.append(max(values) + 3)

recents = [{"number": 0, "paths": 1}]

for i in values:
    paths = 0

    for previous in recents:
        if previous["number"] >= i - 3:
            paths += previous["paths"]

    print(f"i: {i}\tpaths: {paths}\trecents: {recents}")

    recents.append({"number": i, "paths": paths})

    if len(recents) > 3:
        recents.pop(0)
