def solution(genres, plays):
    answer = []
    
    dic1={} #key:장르     #value:해당장르총재생횟수
    dic2={} #key:장르     #value:장르별 인기곡2개
    dic3={} #key:노래고유번호#value:재생횟수
    
    for i, v in enumerate(plays):
        dic3[i] = v
        
    for i, g in enumerate(genres) :
        #장르 최초 선택
        if not g in dic1 :
            dic1[g] = plays[i]
            dic2[g] = [i] 
        #장르 저장된 적 있음
        else :
            dic1[g] += plays[i]
            
            #저장 한번만 됐을 때
            if len(dic2[g]) == 1 :
                dic2[g] = [dic2[g][0],i]
            
            #저장 두번 이상 
            if plays[i] > dic3[dic2[g][1]] :
                dic2[g] = [dic2[g][0],i]
            
            if dic3[dic2[g][0]] < dic3[dic2[g][1]] :
                dic2[g] = [dic2[g][1],dic2[g][0]]
            
            else :
                if dic2[g][0] > dic2[g][1] :
                    dic2[g] = [dic2[g][1],dic2[g][0]]
                else :
                    dic2[g] = [dic2[g][0],dic2[g][1]]
            
    for key, value in sorted(dic1.items(), key=lambda x:x[1], reverse=True) :
        if len(dic2[key]) == 1 :
            answer.append(dic2[key][0])
        else :
            answer.append(dic2[key][0])
            answer.append(dic2[key][1])
            
    return answer

genres = [['classic', 'pop', 'classic', 'classic', 'pop', 'balad']]
plays = [[500, 600, 150, 800, 2500, 4000]]

print(solution(genres[0], plays[0]))

#case0: [4, 1, 3, 0]
