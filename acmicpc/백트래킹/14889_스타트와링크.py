import sys
input = sys.stdin.readline
from itertools import combinations, permutations

N = int(input())
arr = []
res = float("inf")
for _ in range(N):
    arr.append(list(map(int, input().split())))
num_list = [i for i in range(N)]

for cand in combinations(num_list, N//2):
    start_member = list(cand)
    link_member = list(set(num_list) - set(cand))
    start_comb = list(combinations(start_member, 2))
    link_comb = list(combinations(link_member, 2))
    start_sum = 0
    for x,y in start_comb:
        start_sum += arr[x][y] + arr[y][x]
    link_sum = 0
    for x, y in link_comb:
        link_sum += (arr[x][y] + arr[y][x])
    res = min(res, abs(link_sum-start_sum))

print(res)