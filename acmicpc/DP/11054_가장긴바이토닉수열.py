import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split(" ")))


for i in range(N):
    LBS = []
    isAsc = True
    for j in range(i+1, N):
        if isAsc:
            if len(LBS) == 0 or LBS[-1] < arr[j]:
                LBS.append(arr[j])
                continue
            lb = -1
            for cpIdx, cpVal in enumerate(LBS):
                if arr[j] <= cpVal:
                    lb = cpIdx
                    break
            LBS[lb] = arr[j]
    print(LBS)

print(arr)