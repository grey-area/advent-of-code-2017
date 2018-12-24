import numpy as np

data = np.loadtxt('input', dtype=np.int32)
i = 0
steps = 0

while i < data.size and i >= 0:
    jump = data[i]
    data[i] += 1
    i += jump
    steps += 1

print(steps)
