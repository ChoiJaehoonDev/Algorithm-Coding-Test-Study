import sys

input = sys.stdin.readline

n = int(input())
mt = list(input().split(' '))

for i, j in zip(mt, mt[1:]):
    if i == j:
        print('NO')
        exit()
    elif i < j or j > i:
        continue
print('YES')