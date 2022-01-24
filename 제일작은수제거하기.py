def solution(arr):
    answer = []
    min_num = min(arr)
    
    for v in arr :
        if v == min_num :
            continue
        else :
            answer.append(v)
            
    if len(answer) == 0 :
        answer.append(-1)
        
    return answer