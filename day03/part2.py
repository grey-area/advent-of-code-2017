import math
import numpy as np

def compute_coords(index, offset=0):
    next_sqrt = 2 * math.ceil(0.5 * (index**0.5 - 1)) + 1
    next_bottom_right = (next_sqrt - 1) // 2
    coords = [next_bottom_right, next_bottom_right]

    diff = next_sqrt**2 - index

    for sign in [-1, 1]:
        for j in [0, 1]:
            delta = min(diff, next_sqrt-1)
            coords[j] += sign * delta
            diff -= delta

    return coords[0] + offset, coords[1] + offset

value = 277678
bottom_right = math.ceil(0.5 * (value**0.5 - 1)) + 1
grid_size = 2 * bottom_right + 1

grid = np.zeros((grid_size, grid_size), dtype=np.int64)
x, y = compute_coords(1, offset=bottom_right)
grid[x, y] = 1
for i in range(1, value + 1, 1):
    x, y = compute_coords(i, offset=bottom_right)
    grid[x, y] = np.sum(grid[x-1:x+2, y-1:y+2])
    if grid[x, y] > value:
        break

print(grid[x, y])
