with open('input') as f:
    data = f.read().splitlines()

infected = set()

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == '#':
            infected.add((x, y))

x = y = (len(data) - 1) // 2
dx = 0
dy = -1

count = 0
for i in range(10000):
    is_infected = (x, y) in infected
    if is_infected:
        turn_sign = -1
        infected.remove((x, y))
    else:
        turn_sign = 1
        infected.add((x, y))
        count += 1
    if abs(dy) > 0:
        sign = turn_sign
    else:
        sign = -1 * turn_sign
    dx, dy = sign * dy, sign * dx
    x += dx
    y += dy

print(count)
