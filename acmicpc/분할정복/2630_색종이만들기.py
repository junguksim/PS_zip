import sys
input = sys.stdin.readline

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
white, blue = 0, 0
def quad(x,y,n):
    global matrix, blue, white
    num = matrix[y][x]

    for i in range(x, x+n):
        for j in range(y, y + n):
            if matrix[j][i] != num:
                quad(x,y, n//2)
                quad(x+ n//2, y, n//2)
                quad(x, y + n // 2, n // 2)
                quad(x + n // 2, y + n // 2, n // 2)
                return

    if num == 0:
        white += 1
        return
    else:
        blue += 1
        return

quad(0,0,N)
print(white)
print(blue)