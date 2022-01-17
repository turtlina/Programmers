def solution(a, b):
    answer = 0
    for i, v in enumerate(b) :
        answer += a[i]*v
    
    return answer