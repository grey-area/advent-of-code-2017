with open('input') as f:
    data = f.read().splitlines()

HORIZONTAL = 0
VERTICAL = 1

y = 0
x = data[0].index('|')

orientation = VERTICAL
direction = 1

letters_seen = ''
steps = 0

while True:
    if orientation == VERTICAL:
        y += direction
    else:
        x += direction

    steps += 1
    c = data[y][x]

    if c == ' ':
        break

    if c.isalpha():
        letters_seen += c

    if c == '+':
        if orientation == VERTICAL:
            orientation = HORIZONTAL
            for delta in [-1, 1]:
                if data[y][x + delta] != ' ':
                    direction = delta
                    break
        else:
            orientation = VERTICAL
            for delta in [-1, 1]:
                if data[y + delta][x] != ' ':
                    direction = delta
                    break

print(f'Letters seen: {letters_seen}')
print(f'{steps} steps taken')
