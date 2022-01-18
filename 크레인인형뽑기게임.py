def solution(board, moves):
    answer = 0
    stack = []

    for m in moves :
        for i, v in enumerate(board) :
            #크레인이 0을 만남
            if v[m-1] == 0 :
                continue
            #크레인이 숫자를 만남
            else :
                if len(stack) > 0 and v[m-1] == stack[-1] :
                    stack.pop()
                    answer += 1
                    board[i][m-1] = 0
                    break

                stack.append(v[m-1])
                board[i][m-1] = 0
                break
                
    return answer*2


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]


print(solution(board, moves))