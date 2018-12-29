from collections import defaultdict
from collections import namedtuple
from collections import deque
import operator
from functools import partial

Instruction = namedtuple('Instruction', ['op', 'args'])

class Machine():
    def __init__(self, filename, id_):
        self.registers = defaultdict(int)
        self.load_program(filename)
        self.registers['p'] = id_
        self.ip = 0
        self.buffer = deque([])
        self.other_machine = None
        self.waiting = False
        self.terminated = False
        self.send_count = 0

    def set_other_machine(self, other):
        self.other_machine = other

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
        if self.ip < 0 or self.ip >= len(self.program):
            self.terminated = True

    def set(self, X, Y):
        self.registers[X] = self.cast(Y)

    def snd(self, X):
        self.other_machine.buffer.append(self.registers[X])
        self.other_machine.waiting = False
        self.send_count += 1

    def rcv(self, X):
        if len(self.buffer) > 0:
            self.registers[X] = self.buffer.popleft()
        else:
            self.ip -= 1
            self.waiting = True
            if self.other_machine.waiting:
                self.terminated = True
                self.other_machine.terminated = True

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
