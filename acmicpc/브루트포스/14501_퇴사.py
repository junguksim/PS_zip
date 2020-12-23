import sys
def input(): return sys.stdin.readline().strip()

N = int(input())
works = []

for _ in range(N):
    works.append(list(map(int, input().split(" "))))
values = list(map(lambda x : x[1], works))
answer = 0
for i in range(N):
    if i +works[i][0] > N:
        values[i] = 0
        continue
    t = values[i]
    for j in range(i + works[i][0], N):
        if t + works[j][1] > values[j]:
            values[j] = t + works[j][1]
    
print(max(values))