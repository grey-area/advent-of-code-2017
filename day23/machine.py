from collections import defaultdict
from collections import namedtuple
from collections import deque
import operator
from functools import partial

Instruction = namedtuple('Instruction', ['op', 'args'])

class Machine():
    def __init__(self, filename):
        self.registers = defaultdict(int)
        self.load_program(filename)
        self.ip = 0
        self.terminated = False
        self.mul_called = 0

    def cast(self, X):
        try:
            return int(X)
        except ValueError:
            return self.registers[X]

    def sub(self, X, Y):
        self.registers[X] = self.registers[X] - self.cast(Y)

    def mul(self, X, Y):
        self.registers[X] = self.registers[X] * self.cast(Y)
        self.mul_called += 1

    def jnz(self, X, Y):
        if self.cast(X) != 0:
            self.ip += self.cast(Y) - 1

    def set(self, X, Y):
        self.registers[X] = self.cast(Y)

    def load_program(self, filename):
        ops = {}
        self.program = []

        ops['jnz'] = self.jnz
        ops['set'] = self.set
        ops['sub'] = self.sub
        ops['mul'] = self.mul

        with open(filename) as f:
            text = f.read().splitlines()

        for line in text:
            op_str, *args = line.split(' ')
            self.program.append(Instruction(ops[op_str], args))

    def step(self):
        op, args = self.program[self.ip]
        op(*args)
        self.ip += 1

        if self.ip < 0 or self.ip >= len(self.program):
            self.terminated = True
