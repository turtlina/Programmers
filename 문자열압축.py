def cutList(s,n):
    li = []
    li = [s[i:i+n] for i in range(0, len(s), n)]
    return [s[i:i+n] for i in range(0, len(s), n)]

def solution(s):
    answer = 0
    result = []
    
    if len(s) == 1 :
        return 1

    for i in range(1,int(len(s)/2)+1) :
        tmp = ""
        mem_str = ""
        mem_num = 1

        for v in cutList(s,i):
            if mem_str == v :
                if mem_num == 1 :
                    mem_num += 1
                    tmp = tmp + str(mem_num)
                else :
                    tmp = tmp[:(-1)*len(str(mem_num))]
                    mem_num += 1
                    tmp = tmp + str(mem_num)
                mem_str = v
            else :
                tmp = tmp + v
                mem_str = v
                mem_num = 1

        result.append(len(tmp))

    answer = min(result)  
    return answer

s = "xababcdcdababcdcd"

print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xababcdcdababcdcd"))
print(solution("aaaaaaabaaaaaaaa"))
