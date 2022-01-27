def solution(arr1, arr2):
    answer = arr1
    ll=len(arr1)
    ll2 = len(arr1[0])
    for i in range(ll) :
        for j in range(ll2) :
            answer[i][j] = arr1[i][j] + arr2[i][j]
    
    return answer