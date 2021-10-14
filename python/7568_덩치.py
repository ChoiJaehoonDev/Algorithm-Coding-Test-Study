import sys
from collections import deque

n = int(sys.stdin.readline())
rank = []
body = []

#5
#55 185
#58 183
#88 186
#60 175
#46 155
# 덩치가 더 크면 appendleft
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    body.append([x,y])

for w1,h1 in body:
    score = 1
    for w2, h2 in body:
        if w1 < w2 and h1 < h2:
            score += 1
    rank.append(score)

for r in rank:
    print(r, end=' ')