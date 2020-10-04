import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
for i in range(1, len(arr)):
    arr[i] += arr[i-1]
print(sum(arr))