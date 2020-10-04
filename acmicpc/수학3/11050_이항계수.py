# import sys
# input = sys.stdin.readline
# from math import factorial

# n,k = map(int, input().split())
# print(int(factorial(n) / (factorial(k) * factorial(n-k))))

from math import factorial
n, k = map(int, input().split())
result = factorial(n) // (factorial(k) * factorial(n - k))
print(result % 10007)