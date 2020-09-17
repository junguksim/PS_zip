def solution(s):
    if len(s) == 1:
        return False
    if s[0] == ")":
        return False
    cnt = 1
    for i in range(1, len(s)):
        if cnt < 0:
            return False
        if s[i] == "(":
            cnt += 1
        else:
            cnt -= 1
    if cnt != 0:
        return False
    return True