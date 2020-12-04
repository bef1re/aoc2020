#!/usr/bin/env python3
import re

passportlines = []
passports = []
# requiredkeys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] # and cid is optional

def validate(passport):
    try:
        # simple checks first
        if (
                int(passport["byr"]) < 1920 or
                int(passport["byr"]) > 2002 or
                int(passport["iyr"]) < 2010 or
                int(passport["iyr"]) > 2020 or
                int(passport["eyr"]) < 2020 or
                int(passport["eyr"]) > 2030 or
                passport["ecl"] not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"] or
                not re.match("#[0-9a-f]{6}$", passport["hcl"]) or
                not re.match("[0-9]{9}$", passport["pid"])
            ):
            return False

        # height check
        height_unit = passport["hgt"][-2:]
        height = int(passport["hgt"][:-2])

        if height_unit == "cm":
            if height < 150 or height > 193:
                return False
            else:
                pass
                # print(f"allowing height {passport['hgt']}, unit is {height_unit}, value {height}")

        elif height_unit == "in":
            if height < 59 or height > 76:
                return False
            else:
                pass
                # print(f"allowing height {passport['hgt']}, unit is {height_unit}, value {height}")

        else:
            return False

    except (ValueError, KeyError):
        # anything not convertable to an int? Then it's invalid anyway
        # any field missing? Invalid too
        return False

    return True
    
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
    if validate(passport):
        total += 1
        keys = list(passport.keys())
        keys.sort()
        if "cid" in keys:
            keys.remove("cid")
        for key in keys:
            print(f"{key}: {passport[key]}\t", end='')
        print()

print(total)
