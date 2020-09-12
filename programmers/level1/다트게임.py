def solution(dartResult):
    answer = 0
    queue = []
    bonuses = ["S", "D", "T", "*", "#", "N"]
    dartResult = dartResult.replace("10", "N")
    print(dartResult)
    for i in range(len(dartResult)):
        s = dartResult[i]
        if(s == "N"):
            queue.append(10)
        if s not in bonuses:
            queue.append(int(s))
        else:
            if s == "D":
                queue[-1] = queue[-1] ** 2
            if s == "T":
                queue[-1] = queue[-1] ** 3
            if s == "*":
                queue[-1] = queue[-1] * 2
                if(len(queue) >= 2):
                    queue[-2] = queue[-2] * 2
            if s == "#":
                queue[-1] = queue[-1] * -1
            print(queue)
    print(queue)
    answer = sum(queue)
    return answer


print(solution("1D2S#10S"))