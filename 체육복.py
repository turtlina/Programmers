def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)
    
    for v in new_lost :
        if v+1 in new_reserve or v-1 in new_reserve :
            if v+1 not in new_reserve :
                new_reserve.remove(v-1)
            elif v-1 not in new_reserve :
                new_reserve.remove(v+1)
        else :
            n -= 1
            
    return n