def solution(numbers, hand):
    answer = ''
    
    d = {}
    d[1] = (0,3)
    d[2] = (1,3)
    d[3] = (2,3)
    d[4] = (0,2)
    d[5] = (1,2)
    d[6] = (2,2)
    d[7] = (0,1)
    d[8] = (1,1)
    d[9] = (2,1)
    d['*'] = (0,0)
    d[0] = (1,0)
    d['#'] = (2,0)
    
    left = (0,0)
    right = (2,0)
    
    for v in numbers :
        if v == 1 or v == 4 or v == 7 :
            answer = answer + 'L'
            left = d[v]
        elif v == 3 or v == 6 or v == 9 :
            answer = answer + 'R'
            right = d[v]
        else :
            dleft = abs(d[v][0]-left[0])+abs(d[v][1]-left[1])
            dright = abs(d[v][0]-right[0])+abs(d[v][1]-right[1])
        
            if dleft < dright :
                answer = answer + 'L'
                left = d[v]
            elif dleft > dright :
                answer = answer + 'R'
                right = d[v]
            else :
                if hand == 'left' :
                    answer = answer + 'L'
                    left = d[v]
                elif hand == 'right' :
                    answer = answer + 'R'
                    right = d[v]
    return answer