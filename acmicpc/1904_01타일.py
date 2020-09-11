import sys
input = sys.stdin.readline

n = int(input())
memo = [0] * 1000001
memo[1] = 1
memo[2] = 2

for k in range(3, n+1):
    memo[k] = (memo[k-1]+memo[k-2]) % 15746
print(memo[n])