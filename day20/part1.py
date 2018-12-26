import re

with open('input') as f:
    data = f.read().splitlines()

min_accel_i = 0
min_accel = float('inf')

for line_i, line in enumerate(data):
    x, y, z, vx, vy, vz, ax, ay, az = [int(i) for i in re.findall('(-?\d+)', line)]

    accel = abs(ax) + abs(ay) + abs(az)
    if accel < min_accel:
        min_accel = accel
        min_accel_i = line_i

print(min_accel_i)
