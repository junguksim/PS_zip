def findAble(words, s, length, idx):
    arr = []
    words = words[idx+1:]
    for i in range(len(words)):
        cnt = 0
        for j in range(len(words[i])):
            if(words[i][j] == s[j]):
                cnt += 1
        if(cnt == length - 1):
            arr.append(words[i])
    return arr
def DFS(graph, begin):
    cases = []
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
        cases.append(visited)
    cases = (sum(cases, []))
    return cases
def solution(begin, target, words):
    answer = 0
    length = len(begin)
    if target not in words:
        return 0
    graph = {begin : findAble(words, begin, length, -1)}
    for i in range(len(words)):
        graph[words[i]] = findAble(words, words[i], length, i)
    result = DFS(graph, begin)
    return result.index(target)

print(solution("hit", "hhh", ['hhh','hht']))