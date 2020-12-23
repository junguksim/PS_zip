import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
dp = [-1 for i in range(N+1)]
dp[0] = 0
dp[1] = 1


def getPinaryNumber(N):
    if N <= 1:
        return N
    elif dp[N] == -1:
        dp[N] = getPinaryNumber(N-1) + getPinaryNumber(N-2)
        return dp[N]
    else:
        return dp[N]


def main():
    print(getPinaryNumber(N))
    return


main()
