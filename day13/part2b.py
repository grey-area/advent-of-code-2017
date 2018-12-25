import numpy as np
from collections import namedtuple

Firewall = namedtuple('Firewall', ['depth', 'f_range', 'period'])

with open('input') as f:
    data = f.read().splitlines()

firewalls = []
for line in data:
    depth, f_range = [int(i) for i in line.split(': ')]
    period = (f_range - 1) * 2
    firewalls.append(Firewall(depth, f_range, period))

def find_first_offset(start, end, firewalls):
    offsets = np.arange(start, end)
    for f in firewalls:
        offsets = offsets[(f.depth + offsets) % f.period > 0]
    if len(offsets) > 0:
        return offsets[0]
    else:
        return None

result = None
start = 0
end = 100
while result is None:
    result = find_first_offset(start, end, firewalls)
    start = end
    end = end * 2

print(result)
