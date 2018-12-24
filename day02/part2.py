import numpy as np
from itertools import product

data = np.loadtxt('input', dtype=np.int64)

total = 0
for i in range(data.shape[0]):
    for j1, j2 in product(range(data.shape[1]), repeat=2):
        if j1 == j2:
            continue
        if data[i, j1] % data[i, j2] == 0:
            total += data[i, j1] // data[i, j2]

print(total)
