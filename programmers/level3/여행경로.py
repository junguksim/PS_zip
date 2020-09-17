def DFS(graph, tickets):
    cases = []
    for g in graph:
        stack = [g]
        visited = []
        while stack:
            print(graph)
            print(f"stack = {stack}")
            current = stack.pop(-1)
            graph[current].sort(reverse=True)
            for neighbor in graph[current]:
                stack.append(neighbor)
            if(len(graph[current]) > 0):
                graph[current].pop(-1)
                print(f"from {current} to {stack[-1]} able={[current, stack[-1]] in tickets}")
                if [current, stack[-1]] in tickets:
                    if(len(visited) == 0):
                        visited.append(current)
                        visited.append(stack[-1])
                    else:
                        visited.append(stack[-1])
            print(f"visited = {visited}")
            print("=======================")
        cases.append(visited)
    return cases

def solution(tickets):
    answer = []
    graph = {}
    for way in tickets:
        start = way[0]
        end = way[1]
        if start not in graph:
            graph[start] = [end]
        elif end not in graph[start]:
            graph[start].append(end)

        if end not in graph:
            graph[end] = [start]
        elif start not in graph[end]:
            graph[end].append(start)
    print(graph)
    answer = (DFS(graph, tickets))[0]
    return answer

print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))
#print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))