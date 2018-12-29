import re
from collections import namedtuple

class Machine():
    def __init__(self, filename):
        with open(filename) as f:
            text = f.read()

        state_and_steps, *state_text = text.split('\n\n')

        self.states = {}
        State = namedtuple('State', ['write', 'move', 'next_state'])

        moves = {'left': -1, 'right': 1}
        state_re_str = 'value is ([0-1]):\n.+value ([0-1]).\n.+(left|right).\n.+state ([A-Z])'

        for state_str in state_text:
            head, *state_strs = state_str.split('If')
            state_name = re.search('state ([A-Z])', head).groups()[0]

            options = [None, None]

            for state_str in state_strs:
                val, write, direction, next_state = re.search(state_re_str, state_str).groups()
                state = State(int(write), moves[direction], next_state)
                options[int(val)] = state

            self.states[state_name] = options

        self.state, steps = re.search('state ([A-Z]).\n.+ (\d+) steps', state_and_steps).groups()
        self.steps = int(steps)

        self.tape = [0]
        self.cursor = 0

    def step(self):
        write, move, self.state = self.states[self.state][self.tape[self.cursor]]
        self.tape[self.cursor] = write
        self.cursor += move
        if self.cursor >= len(self.tape):
            self.tape += [0] * len(self.tape)
        elif self.cursor < 0:
            self.cursor += len(self.tape)
            self.tape = [0] * len(self.tape) + self.tape
