def solution(numbers):
    answer = []
    
    for i, v in enumerate(numbers) :
        for j in range(i,len(numbers)-1) :
            if not (numbers[i] + numbers[j+1]) in answer :
                answer.append(numbers[i] + numbers[j+1])
    
    answer.sort()
            
    return answer

numbers =	[2,1,3,4,1]

print(solution(numbers))