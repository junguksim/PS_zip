import sys
def input(): return sys.stdin.readline().strip()

T = int(input())
for _ in range(T):
    N = int(input())
    points = []
    passes = []
    for _ in range(N):
        points.append(list(map(int, input().split(" "))))
    points.sort(key=(lambda x : x[0]))
    for i in range(len(points)):
        if len(passes) == 0 or points[i][1] < passes[-1][1]:
            passes.append(points[i])
    print(len(passes))