import math

def compute_coords(index):
    next_sqrt = 2 * math.ceil(0.5 * (index**0.5 - 1)) + 1
    next_bottom_right = (next_sqrt - 1) // 2
    coords = [next_bottom_right, next_bottom_right]

    diff = next_sqrt**2 - index

    for sign in [-1, 1]:
        for j in [0, 1]:
            delta = min(diff, next_sqrt-1)
            coords[j] += sign * delta
            diff -= delta

    return coords

value = 277678
x, y = compute_coords(value)
print(abs(x) + abs(y))
