def solution(records):
    answer = []
    name = {}
    chats = []

    for record in records:
        r = record.split(' ')
        if r[0] == 'Enter':
            name[r[1]] = r[2]
            chats.append([r[1], r[0]])
        elif r[0] == 'Leave':
            chats.append([r[1], r[0]])
        elif r[0] == 'Change':
            name[r[1]] = r[2]

    for chat in chats:
        if chat[1] == 'Enter':
            answer.append(name[chat[0]] + "님이 들어왔습니다.")
        elif chat[1] == 'Leave':
            answer.append(name[chat[0]] + "님이 나갔습니다.")

    return answer