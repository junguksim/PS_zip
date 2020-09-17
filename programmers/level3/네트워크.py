def DFS(graph):
    networks = []
    for i in graph:
        stack = [i]
        visited = []
        while stack:
            current = stack.pop(-1)
            if current not in visited:
                visited.append(current)
                if current in graph:
                    temp = list(set(graph[current]) - set(visited))
                    temp = sorted(temp,reverse=True)
                    stack += temp
        networks.append(visited)
    return networks

def solution(n, computers):
    graph = {}
    for c in range(len(computers)):
        graph[c] = []
        for m in range(len(computers[c])):
            if(computers[c][m] == 1 and c != m):
                graph[c].append(m)
    res = list(set([tuple(set(item)) for item in DFS(graph)]))
    return len(res)

#print(solution(5, [[1, 1, 0, 1, 0], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [1, 0, 0, 1, 0], [0,0,0,0,1]]))
print(solution(5, [[1,1,0,0,0], [1,1,0,0,0], [0,0,1,1,0], [0,0,1,1,0], [0,0,0,0,1]]))