def solution(lottos, win_nums):
    answer = []
    min_correct = 0
    max_correct = 0
    
    # 6 - 1 5 - 2 4 - 3 3 -4 2 - 5 1 -6 0 - 6
    
    for lotto in lottos:
        if lotto == 0:
            max_correct += 1
        elif lotto in win_nums:
            max_correct += 1
            min_correct += 1
    
    if max_correct <= 1:
        answer.append(6)
    elif max_correct > 1:
        answer.append(7-max_correct)
        
    if min_correct <= 1:
        answer.append(6)
    elif min_correct > 1:
        answer.append(7-min_correct)
        
        
    
    return answer