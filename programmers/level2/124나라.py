def solution(n):
    arr = [-1,"1", "2", "4"]
    if(n <= 3):
        return arr[n]
    for i in range(4, n+1):
        mok = i // 3
        if(i % 3 == 0):
            arr.append(arr[mok-1]+"4")
        else:
            if(i % 3 == 1):
                arr.append(arr[mok]+"1")
            else:
                arr.append(arr[mok]+"2")
    return arr[-1]

print(solution(500000000))