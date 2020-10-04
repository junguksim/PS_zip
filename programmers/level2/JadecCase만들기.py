def jaden(s):
    if len(s) == 0:
        return ""
    first = s[0]
    elses = s[1:]
    first = str.upper(first)
    elses = ''.join(list(map(lambda x: str.lower(x), elses)))
    return first + elses

def solution(s):
    s = s.split(' ')
    print(s)
    s = list(map(lambda x: jaden(x), s))
    return ' '.join(s)

print(solution('abcde ffff g gggggg g        ggggggg'))