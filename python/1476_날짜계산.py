import sys

def date_cal(E, S, M):
    while True:
        if E == S == M:
            return E
        else:
            if min(E, S, M) == E:
                E += 15
            elif min(E, S, M) == S:
                S += 28
            elif min(E, S, M) == M:
                M += 19

E, S, M = map(int, sys.stdin.readline().split())

print(date_cal(E,S, M))