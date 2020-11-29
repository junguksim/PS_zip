import sys
def input(): return sys.stdin.readline().strip()
from collections import deque

def main():
    answer = 0
    gears = []
    turns = []
    SHOULD_CHECK_GEAR_NUMBER_RIGHT = 2
    SHOULD_CHECK_GEAR_NUMBER_LEFT = 6
    for _ in range(4):
        gears.append(deque(list(map(int, list(input())))))
    turnTimes = int(input())
    for _ in range(turnTimes):
        turns.append(list(map(int, input().split(" "))))
    

    def turnClockwise(whichGear):
        print(f"{whichGear + 1}번 모터가 시계방향으로 회전")
        gears[whichGear].appendleft(gears[whichGear].pop())
    def turnCounterClockWise(whichGear):
        print(f"{whichGear + 1}번 모터가 반시계방향으로 회전")
        gears[whichGear].append(gears[whichGear].popleft())
    
    def verifyNextDirection(whichGear, startGearTurnDirection):
        if startGearTurnDirection == 1:
            return -1
        else:
            return 1
    def moveByDirection(whichGear, direction):
        if direction == 1:
            turnClockwise(whichGear)
        elif direction == -1:
            turnCounterClockWise(whichGear)
        else:
            return False
    def checkGearShouldTurnFromRightToLeft(whichGear, startGearTurnDirection, shouldMoves):
        if whichGear > 0:
            compareGear = whichGear - 1
            if gears[whichGear][SHOULD_CHECK_GEAR_NUMBER_LEFT] != gears[compareGear][SHOULD_CHECK_GEAR_NUMBER_RIGHT]:
                nextDirection = verifyNextDirection(whichGear, startGearTurnDirection)
                shouldMoves.append([compareGear, nextDirection])
                return checkGearShouldTurnFromRightToLeft(compareGear, nextDirection, shouldMoves)
            else:
                print("같은 극이므로 오른쪽에서 왼쪽으로 탐색을 끝냅니다")
                return shouldMoves
        print(f"더 이상 왼쪽 모터가 없어 탐색하지 않습니다.")
        return shouldMoves
    def checkGearShouldTurnFromLeftToRight(whichGear, startGearTurnDirection, shouldMoves):
        if whichGear < 3:
            compareGear = whichGear + 1
            if gears[whichGear][SHOULD_CHECK_GEAR_NUMBER_RIGHT] != gears[compareGear][SHOULD_CHECK_GEAR_NUMBER_LEFT]:
                nextDirection = verifyNextDirection(whichGear, startGearTurnDirection)
                shouldMoves.append([compareGear, nextDirection])
                return checkGearShouldTurnFromLeftToRight(compareGear, nextDirection, shouldMoves)
            else:
                print("같은 극이므로 왼쪽에서 오른쪽으로 탐색을 끝냅니다")
                return shouldMoves
        print(f"더 이상 오른쪽 모터가 없어 탐색하지 않습니다.")
        return shouldMoves
    for i in range(len(turns)):
        print(f"{i}번째")
        shouldMoves = []
        shouldMoves = checkGearShouldTurnFromRightToLeft(turns[i][0] - 1, turns[i][1], shouldMoves)
        shouldMoves = checkGearShouldTurnFromLeftToRight(turns[i][0] - 1, turns[i][1], shouldMoves)
        moveByDirection(turns[i][0]-1, turns[i][1])
        for j in range(len(shouldMoves)):
            moveByDirection(shouldMoves[j][0], shouldMoves[j][1])
    print(gears)
    point = 1
    for i in range(4):
        if gears[i][0] == 1:
            answer += point
        point *= 2
    print(answer)
main()