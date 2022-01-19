def solution(d, budget):
    d.sort()

    answer = 0 
    for v in d :
        budget -= v
        if budget < 0 :
            break
        answer += 1
    return answer

d=[2,2,3,3]	
budget=10

print(solution(d, budget))