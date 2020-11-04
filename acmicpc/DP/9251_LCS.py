import sys
s1 = sys.stdin.readline().strip().upper()
s2 = sys.stdin.readline().strip().upper()
len1, len2 = len(s1), len(s2)
dp = [[0]*(len2+1) for _ in range(len1 + 1)]
for i in range(1, len1 + 1):
    for j in range(1, len2 + 1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])