import sys
input = sys.stdin.readline

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
coins = reversed(coins)
count = 0

for c in coins:
    if c > K:
        continue
    count += K // c
    K = K % c
    if K == 0:
        print(count)
        break
