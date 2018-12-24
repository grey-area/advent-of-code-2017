from collections import Counter

with open('input') as f:
    data = f.read().splitlines()

valid_count = 0

for line in data:
    if max(Counter(''.join(sorted(phrase)) for phrase in line.split(' ')).values()) == 1:
        valid_count += 1

print(valid_count)
