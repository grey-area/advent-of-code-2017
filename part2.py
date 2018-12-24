with open('input') as f:
    data = f.read().strip()

L = len(data)
print(sum(int(data[i]) for i in range(L) if data[i] == data[(i + L//2) % L]))
