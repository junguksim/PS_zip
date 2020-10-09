import sys
input = sys.stdin.readline
from collections import deque

n,m = map(int, input().split())
wanted = deque(list(map(int, input().split())))
arr = deque([i for i in range(1, n+1)])

answer = 0
while wanted:
    if arr[0] == wanted[0]:
        arr.popleft()
        wanted.popleft()
    else:
        if len(arr) // 2 < arr.index(wanted[0]):
            arr.appendleft(arr.pop())
        else:
            arr.append(arr.popleft())
        answer += 1

print(answer)