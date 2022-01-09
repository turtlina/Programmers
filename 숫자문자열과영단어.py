def solution(s):
    a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        
    for i, v in enumerate(a) :
        s = s.replace(v,str(i))

    return int(s)

s = "one4seveneight"

print(solution(s))