import sys

n = int(sys.stdin.readline())

customSet = []

for _ in range(n):
    line = sys.stdin.readline().split()
    if line[0] == 'add':
        if int(line[1]) not in customSet:
            customSet.append(int(line[1]))
    elif line[0] == 'remove':
        if int(line[1]) in customSet:
            customSet.remove(int(line[1]))
    elif line[0] == 'check':
        if int(line[1]) in customSet:
            print(1)
        else:
            print(0) 
    elif line[0] == 'toggle':
        if int(line[1]) not in customSet:
            customSet.append(int(line[1]))
        else:
            customSet.remove(int(line[1]))
    elif line[0] == 'all':
        customSet = [x for x in range(1, 21)]
    elif line[0] == 'empty':
        customSet = []
