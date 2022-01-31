def solution(n):
    tmp_list = []
    
    for v in str(n) :
        tmp_list.append(v)
    
    tmp_list.sort(reverse=True)
    
    answer = ''
    
    for v in tmp_list :
        answer += str(v)
        
    return int(answer)