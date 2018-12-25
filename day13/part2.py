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
while True:
    caught = False
    for f in firewalls:
        caught = (f.depth + offset) % f.period == 0
        if caught:
            break
    if not caught:
        break
    offset += 1

print(offset)
