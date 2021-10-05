import sys

input = sys.stdin.readline

n = int(input())
board = []
cnt = 0
size = []
max_size = 0
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))

dr = [[0,1],[0,-1],[1,0],[-1,0]]

def dfs(y,x):
    global board, size, max_size

    for dy, dx in dr:
        ny, nx = y+ dy, x + dx
        if 0 <= ny < n and 0 <= nx < n:
            if board[ny][nx] == 1:
                board[ny][nx] = -1
                max_size += 1
                dfs(ny, nx)

    return True

for y in range(n):
    for x in range(n):
        if board[y][x] == 1:
            max_size = 0
            if dfs(y, x):
                cnt += 1
                size.append(max_size)

print(cnt)
print(sorted(size))

