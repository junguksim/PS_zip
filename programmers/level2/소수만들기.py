from itertools import combinations

def isPrime(n):
    if n != 1:
        for f in range(2, n):
            if n % f == 0:
                return False
    else:
        return False
    return True
def solution(nums):
    return len(list(filter(isPrime, list(map(sum, list(combinations(nums, 3)))))))

print(solution([1,2,3,4]))