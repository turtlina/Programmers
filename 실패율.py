def solution(N, stages):
    answer = []
    stages.sort()
    tmp=0
    dict = {}

    for i in range(1, N+1) :
        if stages.count(i) == 0 :
            dict[i] = 0
        else :
            dict[i] = stages.count(i)/(len(stages)-tmp)
        tmp += stages.count(i)
        
    for i in sorted(dict.items(), key=lambda x : x[1], reverse=True) :
        answer.append(i[0])

    return answer



N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

print(solution(N, stages))