def solution(phone_book):
    answer = True
    dic = {}

    for i in phone_book :
        dic[i] = 1
        
    for i in phone_book :
        tmp = ""
        for p in i :
            tmp += p
            if not tmp == i :
                if tmp in dic : 
                    return False

    return answer

phone_book = ["119", "97674223", "1195524421"]

print(solution(phone_book))