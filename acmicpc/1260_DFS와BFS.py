import sys
from collections import deque
input = sys.stdin.readline

def BFS(graph, root):
    visited = []
    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current not in visited:
            visited.append(current)
            if current in graph:
                temp = list(set(graph[current]) - set(visited))
                temp.sort()
                queue += temp
    return " ".join(str(i) for i in visited)
def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        current = stack.pop(-1)
        if current not in visited:
            visited.append(current)
            if current in graph:
                temp = list(set(graph[current]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

n = input().split(" ")
node, edge, start = [int(i) for i in n]
graph = {}
for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph, start))
print(BFS(graph, start))