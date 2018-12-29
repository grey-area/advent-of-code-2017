import numpy as np

def knot_hash(text):
    lengths = [ord(c) for c in text] + [17, 31, 73, 47, 23]
    data = np.arange(256, dtype=np.int32)

    index = 0
    skip = 0
    total_offset = 0

    for r in range(64):
        for length in lengths:
            data = np.concatenate((np.flip(data[:length], 0), data[length:]))
            offset = (length + skip) % len(data)
            total_offset += offset
            data = np.roll(data, shift=-offset)
            skip += 1

    data = np.roll(data, shift=(total_offset % len(data)))
    ans = ''

    for i in range(16):
        block_result = np.bitwise_xor.reduce(data[i * 16:(i + 1) * 16])
        ans += f'{block_result:02x}'

    return ans
