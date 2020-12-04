#!/usr/bin/env python3

passportlines = []
passports = []
requiredkeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Convert passports into single line passports
with open("input.txt", "r") as f:
    current = []
    for line in f:
        if line == "\n":
            passportlines.append(" ".join(current))
            current = []
        else:
            current.append(line.strip())
    passportlines.append(" ".join(current))


# Read password lines into dicts
for passport in passportlines:
    fields = {}
    for part in passport.split():
        key, value = part.split(":", 1)
        fields[key] = value

    passports.append(fields)


# And now we're ready to do the actual checking
total = 0
for passport in passports:
    valid = True
    for key in requiredkeys:
        if key not in passport:
            valid = False
            print(f"Key {key} not found in {passport}")
            break

    if valid:
        total += 1

print(total)
