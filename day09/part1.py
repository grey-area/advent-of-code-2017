with open('input') as f:
    text = f.read()

depth = 0
garbage = False
total = 0
skip = False

for c in text:
    if skip:
        skip = False
        continue

    if not garbage:
        if c == '{':
            depth += 1
            total += depth
        elif c == '}':
            depth -= 1
        elif c == '<':
            garbage = True
    else:
        if c == '!':
            skip = True
        elif c == '>':
            garbage = False

print(total)
