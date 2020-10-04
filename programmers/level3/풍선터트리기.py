import heapq

def solution(a):
    balloons = [(b,i) for i,b in enumerate(a)]
    result = len(a)
    left, right = balloons[:1], balloons[1:]
    heapq.heapify(left)
    heapq.heapify(right)
    

    NUM, IDX = 0, 1
    for i, ballon in enumerate(a[1:-1], 1):
        if ballon == right[0][NUM]:
            while right[0][IDX] <= i:
                heapq.heappop(right) # * right의 0번째 요소의 인덱스가 i 보다 작은 동안 pop
        if ballon > left[0][NUM] and ballon > right[0][NUM]:
            result -= 1
        heapq.heappush(left, (ballon, i))
    return result

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
