from collections import deque
import sys
def input(): return sys.stdin.readline().strip()


M, N = map(int, input().split(" "))
matrix = []
done = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]
for i in range(N):
    line = list(map(int, input().split(" ")))
    for j in range(len(line)):
        if line[j] == 1:
            done.append((i, j))
        if line[j] == -1:
            check[i][j] = -1
    matrix.append(line)


q = deque(done)

while q:
    y, x = q.popleft()
    check[y][x] = True
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= ny < N and 0 <= nx < M:
            if matrix[ny][nx] == -1:
                check[ny][nx] = -1
            elif check[ny][nx] == False and matrix[ny][nx] == 0:
                q.append((ny, nx))
                dist[ny][nx] = dist[y][x] + 1
                check[ny][nx] = True
answer = 0
isBreak = False
for i in range(N):
    if isBreak:
        break
    for j in range(M):
        if check[i][j] == False:
            print(-1)
            isBreak = True
            break
        answer = max(answer, dist[i][j])

if not isBreak:
    print(answer)
