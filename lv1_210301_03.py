def solution(board, moves):
    '''board = 2차원 배열, moves는 1차원 배열'''
    stack = []
    score = 0
    
    for idx1, move in enumerate(moves):
        for idx2, can in enumerate(board):
            if can[move-1] == 0:
                continue
            else:
                if len(stack) == 0:
                    stack.append(can[move-1])
                    can[move-1] = 0
                    break
                if stack[-1] == can[move-1]:
                    stack.pop()
                    score += 2
                else:
                    stack.append(can[move-1])
                can[move-1] = 0
                break

    return score


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4])