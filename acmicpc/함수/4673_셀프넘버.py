def d(n):
    nums = list(map(int, str(n)))
    return n + sum(nums)

arr = [-1 for i in range(1, 11000)]
for i in range(1, 10001):
    arr[d(i)] = 1

for j in range(1, 10001):
    if arr[j] == -1:
        print(j)