#!/usr/bin/env python3

seats = []

with open("input.txt", "r") as f:
    for line in f:
        bits = line.strip().replace("B", "1").replace("F", "0").replace("L", "0").replace("R", "1")
        seat_id = int(bits, 2)
        seats.append(seat_id)

seats.sort()

previous = seats[0] - 1 # mock the seat before the first so the first one is valid

for seat in seats:
    if seat != previous + 1:
        print(previous + 1)
        break
    previous = seat
