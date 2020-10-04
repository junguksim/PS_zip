import sys
input = sys.stdin.readline

N = int(input())
stack = []
lines = []
for _ in range(N):
    line = input().split()
    lines.append(line)

for line in lines:
    if line[0] == "push":
        stack.append(int(line[1]))
    elif line[0] == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif line[0] == "size":
        print(len(stack))
    elif line[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(-1))