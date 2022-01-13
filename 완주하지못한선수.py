def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i, c in enumerate(completion) :
        if participant[i] != completion[i] :
            return participant[i]
    
    return participant[-1]



participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]


print(solution(participant, completion))