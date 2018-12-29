from collections import Counter

with open('input') as f:
    steps = Counter(f.read().strip().split(','))

dirs = ['n', 'ne', 'se', 's', 'sw', 'nw']
opposites = [(dirs[i], dirs[i + 3]) for i in range(3)]

for dir1, dir2 in opposites:
    reduction = min(steps[dir1], steps[dir2])
    steps[dir1] -= reduction
    steps[dir2] -= reduction

for i in range(6):
    dir1 = dirs[i]
    dir2 = dirs[(i + 2) % 6]
    dir3 = dirs[(i + 1) % 6]
    reduction = min(steps[dir1], steps[dir2])
    steps[dir1] -= reduction
    steps[dir2] -= reduction
    steps[dir3] += reduction

print(sum(steps.values()))
