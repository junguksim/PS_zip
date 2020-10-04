def rotate(m, d): 
    N = len(m) 
    ret = [[0] * N for _ in range(N)] 
    if d % 4 == 1: 
        for r in range(N): 
            for c in range(N): 
                ret[c][N-1-r] = m[r][c] 
    elif d % 4 == 2: 
        for r in range(N): 
            for c in range(N): 
                ret[N-1-c][N-1-r] = m[r][c] 
    elif d % 4 == 3: 
        for r in range(N): 
            for c in range(N): 
                ret[N-1-c][r] = m[r][c]
    else: 
        for r in range(N): 
            for c in range(N): 
                ret[r][c] = m[r][c] 
    return ret

def solution(key, lock):
    answer = True
    return answer

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],[[1, 1, 1], [1, 1, 0], [1, 0, 1]]))