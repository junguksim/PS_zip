import re

def solution(words, queries):
    answer = []
    for i in range(len(queries)):
        a = 0
        queries[i] = queries[i].replace("?", ".")
        for j in range(len(words)):
            if len(words[j]) != len(queries[i]):
                continue
            if re.match(queries[i], words[j]):
                a += 1
        answer.append(a)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))