def preorder(graph):
    visited = []
    return 1

def solution(nodeinfo):
    answer = [[]]
    graph = {}
    for i in range(1, len(nodeinfo) + 1):
        graph[i] = [tuple(nodeinfo[i-1])]
    print(graph)
    sortByYGraph = sorted(graph.items(), key=(lambda x: x[1][0][1]), reverse=True)
    print(sortByYGraph)
    yStack = []
    for i in range(len(sortByYGraph)-1):
        node = sortByYGraph[i][0]
        pos = sortByYGraph[i][1][0]
        idx = i+1
        while pos[1] != sortByYGraph[idx][1][0][1]
    return answer

print(solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]))