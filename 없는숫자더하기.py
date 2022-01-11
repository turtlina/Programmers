def solution(numbers):
    answer = 0
     
    for i in range(0,10) :
        if not i in numbers :
            answer = answer + i
            
    return answer

numbers = [1,2,3,4,6,7,8,0]

print(solution(numbers))
