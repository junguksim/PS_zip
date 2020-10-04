import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
answer = []
s = []
d = 0
for i in range(n):
    s.append(int(input()))
    if i == 1:
        d = abs(s[1]-s[0])
    d = gcd(abs(s[i]-s[i-1]), d)
d_a = int(d ** 0.5)
for i in range(2, d_a+1):
    if d % i == 0:
        answer.append(i)
        answer.append(d // i)
answer.append(d)
answer = list(set(answer))
answer.sort()
for i in answer:
    print(i, end=' ')