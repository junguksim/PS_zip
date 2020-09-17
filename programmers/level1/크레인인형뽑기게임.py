def solution(board, moves):
    answer = 0
    stack = []
    newBoard = [[] for row in range(len(board[0]))]
    for line in reversed(board):
        for i in range(len(line)):
            newBoard[i].append(line[i])
    print(newBoard)
    for pos in moves:
        line = newBoard[pos-1]
        i = -1
        while(line[i] == 0 and abs(i) != len(line)):
            i -=1
        if(line[i] == 0):
            continue
        if(len(stack) > 0):
            if(stack[-1] == line[i]):
                answer += 2
                stack.pop(-1)
                line[i] = 0
                print(stack, answer)
                continue
        stack.append(line[i])
        print(stack, answer)
        line[i] = 0
    return answer

print(solution(	[[0, 0, 2, 2, 1], [0, 0, 1, 5, 3], [1, 2, 5, 0, 1], [4, 2, 5, 4, 2], [3, 5, 3, 3, 1]], [1, 2, 5, 4, 3, 2, 1, 5, 4]))