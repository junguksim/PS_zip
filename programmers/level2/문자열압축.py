def solution(s):
    answer = 0
    if len(s) == 1:
        return 1
    length = 1
    while length < len(s):
        i = 0
        arr = []
        while True:
            if i + length <= len(s):
                arr.append(s[i:i+length])
            else:
                if len(s[i:]) > 0:
                    arr.append(s[i:])
                break
            i += length
        newS = ""
        cnt = 0
        print(arr)
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                if cnt == 0:
                    cnt = 2
                else:
                    cnt += 1
                if i == len(arr) - 2:
                    newS += str(cnt) + arr[i]
            else:
                if cnt == 0:
                    newS += arr[i]
                else:
                    newS += str(cnt) + arr[i]
                    cnt = 0
                if i == len(arr) - 2:
                    newS += arr[i + 1]
        if answer == 0:
            answer = len(newS)
        else:
            answer = min(answer, len(newS))
        length += 1
    return answer

print(solution("a"))