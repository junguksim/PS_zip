# def solution(numbers):
#     answer = []
#     for idx, num in enumerate(numbers):
#         sliced = numbers[idx+1:]
#         sliced = list(map(lambda x: x+num, sliced))
#         for i in sliced:
#             if i not in answer:
#                 answer.append(i)
#     answer.sort()
#     return answer

# print(solution([2,1,3,4,1]))
def solution(n):
    arr = [[0],[1],[2,9],[3,10,8],[4,5,6,7]]
    if(n == 4):
        answer = sum(arr, [])
        answer.pop(0)
        return answer
    newArr = []
    answer = []
    for i in range(5, n+1):
        for j in range(i, 2*i):
            newArr.append(j)
        arr.append(newArr)
        newArr = []
    for i in range(1, n):
        print(arr[i])
        for j in range(1, i):
            arr[i][j] += 3*(n-4)
    print(arr)
    answer = sum(arr, [])
    answer.pop(0)
    return answer

print(solution(5))

# def solution(a):
#     answer = 0
#     if(len(a) <= 2):
#         return len(a)
#     a.sort()
#     print(a)
#     answer = a[:2]
#     lessCnt = 1
#     for i in range(2, len(a)):
#         print(a[i])
#         for j in range(i):
            
#     return answer

# print(solution([9,-1,-5]))