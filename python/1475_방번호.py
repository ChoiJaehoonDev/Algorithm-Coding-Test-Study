import sys
from math import ceil
N = sys.stdin.readline()
pn = 0

check = {}

for n in N:
    if n == '6' or n == '9':
        n = '6'
        if n not in check.keys():
            check[n] = 0.5
        else:
            check[n] += 0.5

    else:
        if n not in check.keys():
            check[n] = 1
        else:
            check[n] += 1

print(ceil(max(check.values())))