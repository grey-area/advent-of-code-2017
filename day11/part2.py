from collections import Counter

with open('input') as f:
    step_list = f.read().strip().split(',')

dirs = ['n', 'ne', 'se', 's', 'sw', 'nw']
opposites = [(dirs[i], dirs[i + 3]) for i in range(3)]
reduction_triples = [(dirs[i], dirs[(i + 2)%6], dirs[(i + 1)%6]) for i in range(6)]

def compute_reduction(step_list):
    steps = Counter(step_list)

    for dir1, dir2 in opposites:
        reduction = min(steps[dir1], steps[dir2])
        steps[dir1] -= reduction
        steps[dir2] -= reduction

    for dir1, dir2, dir3 in reduction_triples:
        reduction = min(steps[dir1], steps[dir2])
        steps[dir1] -= reduction
        steps[dir2] -= reduction
        steps[dir3] += reduction

    return sum(steps.values())

dists = [compute_reduction(step_list[:i]) for i in range(1, len(step_list) + 1, 1)]

print(max(dists))
