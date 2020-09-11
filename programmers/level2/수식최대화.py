import re

def solution(expression):
    answer = 0
    arr = [["*","+","-"], ["*","-","+"], ["+","*","-"], ["+","-","*"], ["-","*","+"], ["-","+","*"]]
    stack = []
    numbers = list(map(int, re.findall("\d+", expression)))
    tempNumbers = numbers[:]
    ops = re.findall("[-+*]+", expression)
    tempOps = ops[:]
    print(numbers, ops)
    idx = 0
    while len(arr) > 0:
        if(arr[0][idx] in tempOps):
            gopIdx = tempOps.index(arr[0][idx])
            if(arr[0][idx] == "*"):
                tempNumbers[gopIdx] = tempNumbers[gopIdx] * tempNumbers[gopIdx+1]
            elif(arr[0][idx] == "+"):
                tempNumbers[gopIdx] = tempNumbers[gopIdx] + tempNumbers[gopIdx+1]
            else:
                tempNumbers[gopIdx] = tempNumbers[gopIdx] - tempNumbers[gopIdx+1]
            tempNumbers.pop(gopIdx+1)
            tempOps.pop(gopIdx)
            print(tempNumbers)
            print(tempOps)
            continue
        idx += 1
        if(idx == 3):
            value = abs(tempNumbers[0])
            stack = []
            answer = max(value, answer)
            print(answer)
            idx = 0
            arr.pop(0)
            tempOps = ops[:]
            tempNumbers = numbers[:]
    return answer
        

print(solution("100-200*300-500+20"))