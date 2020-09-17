def solution(n, arr1, arr2):
    answer = [""]*n
    for i in range(n):
        arr1[i] = format(arr1[i], "b")
        while(len(arr1[i]) < n):
            arr1[i] = "0" + arr1[i]
        arr2[i] = format(arr2[i], "b")
        while(len(arr2[i]) < n):
            arr2[i] = "0" + arr2[i]
        for j in range(n):
            if(arr1[i][j] == "1" or arr2[i][j] == "1"):
                answer[i] += "#"
            else:
                answer[i] += " " 
    print(arr1, arr2)
    return answer


print(solution(5, [9, 20, 28, 18, 11], 	[30, 1, 21, 17, 28]))