def solution(absolutes, signs):
    answer = 0
    for i, v in enumerate(absolutes) :
        if signs[i] == True :
            answer += v
        else :
            answer -= v
    
    return answer

    absolutes = [4,7,12]
    signs = [true,false,true]

    print(solution(absolutes, signs))