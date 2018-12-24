import re
from collections import Counter
import sys


class Program():
    def __init__(self, name, weight):
        self.name = name
        self.weight = int(weight)
        self.children = []

    def compute_weight(self):
        if len(self.children) == 0:
            return self.weight
        else:
            child_weights = [child.compute_weight() for child in self.children]
            weight_counts = Counter(child_weights)
            standard_weight = max(weight_counts, key=weight_counts.get)
            wrong_weight = min(weight_counts, key=weight_counts.get)
            if standard_weight != wrong_weight:
                offset = standard_weight - wrong_weight
                child_to_correct = child_weights.index(wrong_weight)
                print(self.children[child_to_correct].weight + offset)
                sys.exit()

            return self.weight + sum(child_weights)

re_str = '(\S+) \((\d+)\)'
with open('input') as f:
    data = f.read().splitlines()

dependencies = {}
programs = {}

for line in data:
    line = line.split(' -> ')
    if len(line) == 1:
        line.append(None)
    lhs, rhs = line

    name, weight = re.search(re_str, lhs).groups()
    depends = set()
    if rhs is not None:
        depends = set(rhs.split(', '))
    dependencies[name] = depends
    programs[name] = Program(name, weight)

all_dependencies = set.union(*dependencies.values())
for name, program in programs.items():
    if name not in all_dependencies:
        root = program

    depends = dependencies[name]
    for child_name in depends:
        program.children.append(programs[child_name])

root.compute_weight()
