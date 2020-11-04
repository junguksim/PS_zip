import sys
input = sys.stdin.readline

n = int(input())
arr = [["*"] * n for _ in range(n)]
v = n
cnt = 0
def star(n):
    global arr
    idx = [i for i in range(n) if (i // 3 ** cnt_) % 3 == 1 ]
    for i in idx:
        for j in idx:
            arr[i][j] == " "


star(n)