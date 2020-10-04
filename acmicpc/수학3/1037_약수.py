import sys
input = sys.stdin.readline
from math import gcd

n = int(input())
line = list(map(int, input().split()))
print(max(line)*min(line))