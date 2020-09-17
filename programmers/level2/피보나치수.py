
def solution(n):
    arr = [0 for i in range(n+1)]
    arr[1] = 1
    for i in range(2, n+1):
        a[i] = (a[i-2] + a[i-1]) % 1234567
    return arr[n]

print(solution(100000))