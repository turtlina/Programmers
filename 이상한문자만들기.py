def solution(s):
    answer = ''
    
    i=0
    for v in s :
        if v.isalpha() :
            if i%2 == 0 :
                answer += v.upper()
            else :
                answer += v.lower()
            i += 1
        else :
            answer += v
            i = 0
    return answer