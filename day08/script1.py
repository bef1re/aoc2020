#!/usr/bin/env python3
import logging
from machine import Machine, MachineLoopException

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger(__name__)

    log.info("Reading program")
    with open("input.txt", "r") as f:
        program = []

        for line in f:
            instr, arg = line.strip().split()
            program.append((instr, int(arg)))

    log.info("Initializing machine")
    machine = Machine(program)

    log.info("Starting machine")
    try:
        machine.run()
        log.info("The machine halted cleanly")
    except MachineLoopException:
        log.warning("The machine looped")

    print(f"The current accumulator value is {machine.accumulator}")
