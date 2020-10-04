import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
dq = deque([])
def op(line):
    if line[0] == "push_front":
        dq.appendleft(int(line[1]))
    elif line[0] == "push_back":
        dq.append(int(line[1]))
    elif line[0] == 'size':
        print(len(dq))
    elif line[0] == "empty":
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(dq) == 0:
            print(-1)
        elif line[0] == "pop_front":
            print(dq.popleft())
        elif line[0] == "pop_back":
            print(dq.pop())
        elif line[0] == "front":
            print(dq[0])
        else:
            print(dq[-1])
for _ in range(n):
    op(input().split())