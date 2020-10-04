def solution(triangle):
    for i in range(len(triangle)):
        triangle[i] += [0 for i in range(len(triangle) - len(triangle[i]))]
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if triangle[i][j] == 0:
                continue
            try:
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                else:
                    triangle[i][j] = max(triangle[i-1][j], triangle[i-1][j-1]) + triangle[i][j]
            except:
                continue
    return max(triangle[-1])

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
