# def solution(lines):
#     answer = 1
#     if(len(lines) == 1):
#         return 1
#     secStack = [[] for i in range(25)]
#     answerStack = []
#     for times in lines:
#         times = times.split(" ")
#         hourToSec = times[1].split(":")
#         hour = int(hourToSec[0])
#         sec = float(hourToSec[2])
#         sectionTime = float((times[2].split("s"))[0])
#         if(sec-sectionTime+0.001 < 0):
#             startSec = round(sec-sectionTime+60.001, 3)
#             secStack[hour-1].append(startSec)
#             secStack[hour].append(sec)
#         else:
#             startSec = round(sec-sectionTime+0.001, 3)
#             secStack[hour].append(startSec)
#             secStack[hour].append(sec)
#     for i in range(len(secStack)-1):
#         if(len(secStack[i]) == 0):
#             continue
#         secStack[i].sort()
#         for j in range(len(secStack[i])):
#             to = round(secStack[i][j]+1 - 0.001, 3)
#             if(j == len(secStack[i]) - 1):
#                 if(len(secStack[i+1]) != 0):
#                     nextStart = secStack[i+1][0]
#                 else:
#                     break
#             else:
#                 nextStart = secStack[i][j+1]
#             if(to > 60):
#                 newTo = round(to - 60, 3)
#                 print(f"from {secStack[i][j]} ~ to newTo {newTo}. next is {nextStart}")
#                 if(nextStart > newTo):
#                     answerStack.append(answer)
#                     print(f"answer is {answer}")
#                     continue
#                 idx = 1
#                 while(nextStart <= newTo and idx < len(secStack[i+1])):
#                     nextStart = secStack[i][idx]
#                     idx += 1
#                     answer += 1
#                 answerStack.append(answer)
#                 print(f"answer is {answer}")
#                 answer = 1
#             else:
#                 print(f"from {secStack[i][j]} ~ to {to}. next is {nextStart}")
#                 if(nextStart > to):
#                     answerStack.append(answer)
#                     print(f"answer is {answer}")
#                     continue
#                 idx = j+2
                
#                 while(nextStart <= to and idx < len(secStack[i])):
#                     nextStart = secStack[i][idx]
#                     idx += 1
#                     answer += 1
#                 answerStack.append(answer)
#                 print(f"answer is {answer}")
#                 answer = 1
#     print(secStack)
#     print(answerStack)
#     return max(answerStack)

def solution(lines):
    logs = []
    for line in lines:
        _, done, time = line.split()
        h, m, s = done.split(":")
        end = (int(h)*60*60 + int(m)*60 + float(s))* 1000
        print((end-float(time[:-1])*1000 + 1, end))
        logs.append((end-float(time[:-1])*1000 + 1, end))
    print(logs)
    length = len(logs)
    max_ = 1
    for i in range(length-1):
        cnt = 1
        for j in range(i+1, length):
            if logs[j][1] - logs[i][1] >= 4000:
                break
            if logs[j][0] - logs[i][1] < 1000:
                cnt += 1
        max_ = max(max_, cnt)
    return max_

# print(solution([
# "2016-09-15 01:00:04.002 2.0s",
# "2016-09-15 01:00:07.000 2s"
# ]))
print(solution(	[
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s",
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s",
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"]))
