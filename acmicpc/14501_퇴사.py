import sys
input = sys.stdin.readline

n = int(input())
arr = []
values = []
for _ in range(n):
    arr.append(tuple(map(int, input().split(" "))))

print(arr)
for i in range(n):
    possible = i + arr[i][0] - 1
    if possible < n:
        value = arr[i][1]
    for j in range(i+1,n):
        if j <= possible:
            print(f"{i} : {j} 번째 아이템은 스킵. possible = {possible} value = {value}")
            continue
        possible += arr[j][0]
        if possible < n:
            value += arr[j][1]
    values.append(value)
print(values)
print(max(values))