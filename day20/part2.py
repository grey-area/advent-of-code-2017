import re
from collections import Counter

with open('input') as f:
    data = f.read().splitlines()

class Particle():
    def __init__(self, x, y, z, vx, vy, vz, ax, ay, az):
        self.x = x
        self.y = y
        self.z = z
        self.vx = vx
        self.vy = vy
        self.vz = vz
        self.ax = ax
        self.ay = ay
        self.az = az
        self.removed = False

    def update(self):
        self.vx += self.ax
        self.vy += self.ay
        self.vz += self.az
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

        return (self.x, self.y, self.z)

particles = []

for line_i, line in enumerate(data):
    particles.append(Particle(*[int(i) for i in re.findall('(-?\d+)', line)]))

# TODO implement termination check: all pairs of remaining particles are moving away from each other
for i in range(1000):
    positions = [p.update() for p in particles]
    pos_count = Counter(positions)
    for p, pos in zip(particles, positions):
        if pos_count[pos] > 1:
            p.removed = True
    particles = [p for p in particles if not p.removed]

print(len(particles))
