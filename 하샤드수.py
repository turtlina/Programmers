def solution(x):
    s = 0
    for v in str(x) :
        s += int(v)
    
    if x%s == 0 :
        return True
    else :
        return False