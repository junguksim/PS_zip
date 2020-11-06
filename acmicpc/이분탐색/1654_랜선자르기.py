import sys
def input(): return sys.stdin.readline().strip()


K, N = map(int, input().split(" "))
arr = []
for _ in range(K):
    arr.append(int(input()))
start = 1
end = max(arr)
mid = (start + end) // 2
result = 0

while start <= end:
    sums = list(map(lambda x: x // mid, arr))
    sumVal = sum(sums)
    if sumVal >= N:
        result = mid
        start = mid + 1
    else:
        end = mid - 1
    mid = (start + end) // 2
print(result)
