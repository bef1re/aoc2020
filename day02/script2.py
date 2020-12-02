#!/usr/bin/env python3

with open("input2.txt", "r") as f:
    count = 0
    for line in f:
        policy, password = line.split(": ")
        firstlast, letter = policy.split(" ")
        first, last = firstlast.split("-")
        first = int(first)
        last = int(last)

        if (password[first - 1] == letter) ^ (password[last - 1] == letter):
            count += 1

    print(count)
