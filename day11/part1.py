from collections import Counter

with open('input') as f:
    steps = Counter(f.read().strip().split(','))

dirs = ['n', 'ne', 'se', 's', 'sw', 'nw']
opposites = [(dirs[i], dirs[i + 3]) for i in range(3)]
reduction_triples = [(dirs[i], dirs[(i + 2)%6], dirs[(i + 1)%6]) for i in range(6)]

for dir1, dir2 in opposites:
    reduction = min(steps[dir1], steps[dir2])
    steps[dir1] -= reduction
    steps[dir2] -= reduction

for dir1, dir2, dir3 in reduction_triples:
    reduction = min(steps[dir1], steps[dir2])
    steps[dir1] -= reduction
    steps[dir2] -= reduction
    steps[dir3] += reduction

print(sum(steps.values()))
