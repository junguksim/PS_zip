def solution(n):
    answer = 1
    val = 0
    start = 1
    now = 1
    while now < n:
        while val + start <= n:
            print(val, start)
            val += start
            start += 1
        if val == n:
            answer += 1
        start = now + 1
        now += 1
        val = 0
        print(answer)
    return answer

print(solution(15))