# def solution(relation):
#     answer = 0
#     columns = [[] for i in range(len(relation[0]))]
#     idxList = []
#     for row in relation:
#         for idx, column in enumerate(row):
#             columns[idx].append(column)
#     for i in range(len(columns)):
#         if(len(set(columns[i])) == len(columns[i])):
#             answer += 1
#             idxList.append(i)
#     for i in range(len(columns)-1):
#         print(idxList, i)
#         if i in idxList:
#             continue
#         temp = list(map(lambda x: [x], columns[i]))
#         for j in range(i+1, len(columns)):
#             if j in idxList:
#                 continue
#             for k in range(len(columns[j])):
#                 temp[k].append(columns[j][k])
#             filteredTemp = list(set([tuple(t) for t in temp]))
#             print(temp, filteredTemp)
#             if(len(temp) == len(filteredTemp)):
#                 answer += 1
#                 idxList.append(i)
#                 break;
#     print(idxList)
#     #print(columns)
#     return answer
from itertools import combinations
def solution(relation):
    def checkCandidate(colLst, rows):
        tmp = [tuple([item[idx] for idx in colLst]) for item in relation]
        if len(set(tmp)) != rows:
            return False
        else:
            return True
    rows = len(relation)
    cols = len(relation[0])
    colLst = range(cols)
    lst = []
    for leng in range(1, cols+1):
        comb = combinations(colLst, leng)
        for n1 in list(comb):
            if checkCandidate(n1, rows):
                lst.append(set(n1))
    for el1 in lst[:]:
        for el2 in lst[:]:
            if el1 == el1 & el2:
                if el1 != el2:
                    lst.remove(el2)
    return len(lst)
print(solution([["a", "aa"], ["aa", "a"], ['a', 'a']]))
