#!/usr/bin/env python3

highest = 0 

with open("input.txt", "r") as f:
    for line in f:
        bits = line.strip().replace("B", "1").replace("F", "0").replace("L", "0").replace("R", "1")
        seat_id = int(bits, 2)
        if seat_id > highest:
            print(highest)
            
print(highest)
