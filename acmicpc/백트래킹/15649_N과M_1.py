import sys
input = sys.stdin.readline
from itertools import permutations

inputLine = list(map(int,input().split(' ')))
N = inputLine[0]
M = inputLine[1]
arr = []
combis = []

for i in range(1, N+1):
    arr.append(i)
combis = (list(permutations(arr, M)))
for c in combis:
    s = ""
    for c_ in c:
        s += str(c_)  + " "
    print(s)