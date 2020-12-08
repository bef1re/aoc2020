#!/usr/bin/env python3
import logging

from machine import Machine, MachineLoopException

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    log = logging.getLogger(__name__)

    log.info("Reading program")
    with open("input.txt", "r") as f:
        program = []

        for line in f:
            instr, arg = line.strip().split()
            program.append((instr, int(arg)))

    for i in range(len(program)):
        patched_program = program.copy()
        instr, arg = patched_program[i]

        if instr == "jmp":
            patched_program[i] = ("nop", arg)
        elif instr == "nop":
            patched_program[i] = ("jmp", arg)
        else:
            continue

        log.info(f"Initializing machine with instr {i} modified")
        machine = Machine(patched_program)

        log.info("Starting machine")

        try:
            machine.run()
            log.info("The machine halted cleanly")
            print(f"The current accumulator value is {machine.accumulator}")
            break
        except MachineLoopException:
            log.warning("The machine looped")
