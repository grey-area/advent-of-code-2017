import numpy as np

lower_16 = 0xffff
A = 699
B = 124
A_mul = 16807
B_mul = 48271
div = 2**31 - 1

judge_As = []
judge_Bs = []
N = 5000000

while len(judge_As) < N:
    A = (A * A_mul) % div
    if A % 4 == 0:
        judge_As.append(A & lower_16)

while len(judge_Bs) < N:
    B = (B * B_mul) % div
    if B % 8 == 0:
        judge_Bs.append(B & lower_16)

print(np.sum(np.array(judge_As) == np.array(judge_Bs)))
