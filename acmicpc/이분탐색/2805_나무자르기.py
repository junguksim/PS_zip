import sys
def input(): return sys.stdin.readline().strip()


N, M = map(int, input().split(" "))
trees = list(map(int, input().split(" ")))

start = 1
end = max(trees)
result = 0
while start <= end:
    mid = (start + end) // 2
    afterCut = list(map(lambda x: (x - mid if x > mid else 0), trees))
    sumVal = sum(afterCut)
    if sumVal >= M:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)
