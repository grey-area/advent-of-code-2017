import re

re_str = '(\S+) \((\d+)\)'
with open('input') as f:
    data = f.read().splitlines()

seen_dependencies = set()
names = []

for line in data:
    line = line.split(' -> ')
    if len(line) == 1:
        line.append(None)
    lhs, rhs = line

    name, weight = re.search(re_str, lhs).groups()
    depends = []
    if rhs is not None:
        depends = rhs.split(', ')
    seen_dependencies.update(depends)
    names.append(name)

for name in names:
    if name not in seen_dependencies:
        print(name)
        break
