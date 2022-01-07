def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0

    for v in lottos :
        if v in win_nums :
            cnt += 1
        elif v == 0 :
            zero += 1
    max = cnt+zero

    if max >= 6 :
        answer.append(1)
    elif max == 5 :
        answer.append(2)
    elif max == 4 :
        answer.append(3)
    elif max == 3 :
        answer.append(4)
    elif max == 2 :
        answer.append(5)
    else :
        answer.append(6)


    if cnt >= 6 :
        answer.append(1)
    elif cnt == 5 :
        answer.append(2)
    elif cnt == 4 :
        answer.append(3)
    elif cnt == 3 :
        answer.append(4)
    elif cnt == 2 :
        answer.append(5)
    else :
        answer.append(6)

    return answer
lottos = [44, 1, 0, 0, 31, 25]
win_nums = 	[31, 10, 45, 1, 6, 19]

print(solution(lottos, win_nums))
