import sys
input = sys.stdin.readline

n = int(input())
points = [0 for i in range(301)]
memo = [0 for i in range(301)]
for i in range(n):
    points[i] = int(input())
memo[0] = points[0]
memo[1] = points[0]+points[1]
memo[2] = max(points[1]+points[2], memo[0]+points[2])
for i in range(3, n):
    memo[i] = max(points[i] + memo[i-2], points[i] + points[i-1] + memo[i-3])
print(memo[n-1])