with open('input') as f:
    data = [int(i) for i in f.read().splitlines()]

# Note: may take some time (~1 minute) to run,
# but will be significantly faster using pypy

i = 0
steps = 0

while i < len(data) and i >= 0:
    jump = data[i]
    if jump >= 3:
        data[i] -= 1
    else:
        data[i] += 1
    i += jump
    steps += 1

print(steps)
