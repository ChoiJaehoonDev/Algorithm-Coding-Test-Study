def solution(record):
    answer = []
    name = {}
    log = []

    for rcd in record:
        r = rcd.split(' ')
        if r[0] == "Enter":
            name[r[1]] = r[2]
            log.append([r[1], r[0]])
        elif r[0] == "Leave":
            log.append([r[1], r[0]])
        else:
            name[r[1]] = r[2]

    for l in log:
        if l[1] == "Enter":
            answer.append(name[l[0]] + '님이 들어왔습니다.')
        else:
            answer.append(name[l[0]] + '님이 나갔습니다.')

    return answer