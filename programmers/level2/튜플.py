import re

def solution(s):
    answer = []
    numbers = re.findall("\d+", s)
    numbers = list(map(int, numbers))
    maxVal = max(numbers)
    arr = [0 for i in range(maxVal+1)]
    print(numbers)
    for num in numbers:
        arr[num] += 1
    print(arr)
    for i in range(len(arr)):
        if(i == 0):
            continue
        maxInArr = max(arr)
        maxIndex = arr.index(maxInArr)
        answer.append(maxIndex)
        arr[maxIndex] = -1
    
    print(answer)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))