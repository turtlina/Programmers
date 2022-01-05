def solution(new_id):
    answer = ''
    
    #1단계 대문자를 소문자로 바꾸기
    new_id = new_id.lower()

    #2단계 특수문자 제거
    for i, v in enumerate(new_id) :
        if v == '-' or v == '_' or v == '.' :
            answer = answer + v
        elif v.isalnum() :
            answer = answer + v

    #3단계 마침표가 2개 이상 연속되면 하나로 바꿈..
    tmpli = []
    tmpli = answer.split('.')

    answer = ''
    for v in tmpli :
        if v == '' :
            continue
        else : 
            answer = answer + '.' + v

    #4단계 마침표가 맨 처음이나 끝에 위차한다면 제거
    if len(answer) > 0 :
        if answer[0] == '.' :
            answer = answer[1:]
        if answer[-1] == '.' :
            answer = answer[:len(answer)]

    #5단계 빈 문자열이라면 'a'대입
    if answer == "" :
        answer='a'

    #6단계 16자 이상이면 첫15개문자만 
    if len(answer) >= 16 : 
        answer = answer[:15]

    #7단계 new_id 길이가 2자 이하면 마지막 문자를 3될때까지 반복
    if len(answer) < 3 :
        while(len(answer)<3):
            answer = answer + answer[-1]

    #4단계 다시
    if answer[0] == '.' :
        answer = answer[1:]
    if answer[-1] == '.' :
        answer = answer[:len(answer)-1]

    return answer


new_id = "...!@BaT#*..y.abcdefghijklm"

print(solution(new_id))

#case0: [4, 1, 3, 0]
