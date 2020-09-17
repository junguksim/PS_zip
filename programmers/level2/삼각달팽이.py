def solution(n):
    length = 0
    for i in range(1, n):
        length += i
    answer = [0 for i in range(length)]
    idx = 0
    idxArr = []
    for i in range(1, length+1): 
        if idx == 0:
            answer[idx] = i
            print(answer)
            continue
        elif idx + i < length:
            idxArr.append(i)
            idx += i
            answer[idx] = i
            
        elif i == n:
            for j in range(n, 2*n):
                answer.append(j)
            print(answer)
            continue
        else:
            if 1 in idxArr:
                idxArr.pop(0)
            else:
                idxArr.pop(-1)
            idx = sum(idxArr)
            answer[idx] = i
        print(answer)
    return answer
        
print(solution(4))

#* [1,2,9,3,10,8,4,5,6,7] 1 - 0, 2 - 1, 3 - 1+2, 4 - 1+2+3 n = 4 이므로 뒤에 567 붙고, 8 = 
#* [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9] 1-0, 2-1, 3-1+2, 4-1+2+3, 5- 1+2+3+4 10 = 1+2+3+4-1, 11 = 1+2+3-1 12 = 1+2-1 13 = 
#* [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]