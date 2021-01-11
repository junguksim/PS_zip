import sys
def input(): return sys.stdin.readline().strip()
from itertools import combinations

N, S = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
answer = 0
for i in range(1, N+1):
    combis = list(map(list , combinations(arr, i)))
    for j in range(len(combis)):
        if sum(combis[j]) == S:
            answer += 1

print(answer)