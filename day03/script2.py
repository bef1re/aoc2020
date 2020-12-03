#!/usr/bin/env python3
"""

Honey it's not what it looks like! I can explain this.

"""

linelength = 31

def run(rightsteps, downsteps):
    readsize = linelength + rightsteps

    t = 0
    with open("input.txt", "r") as f:
        c = 'F'
        while c != '':
            nls = 0

            # support downsteps
            if c != 'F' and downsteps > 1:
                print(f.read((downsteps - 1) * linelength + 1), end='')

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

    return t

print(run(1, 1) * run(3, 1) * run(5, 1) * run(7, 1) * run(1, 2))
