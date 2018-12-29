from knot import knot_hash
import numpy as np

key = 'ljoxqyyw'

grid = np.zeros((128, 128), dtype=np.int32)
component_id = 1

for i in range(128):
    row_key = f'{key}-{i}'
    row_hex = knot_hash(row_key)
    row = f'{int(row_hex, 16):0128b}'
    for j in range(len(row)):
        if row[j] == '1':
            grid[i, j] = component_id

            if j > 0 and grid[i, j-1] > 0 and grid[i, j-1] != component_id:
                grid[grid == grid[i, j-1]] = component_id
            if i > 0 and grid[i - 1, j] > 0 and grid[i-1, j] != component_id:
                grid[grid == grid[i-1, j]] = component_id

            component_id += 1

print(np.unique(grid).size - 1)
