from collections import defaultdict
from collections import namedtuple
import operator
from functools import partial

Instruction = namedtuple('Instruction', ['op', 'args'])

class Machine():
    def __init__(self, filename):
        self.registers = defaultdict(int)
        self.load_program(filename)
        self.ip = 0
        self.frequency = None
        self.received = None

    def cast(self, X):
        try:
            return int(X)
        except ValueError:
            return self.registers[X]

    def generic_inst(self, op, X, Y):
        self.registers[X] = op(self.registers[X], self.cast(Y))

    def jgz(self, X, Y):
        if self.cast(X) > 0:
            self.ip += self.cast(Y) - 1

    def set(self, X, Y):
        self.registers[X] = self.cast(Y)

    def snd(self, X):
        self.frequency = self.registers[X]

    def rcv(self, X):
        if self.registers[X] != 0:
            self.received = self.frequency

    def load_program(self, filename):
        ops = {}
        self.program = []

        for opname, op in zip(['add', 'mul', 'mod'],
                              [operator.add, operator.mul, operator.mod]):
            ops[opname] = partial(self.generic_inst, op)
        ops['jgz'] = self.jgz
        ops['set'] = self.set
        ops['snd'] = self.snd
        ops['rcv'] = self.rcv

        with open(filename) as f:
            text = f.read().splitlines()

        for line in text:
            op_str, *args = line.split(' ')
            self.program.append(Instruction(ops[op_str], args))

    def step(self):
        op, args = self.program[self.ip]
        op(*args)
        self.ip += 1
