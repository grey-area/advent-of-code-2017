import re

with open('input') as f:
    text = f.read()

blocks = [int(i) for i  in re.findall('\d+', text)]
N = len(blocks)
indices = list(range(N))

seen = {}
steps = 0

while True:
    blocks_tuple = tuple(blocks)
    if blocks_tuple in seen.keys():
        print(steps - seen[blocks_tuple])
        break
    else:
        seen[blocks_tuple] = steps

    index = max(indices, key=lambda i: blocks[i])
    redist = blocks[index]
    blocks[index] = 0
    while redist > 0:
        index = (index + 1) % N
        blocks[index] += 1
        redist -= 1

    steps += 1
