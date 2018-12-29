state_length = 1
value_after_0 = 0
index = 0
step = 303

for value in range(1, 50000000, 1):
    index = (index + step) % state_length + 1
    state_length += 1
    if index == 1:
        value_after_0 = value

print(value_after_0)
