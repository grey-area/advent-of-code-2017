with open('input') as f:
    data = f.read().splitlines()

# Used a dictionary of cell coordinates instead of a grid
# because I couldn't be bothered handling grid resizing

status = {}

CLEAN = 0
WEAK = 1
INFECTED = 2
FLAGGED = 3

chars = '.W#F'

def print_grid(status, x1, y1):
    grid_str = ''
    for y in range(-3, 5, 1):
        for x in range(-3, 6, 1):

            if x == x1 and y == y1:
                prev_chr = '['
                next_chr = ']'
            else:
                prev_chr = ' '
                next_chr = ' '

            if (x, y) not in status.keys():
                grid_str += prev_chr + '.' + next_chr
            else:
                grid_str += prev_chr + chars[status[(x, y)]] + next_chr
        grid_str += '\n'
    print(grid_str)

for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == '#':
            status[(x, y)] = INFECTED

x = y = (len(data) - 1) // 2
dx = 0
dy = -1
turning = True

count = 0
for i in range(10000000):
    if (x, y) in status.keys():
        cell_status = status[(x, y)]
    else:
        cell_status = CLEAN

    if cell_status == CLEAN:
        turn_sign = 1
        turning = True
    elif cell_status == WEAK:
        turn_sign = 1
        turning = False
        count += 1
    elif cell_status == INFECTED:
        turn_sign = -1
        turning = True
    elif cell_status == FLAGGED:
        turn_sign = -1
        turning = False

    if cell_status == CLEAN:
        status[(x, y)] = WEAK
    else:
        status[(x, y)] += 1
        if status[(x, y)] > FLAGGED:
            del(status[(x, y)])

    if turning:
        if abs(dy) > 0:
            sign = turn_sign
        else:
            sign = -1 * turn_sign
        dx, dy = sign * dy, sign * dx
    else:
        dx, dy = turn_sign * dx, turn_sign * dy
    x += dx
    y += dy

print(count)
