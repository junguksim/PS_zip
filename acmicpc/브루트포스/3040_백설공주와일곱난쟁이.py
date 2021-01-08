import sys
def input(): return sys.stdin.readline().strip()
from itertools import combinations

arr = []
for _ in range(9):
    arr.append(int(input()))

combis = list(combinations(arr, 7))
for i in range(len(combis)):
    if sum(combis[i]) == 100:
        for j in range(len(combis[i])):
            print(combis[i][j])
        break