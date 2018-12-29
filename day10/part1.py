import numpy as np

lengths = np.loadtxt('input', delimiter=',', dtype=np.int32)
data = np.arange(256, dtype=np.int32)

index = 0
skip = 0
total_offset = 0

for length in lengths:
    data = np.concatenate((np.flip(data[:length], 0), data[length:]))
    offset = length + skip
    total_offset += offset
    data = np.roll(data, shift=-offset)
    skip += 1

data = np.roll(data, shift=(total_offset % len(data)))
print(data[0] * data[1])
