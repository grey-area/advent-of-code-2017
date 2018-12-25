from collections import namedtuple

Firewall = namedtuple('Firewall', ['depth', 'f_range', 'period'])

with open('input') as f:
    data = f.read().splitlines()

firewalls = []
for line in data:
    depth, f_range = [int(i) for i in line.split(': ')]
    period = (f_range - 1) * 2
    firewalls.append(Firewall(depth, f_range, period))

offset = 0
while sum((f.depth + offset) % f.period == 0 for f in firewalls) > 0:
    offset += 1

print(offset)
