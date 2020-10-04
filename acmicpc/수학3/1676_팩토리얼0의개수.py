import sys
input = sys.stdin.readline
from math import factorial

N = int(input())
if N == 0 or N == 1:
    print(0)
else:
    count = 0
    fact = list(reversed(list(str(factorial(N)))))
    for i in fact:
        if i == "0":
            count += 1
        else:
            print(count)
            break