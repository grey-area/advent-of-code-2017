from collections import defaultdict

registers = defaultdict(int)

with open('input') as f:
    inst_strs = f.read().splitlines()

for inst_str in inst_strs:
    result_str, condition_str = inst_str.split(' if ')

    reg_name, *remainder = condition_str.split(' ')
    condition = str(registers[reg_name]) + ' ' + ' '.join(remainder)
    if eval(condition):
        reg_name, op, val = result_str.split(' ')

        if op == 'inc':
            registers[reg_name] += int(val)
        else:
            registers[reg_name] -= int(val)

print(max(registers.values()))
