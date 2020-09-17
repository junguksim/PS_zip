def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    answer = ''
    start = 0
    arr = []
    while(len(answer) < t):
        num = convert(start, n)
        num = str(num)
        for i in num:
            arr.append(i)
        print(arr)
        start += 1
        if(p-1 >= len(arr)):
            continue
        answer += arr[p-1]
        p += m
        
    return answer

print(solution(16,16,2,1))