# import sys
# input = sys.stdin.readline

# N = int(input())

# def VPS(s):
#     stack = []
#     for i in s:
#         if i == "(":
#             stack.append(i)
#         else:
#             if not stack:
#                 return "NO"
#             else:
#                 stack.pop()
#     if not stack:
#         return "YES"
#     else:
#         return "NO"

# lines = []
# for _ in range(N):
#     line = input()
#     lines.append(line)

# for line in lines:
#     print(VPS(line))

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')