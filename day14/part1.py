from knot import knot_hash

key = 'ljoxqyyw'
count = 0

for i in range(128):
    row_key = f'{key}-{i}'
    row_hex = knot_hash(row_key)
    count += bin(int(row_hex, 16)).count('1')

print(count)
