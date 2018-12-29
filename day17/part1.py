from collections import deque

state = deque([0])
step = 303

for value in range(1, 2018, 1):
    state.rotate(-(step + 1))
    state.appendleft(value)

print(state[1])
