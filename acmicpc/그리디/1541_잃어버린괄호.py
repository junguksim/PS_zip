import sys
input = sys.stdin.readline
import re

s = input()
ops = re.findall("[+-]", s)
numbers = list(map(int, re.findall("\d+", s)))

idx = 0
while idx < len(ops):
    if ops[idx] == "+":
        ops.pop(idx)
        numbers[idx] += numbers[idx+1]
        numbers.pop(idx+1)
    else:
        idx += 1
idx = 0
while ops:
    ops.pop(idx)
    numbers[idx] -= numbers[idx+1]
    numbers.pop(idx+1)
print(numbers[0])
