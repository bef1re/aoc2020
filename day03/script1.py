#!/usr/bin/env python3
"""

/*
 * Me: I really want to code in c
 * Mom: We have c at home
 * C at home:
 */

"""
linelength = 31
readsize = linelength + 3

t = 0
with open("input.txt", "r") as f:
    c = '.'
    while c != '':
        c = f.read(1)
        if c == '\n':
            print()
            c = f.read(1)

        print("X", end='')
        if c == '#':
            t += 1

        i = 0
        while i < readsize:
            i += 1
            c = f.read(1)
            print(c, end='')
            if c == '\n':
                if i <= readsize - linelength:
                    i += linelength

print(t)
