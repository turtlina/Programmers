def solution(id_list, report, k):
    answer = []
    
    #신고 중복 제거
    tmp_set = set(report)
    report = list(tmp_set)

    # K이상 신고를 받은 사람
    p_list = []
    dic={}
    for v in report :
        tmp = v.split(" ")
        if tmp[1] in dic :
            dic[tmp[1]] += 1            
        else :
            dic[tmp[1]] = 1
    
    for key, val in dic.items() :
        if val >= k :
            p_list.append(key)

    #신고자의 신고횟수
    dic2={}
    for v in report :
        tmp = v.split(" ")

        if tmp[1] in p_list :
            if tmp[0] in dic2 :
                dic2[tmp[0]] += 1
            else :
                dic2[tmp[0]] = 1

    for v in id_list:
        if v in dic2 :
            answer.append(dic2[v])
        else :
            answer.append(0)

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))