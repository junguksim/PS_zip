def solution(numbers, hand):
    answer = ''
    pad = [[1,2,3],[4,5,6],[7,8,9],["*",0,"#"]]
    leftPad = [1,4,7]
    rightPad = [3,6,9]
    centerPad = [2,5,8,0]
    leftPos = [3, 0]
    rightPos = [3, 2]
    for num in numbers:
        if(num in leftPad):
            line = leftPad.index(num)
            leftPos = [line, 0]
            answer += "L"
            print(answer)
        elif(num in rightPad):
            line = rightPad.index(num)
            rightPos = [line, 2]
            answer += "R"
            print(answer)
        else:
            line = centerPad.index(num)
            keyAt = [line, 1]
            disL = abs(leftPos[0]-keyAt[0]) + abs(leftPos[1]-keyAt[1]) 
            disR = abs(rightPos[0]-keyAt[0]) + abs(rightPos[1]-keyAt[1])
            print(f"leftPos={leftPos}, rightPos={rightPos}, disL = {disL}, disR = {disR}, num = {num} 이므로 keyAt={keyAt}")
            if(disL == disR):
                if(hand == "right"):
                    rightPos = keyAt
                    answer += "R"
                else:
                    leftPos = keyAt
                    answer += "L"
            elif(disL > disR):
                answer += "R"
                rightPos = keyAt
            else:
                leftPos = keyAt
                answer += "L"
            print(answer)


    return answer

print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))