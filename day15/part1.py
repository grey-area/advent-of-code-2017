import numpy as np

lower_16 = 0xffff
A = 699
B = 124
A_mul = 16807
B_mul = 48271
div = 2**31 - 1

matches = 0

for i in range(40000000):
    A = (A * A_mul) % div
    B = (B * B_mul) % div
    judge_A = A & lower_16
    judge_B = B & lower_16
    matches += judge_A == judge_B

print(matches)
