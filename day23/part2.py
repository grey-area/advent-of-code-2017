# The assembly program in 'input' computes the number of composite
# numbers in the sequence 107900, 107917, 107934, ..., 124900

b = 107900
c = 124900

primes = []
for n in range(2, int(c**0.5) + 1):
    if all([n % p > 0 for p in primes]):
        primes.append(n)

h = 0
for n in range(b, c + 1, 17):
    if any([n % p == 0 for p in primes]):
        h += 1

print(h)
