from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque([])
def op(line):
    line = line.split()
    s = line[0]
    if s == "push":
        queue.append(line[1])
    elif s == "pop":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.popleft())
    elif s == "size":
        print(len(queue))
    elif s == "empty":
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif s == "front":
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])

for _ in range(n):
    op(input())