import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
arr = sorted(list(map(int, input().split(" "))))
graph = {}
for i in range(len(arr)):
    try:
        graph[arr[i]] += 1
    except:
        graph[arr[i]] = 1
M = int(input())
targets = list(map(int, input().split(" ")))

for i in range(M):
    try:
        print(graph[targets[i]], end=" ")
    except:
        print(0, end=" ")
