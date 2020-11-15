import sys
def input(): return sys.stdin.readline().strip()


def isGroup(s):
    s = list(s)
    arr = []
    for i in range(len(s)):
        if s[i] not in arr:
            arr.append(s[i])
        elif arr[-1] != s[i]:
            return False
    return True


answer = 0
n = int(input())
for _ in range(n):
    s = input()
    if isGroup(s):
        answer += 1
print(answer)
