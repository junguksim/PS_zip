import sys
input = sys.stdin.readline
from collections import deque
import copy

def goLeft(deq, target):
    cnt = 0
    while deq[0] != target:
        deq.append(deq.popleft())
        cnt += 1
    deq.append(deq.popleft())
    cnt += 1
    deq.popleft()
    return [deq, cnt]

def goRight(deq, target):
    cnt = 0
    while deq[-1] != target:
        deq.appendleft(deq.pop())
        cnt += 1
    deq.appendleft(deq.pop())
    cnt += 1
    deq.popleft()
    return [deq, cnt]


n, m = map(int, input().split(" "))
arr = deque([i for i in range(1, n+1)])
cnt = 0
targets = list(map(int, input().split(" ")))
for t in targets:
    left = goLeft(copy.deepcopy(arr), t)
    right = goRight(copy.deepcopy(arr),t)
    at = arr.index(t)
    print(arr, t)
    if left[1] > right[1]:
        if right[1] < at:
            arr = right[0]
            cnt += right[1]
        else:
            for i in range(len(arr)):
                if arr[0] != t and arr[0] not in targets:
                    arr.popleft()
                else:
                    break
            arr.popleft()
    else:
        if left[1] < at:
            arr = left[0]
            cnt += left[1]
        else:
            for i in range(len(arr)):
                if arr[0] != t and arr[0] not in targets:
                    arr.popleft()
                else:
                    break
            arr.popleft()
print(cnt)