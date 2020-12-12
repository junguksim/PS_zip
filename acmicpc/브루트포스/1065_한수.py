import sys
def input(): return sys.stdin.readline().strip()


def isHansu(n):
    listN = list(map(int, list(str(n))))
    if len(listN) <= 2:
        return True
    term = listN[0]-listN[1]
    for i in range(1, len(listN)-1):
        if listN[i] - listN[i+1] != term:
            return False
    return True


N = int(input())
answer = 0
for i in range(1, N+1):
    if isHansu(i):
        answer += 1
print(answer)
