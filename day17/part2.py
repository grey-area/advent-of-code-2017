from collections import deque

state = deque([0])
step = 303

for value in range(1, 50000000, 1):
    state.rotate(-(step + 1))
    state.appendleft(value)

print(state[state.index(0) + 1])
