with open('input') as f:
    data = f.read()
insts = data.split(',')

def spin(programs, i):
    i = i % len(programs)
    return programs[-i:] + programs[:-i]

def swapi(programs, i, j):
    programs[i], programs[j] = programs[j], programs[i]
    return programs

def swapv(programs, x, y):
    i = programs.index(x)
    j = programs.index(y)
    return swapi(programs, i, j)

programs = list('abcdefghijklmnop')
initial_programs = programs.copy()
cycle_length = None

for gen in range(1000000000):
    if gen > 0 and cycle_length is None and programs == initial_programs:
        cycle_length = gen

    if cycle_length is not None and (1000000000 - gen) % cycle_length == 0:
        break

    for inst in insts:
        if inst[0] == 's':
            i = int(inst[1:])
            programs = spin(programs, i)
        elif inst[0] == 'x':
            i, j = inst[1:].split('/')
            programs = swapi(programs, int(i), int(j))
        elif inst[0] == 'p':
            programs = swapv(programs, inst[1], inst[3])

print(''.join(programs))
