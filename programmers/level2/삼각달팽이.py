def solution(n):
    numbers = []
    for i in range(1, round(n*(n+1)/2) + 1):
        numbers.append(i)
    lens = []
    for j in range(n, 0, -1):
        lens.append(j)
    for length in lens:
        
    
        
            

print(solution(5))
#* [1,2,9,3,10,8,4,5,6,7] 1 - 0, 2 - 1, 3 - 1+2, 4 - 1+2+3 n = 4 이므로 뒤에 567 붙고, 8 = 
#* [1,2,12,3,13,11,4,14,15,10,5,6,7,8,9] 1-0, 2-1, 3-1+2, 4-1+2+3, 5- 1+2+3+4 10 = 1+2+3+4-1, 11 = 1+2+3-1 12 = 1+2-1 13 = 
#* [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]