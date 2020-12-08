#!/usr/bin/env python3
import logging

log = logging.getLogger(__name__)


class MachineLoopException(Exception):
    """
    Gets raised when the machine looped,
    in order to answer question 1
    """

    pass


class Machine:
    """
    Machine that executes instructions according to the spec of
    Advent of Code 2020, day 8, part 1
    """

    pointer: int
    accumulator: int
    program: list[tuple[str, int]]

    already_executed: set

    def __init__(self, program):
        self.program = program
        self.pointer = 0
        self.accumulator = 0
        self.already_executed = set()

    def accumulate(self, value):
        """
        Machine instruction to add to the accumulator
        """
        log.debug(f"Accumulating {value}")
        self.accumulator += value
        return True
        
    def jump(self, value):
        """
        Machine instruction to move the pointer by value
        """
        log.debug(
            f"Jumping from step {self.pointer} to {self.pointer + value - 1}"
        )
        self.pointer += value - 1
        return True

    def halt(self, _):
        """
        Machine instruction to halt
        (not part of spec, specific to this implementation)
        """
        log.debug("Halting execution")
        return False

    def nop(self, _):
        """
        Machine instruction to do nothing
        """
        log.debug("Doing nothing")
        return True
        
    def step(self):
        """
        Execute the next program instruction
        """
        log.debug(f"Executing step {self.pointer}")
        if self.pointer in self.already_executed:
            raise MachineLoopException()

        instr, arg = self.program[self.pointer]

        instructions = {
            "jmp": self.jump,
            "acc": self.accumulate,
            "hlt": self.halt,
            "nop": self.nop,
        }

        self.already_executed.add(self.pointer)
        self.pointer += 1

        if self.pointer >= len(self.program):
            log.debug("End of program reached")
            return False

        log.debug(f"Advancing to step {self.pointer}")
        return instructions[instr](arg)

    def run(self):
        """
        Run the program until it halts or raises an exception
        """
        run = True
        while run:
            run = self.step()
