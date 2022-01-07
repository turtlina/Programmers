def solution(record):
    answer = []
    dic = {}

    for s in record :
        str = s.split(" ")
        if str[0] == "Enter" or str[0] == "Change" :
            dic[str[1]] = str[2]
    
    for s in record :
        str = s.split(" ")
        name = dic[str[1]]

        if str[0] == "Enter" :
            answer.append(name+"님이 들어왔습니다.")
        elif str[0] == "Leave" :
            answer.append(name+"님이 나갔습니다.")
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

print(solution(record))
