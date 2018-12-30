import numpy as np
from itertools import product

def array_from_str(string):
    return np.array([[c=='#' for c in row] for row in string.split('/')], dtype=np.bool)

def print_grid(grid):
    ans = ''
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            if grid[i, j]:
                ans += '#'
            else:
                ans += '.'
        ans += '\n'
    print(ans)

def load_rules():
    with open('input') as f:
        rule_strs = f.read().splitlines()

    rules = {}

    for rule_str in rule_strs:
        lhstr, rhstr = rule_str.split(' => ')
        lhs = array_from_str(lhstr)
        rhs = array_from_str(rhstr)
        for k in range(4):
            lhs1 = np.rot90(lhs, k=k)
            rules[lhs1.tobytes()] = rhs
            rules[np.flipud(lhs1).tobytes()] = rhs
            rules[np.fliplr(lhs1).tobytes()] = rhs

    return rules

def update(grid, rules):
    d = 3
    if grid.shape[0] % 2 == 0:
        d = 2
    N = grid.shape[0] // d

    rows = []

    for i in range(N):
        cells = []
        for j in range(N):
            grid_portion = grid[d*i:d*(i+1), d*j:d*(j+1)]
            cell = rules[grid_portion.tobytes()]
            cells.append(cell)
        rows.append(np.concatenate(cells, axis=1))

    return np.concatenate(rows, axis=0)


if __name__ == '__main__':

    rules = load_rules()

    grid = np.array([[False, True, False],
                     [False, False, True],
                     [True, True, True]], dtype=np.bool)

    for i in range(5):
        grid = update(grid, rules)

    print(np.sum(grid))
