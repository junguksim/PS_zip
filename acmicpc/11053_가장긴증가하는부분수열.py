import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
LIS = []

for idx, val in enumerate(arr):
    if(idx == 0 or LIS[-1] < val):
        LIS.append(val)
        continue
    lb = -1
    for cpIdx,cpVal in enumerate(LIS):
        if(val <= cpVal):
            lb = cpIdx
            break
    LIS[lb] = val
print(len(LIS))

