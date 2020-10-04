import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    nums = list(map(int,input().split(' ')))
    arr.append(tuple(nums))
answer = sorted(arr, key=(lambda x: (x[1], x[0])))
for a in answer:
    print(f"{a[0]} {a[1]}")