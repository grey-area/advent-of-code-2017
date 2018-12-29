from collections import defaultdict

dirs = ['n', 'ne', 'se', 's', 'sw', 'nw']

with open('input') as f:
    step_list = [dirs.index(d) for d in f.read().strip().split(',')]

def compute_reduction(step_list):
    steps = defaultdict(int)

    dists = []

    for step in step_list:
        opposite = (step + 3) % 6
        plus1 = (step + 1) % 6
        plus2 = (step + 2) % 6
        minus1 = (step - 1) % 6
        minus2 = (step - 2) % 6
        if steps[opposite] > 1:
            steps[opposite] -= 1
        elif steps[plus2] > 0:
            steps[plus2] -= 1
            steps[plus1] += 1
        elif steps[minus2] > 0:
            steps[minus2] -= 1
            steps[minus1] += 1
        else:
            steps[step] += 1

        dists.append(sum(steps.values()))

    return max(dists)

ans = compute_reduction(step_list)
print(ans)
