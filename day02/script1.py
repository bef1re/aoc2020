#!/usr/bin/env python3

with open("input.txt", "r") as f:
    count = 0
    for line in f:
        policy, password = line.split(": ")
        leastmost, letter = policy.split(" ")
        least, most = leastmost.split("-")
        least = int(least)
        most = int(most)

        amount = 0
        for c in password:
            if c == letter:
                amount += 1

        if amount >= least and amount <= most:
            count += 1

    print(count)
