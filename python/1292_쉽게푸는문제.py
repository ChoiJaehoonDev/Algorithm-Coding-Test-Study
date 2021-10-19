import sys

s,e  = map(int, sys.stdin.readline().split())

i = 1
cnt = 1
arr = []

while len(arr) <= e:
    for _ in range(i):
        arr.append(i)
    i += 1

print(sum(arr[s-1:e]))

