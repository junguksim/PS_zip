def solution(N, number):
    S = [0, {N}]
    for i in range(2,9):
        caseSet = {int(str(N) * i)}
        for iHalf in range(1, i//2 + 1):
            for x in S[iHalf]:
                for y in S[i-iHalf]:
                    caseSet.add(x+y)
                    caseSet.add(x-y)
                    caseSet.add(y-x) # y-x 케이스 추가
                    caseSet.add(x*y)
                    if x != 0:
                        caseSet.add(y//x)
                    if y != 0:
                        caseSet.add(x//y)
        if number in caseSet:
            return i
        S.append(caseSet)
    return -1

print(solution(5, 12))