import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    s = input()
    arr.append(s[:-1])
arr = list(set(arr))
answer = sorted(arr, key=(lambda x : (len(x), x)))
for s in answer:
    print(s)