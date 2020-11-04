import sys
input = sys.stdin.readline

n = int(input())
lines = []
dp = [0 for i in range(n)]

for _ in range(n):
    lines.append(list(map(int, input().split(' '))))

lines.sort(key=(lambda x: x[0]))
b = []
for i in range(n):
    b.append(lines[i][1])
for i in range(n):
    for j in range(i):
        if b[i] > b[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(n - max(dp))