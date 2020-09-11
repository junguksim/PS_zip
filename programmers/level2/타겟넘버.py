def solution(numbers, target):
    sup = [0]
    for i in numbers:
        sub = []
        for j in sup:
            sub.append(j + i)
            sub.append(j - i)
        print(sub)
        sup = sub
    return sup.count(target)

print(solution([1,1,1,1,1], 3))