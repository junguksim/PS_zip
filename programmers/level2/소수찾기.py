from itertools import permutations

def isPrime(n):
    if n > 1:
        for f in range(2, n):
            if(n % f == 0):
                return False
    else:
        return False
    return True

def solution(numbers):
    answer = 0
    pems = []
    for i in range(1, len(numbers)+1):
        temp = permutations(numbers,i)
        for j in temp:
            pems.append(int(''.join(j)))
    pems = list(set(pems))
    answer = len(pems)
    for i in pems:
        if(not isPrime(i)):
            answer -= 1
    return answer

print(solution("0123456"))