def solution(n, t, m, timetable):
    answer = ''
    arriveList = []
    waitList = []
    goingList = []
    cnt = m
    firstArrive = (9, 0)
    for i in range(n):
        arriveList.append(firstArrive)
        if(firstArrive[1] + t >= 60):
            firstArrive = (firstArrive[0] + 1, firstArrive[1] + t - 60)
        else :
            firstArrive = (firstArrive[0], firstArrive[1] + t)
    
    for wait in timetable:
        wait = wait.split(":")
        wait = (int(wait[0]), int(wait[1]))
        waitList.append(wait)
    waitList.sort(key=lambda el: (el[0], el[1]))
    print(f"arriveList : {arriveList}")
    print(f"waitList : {waitList}")
    if(m > len(waitList)):
        return makeTime(arriveList[-1][0], arriveList[-1][1])
    while len(arriveList) > 0:
        for arrIdx,arrTime in enumerate(arriveList):
            for idx, wait in enumerate(waitList):
                if idx in goingList:
                    continue
                print(f"arrH = {arrTime[0]} arrM = {arrTime[1]}, waitH = {wait[0]}, waitM = {wait[1]}")
                if(arrTime[0] > wait[0] or (arrTime[0] == wait[0] and arrTime[1] >= wait[1]) and cnt > 0):
                    cnt -= 1
                    goingList.append(idx)
                if(arrIdx == len(arriveList) -1):
                    # if(cnt == 1):
                    print(f"cnt = {cnt}")
                    if(idx == len(waitList)-1):
                        print("1")
                        return makeTime(arrTime[0],arrTime[1])
                    elif(cnt == 1):
                        print("2")
                        return makeTime(wait[0], wait[1]-1)
                    else:
                        print("3")
                        return makeTime(wait[0], wait[1])
                    # else:
                    #     if(arrTime[0] < waitList[idx+1][0] or (arrTime[0]==waitList[idx+1][0] and arrTime[1] <= waitList[idx+1][1])):
                    #         print("4")
                    #         return makeTime(arrTime[0], arrTime[1])
            arriveList.pop(arrIdx)
            print(f"arriveList : {arriveList}, cnt = {cnt}")
            print(f"waitList : {waitList}, goingList : {goingList}")
            cnt = m
    return answer

def makeTime(h, m):
    if(m < 0):
        m = 60 + m
        h -= 1
    if(h < 10):
        h = "0" + str(h)
    else:
        h = str(h)
    if(m < 10):
        m = "0" + str(m)
    else:
        m = str(m)
    return h+":"+m
# print(solution(1,1,5,['08:00', '08:01', '08:02', '08:03']))
# print(solution(2,10,2,["09:10", "09:09", '08:00']))
print(solution(2,1,2,['09:00', '09:00','09:00','09:00']))
print(solution(2,10,2,["09:05", "09:06", "09:00", "09:00", "09:00"]))
print(solution(2, 10, 2, ["09:10", "09:09", "08:00"]))