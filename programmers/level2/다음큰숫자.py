def solution(n):
    strN = str(format(n, 'b'))
    count = strN.count('1')
    cp = 0
    while cp != count:
        n += 1
        strN = str(format(n, 'b'))
        cp = strN.count('1')
    return n

print(solution(15))