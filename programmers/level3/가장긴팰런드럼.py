import string
import random

# s = ''
# for i in range(2500):
#     s += random.choice(string.ascii_lowercase)
# print(s)
def solution(s):
    if len(s) <= 1:
        return len(s)
    answer = 1
    for cut in range(len(s), 0 , -1):
        for start in range(0, len(s)):
            cutStr = s[start:start+cut]
            for i in range(len(cutStr) // 2):
                if cutStr[i] == cutStr[-(i+1)]:
                    if i == len(cutStr)//2 - 1:
                        return len(cutStr)
                else:
                    break
            if start+cut >= len(s):
                break
    return answer
print(solution('abcde'))
#print(solution())

