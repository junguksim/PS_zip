import sys
def input(): return sys.stdin.readline().strip()

dp = [-1 for i in range(1001)]
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3 #세로 1개 나올 때 경우의 수 * 2 + 세로만 1
dp[4] = 5 # 세로만 1 + 가로만 1 + 세로 1개 불가능 0 + 세로 2개 일때 3 = 5

def tile(n):
    if n <= 2:
        return n
    elif dp[n] != -1:
        return dp[n]
    else:
        dp[n] = tile(n-1) + tile(n-2)
        return dp[n]

print(tile(int(input())) % 10007)