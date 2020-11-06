import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
arr = sorted(list(map(int, input().split(" "))))

M = int(input())
targets = list(map(int, input().split(" ")))


def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1
    mid = (start + end) // 2

    print(f"target = {target} arr = {arr}")
    while(end - start >= 0):
        center = arr[mid]
        if(center == target):
            return 1
        elif center < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) // 2
    return 0


for i in range(M):
    print(binarySearch(arr, targets[i]))
