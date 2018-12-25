class Firewall():
    def __init__(self, f_range):
        self.f_range = f_range
        self.i = 0
        self.sign = 1

    def step(self):
        self.i += self.sign
        if self.i == 0 or self.i == self.f_range - 1:
            self.sign *= -1

with open('input') as f:
    data = f.read().splitlines()

firewalls = {}
for line in data:
    depth, f_range = [int(i) for i in line.split(': ')]
    firewalls[depth] = Firewall(f_range)
max_depth = depth

severity = 0
for depth in range(max_depth + 1):
    if depth in firewalls.keys():
        firewall = firewalls[depth]
        if firewall.i == 0:
            severity += depth * firewall.f_range
    for firewall in firewalls.values():
        firewall.step()

print(severity)
