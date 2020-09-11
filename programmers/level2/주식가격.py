def solution(prices):
    stack = []
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            if(prices[i] <= prices[j]):
                cnt += 1
            else:
                cnt += 1
                break
        stack.append(cnt)
    stack.append(0)
    return stack

print(solution([3,4,2,6,5]))