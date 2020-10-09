import sys
input = lambda : sys.stdin.readline().strip()
import re
from collections import deque

T = int(input())
for _ in range(T):
    p = input()
    p = p.replace("RR", "")
    n = int(input())
    arr = input()[1:-1].split(',')
    
    r = 0
    f, b = 0, 0
    for j in p:
        if j == "R":
            r += 1
        else:
            if r % 2 == 0:
                f += 1
            else:
                b += 1
    
    if f + b <= n:
        arr = arr[f:n-b]
        if r % 2 == 1:
            print("[" + ','.join(arr[::-1]) + "]")
        else:
            print("[" + ",".join(arr) + "]")
    else:
        print("error")