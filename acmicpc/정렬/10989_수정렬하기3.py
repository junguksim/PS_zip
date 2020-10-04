import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * (N+1)

for i in range(N+1):
    num = int(input())
    arr[num] += 1

for i in range(N+1):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)
