import sys



n = int(sys.stdin.readline())
cnt = 0

for _ in range(n):
    check = {}
    pre = ''
    c = 0
    word = sys.stdin.readline()
    for w in word:
        # 이 전 단어와 지금 단어가 같으면 pass
        # 다른데 이미 존재하면 break
        # 다른데 존재하지 않으면 pre를 초기화, check 갱신
        if pre is w:
            pass
        else:
            if w in check.keys():
                break
            else:
                pre = w
                check[w] = True
        c += 1
    cnt += (c // len(word))

print(cnt)