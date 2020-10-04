import sys
input = sys.stdin.readline
from itertools import permutations

N = int(input())
numbers = list(map(int, input().split(' ')))
opsCnts = list(map(int, input().split(' ')))
ops = []
results = []
for idx,cnt in enumerate(opsCnts):
    for i in range(cnt):
        if idx == 0:
            ops.append("+")
        elif idx == 1:
            ops.append("-")
        elif idx == 2:
            ops.append("*")
        else:
            ops.append("/")
opPerms = list(set(list(permutations(ops, len(ops)))))
for i in range(len(opPerms)):
    num = numbers[0]
    for j in range(len(opPerms[i])):
        if opPerms[i][j] == "+":
            num += numbers[j+1]
        elif opPerms[i][j] == "-":
            num -= numbers[j+1]
        elif opPerms[i][j] == "*":
            num *= numbers[j+1]
        else:
            if num < 0:
                num = -1 * (abs(num) // numbers[j+1])
            else:
                num = num // numbers[j+1]
    results.append(num)
print(max(results))
print(min(results))