import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
times = deque([])
check = [False] * N
time, count = (2 ** 31) - 1, 0
for _ in range(N):
    inputTime = list(map(int, input().split()))
    times.append(inputTime)
times = sorted(times, key=(lambda x: (x[1],x[0])))
count = 0
start_time = 0

for time in times:
    if time[0] >= start_time:
        start_time = time[1]
        count += 1

print(count)