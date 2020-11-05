import sys
def input(): return sys.stdin.readline().strip()


T = int(input())


def DFS(matrix, x, y, M, N):
    stack = [[y, x]]
    while len(stack) > 0:
        [py, px] = stack.pop()
        matrix[py][px] = 0
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(4):
            n_x = px + dx[i]
            n_y = py + dy[i]
            if(n_x >= 0 and n_x < M and n_y >= 0 and n_y < N):
                if matrix[n_y][n_x] == 1:
                    stack.append([n_y, n_x])
    return 1


for _ in range(T):
    [M, N, CABBAGE] = list(map(int, input().split(" ")))
    matrix = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(CABBAGE):
        [x, y] = list(map(int, input().split(" ")))
        matrix[y][x] = 1
    ans = 0
    for y in range(N):
        for x in range(M):
            if(matrix[y][x] == 1):
                ans += DFS(matrix, x, y, M, N)
    print(ans)
