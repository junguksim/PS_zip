import heapq

def solution(scoville, K):
    answer = 0
    heap = []

    for num in scoville:
        heapq.heappush(heap, num)
    print(heap)
    while heap[0] < K:
        try:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap)*2))
        except IndexError:
            return -1
        answer += 1
    return answer
print(solution([1,2,3,9,10,12], 7))