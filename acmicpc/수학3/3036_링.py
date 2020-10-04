import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
c = list(map(int, input().split()))
for i in range(1, len(c)):
    g = gcd(c[0], c[i])
    print('{0}/{1}'.format(c[0]//g, c[i]//g))