import numpy as np

data = np.loadtxt('input', dtype=np.int64)

print(np.sum(np.max(data, axis=1) - np.min(data, axis=1)))
