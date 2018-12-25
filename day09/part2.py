with open('input') as f:
    text = f.read()

garbage_start = None
skip = False
cancelled = 0
total = 0

for c_i, c in enumerate(text):
    if skip:
        skip = False
        continue

    if garbage_start is None and c == '<':
        garbage_start = c_i
    else:
        if c == '!':
            skip = True
            cancelled += 2
        elif c == '>':
            total += c_i - garbage_start - cancelled - 1
            garbage_start = None
            cancelled = 0

print(total)
