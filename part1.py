with open('input') as f:
    data = f.read().strip()

print(sum(int(i) for i, j in zip(data, data[1:] + data[0]) if i==j))
