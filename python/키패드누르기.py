import math

def solution(numbers, hand):
    answer = ''
    now = [10, 12]
    
    cord = {}
    x = 1
    for i in range(4):
        for j in range(3):
            cord[x] = [i,j]
            x += 1
    

    for number in numbers:
        if number == 0:
            number = 11
        if number == 1 or number == 4 or number == 7:
            answer += 'L'
            now[0] = number
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            now[1] = number
        else:
            l = abs(cord[number][0] - cord[now[0]][0]) + abs(cord[number][1] - cord[now[0]][1])
            r = abs(cord[number][0] - cord[now[1]][0]) + abs(cord[number][1] - cord[now[1]][1])
            if l < r:
                answer += 'L'
                now[0] = number
            elif l > r:
                answer += 'R'
                now[1] = number
            else:
                if hand == 'right':
                    answer += 'R'
                    now[1] = number
                else:
                    answer += 'L'
                    now[0] = number
    return answer