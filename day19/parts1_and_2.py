with open('input') as f:
    data = f.read().splitlines()

# Initial position
x = data[0].index('|')
y = 0

# Initial velocity
dx = 0
dy = 1

letters_seen = ''
steps = 0

while data[y][x] != ' ':
    # Step forwards
    x += dx
    y += dy
    steps += 1

    # If we see a letter, add it to the sequence seen
    if data[y][x].isalpha():
        letters_seen += data[y][x]
    # If we're at a corner
    elif data[y][x] == '+':
        # Look for a direction we can step that isn't where we just came from
        for dx1, dy1 in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if data[y + dy1][x + dx1] != ' ' and not (dx1 == -dx and dy1 == -dy):
                dx = dx1
                dy = dy1
                break

print(f'Letters seen: {letters_seen}')
print(f'{steps} steps taken')
