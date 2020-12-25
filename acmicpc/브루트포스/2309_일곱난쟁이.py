import sys
def input(): return sys.stdin.readline().strip()
from itertools import combinations

def main():
    arr = []
    for _ in range(9):
        arr.append(int(input()))
    comb = list(map(list, combinations(arr, 7)))
    for i in range(len(comb)):
        if sum(comb[i]) == 100:
            comb[i].sort()
            for j in range(len(comb[i])):
                print(comb[i][j])
            break

main()