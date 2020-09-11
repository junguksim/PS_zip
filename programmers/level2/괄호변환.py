def isItRight(p):
    left = 0
    right = 0
    for bracket in p:
        if bracket == "(":
            left += 1
        else:
            right += 1
        if left < right:
            return False
    return True

def makeBalanced(p):
    if(p == ""):
        return ""
    left = 0
    right = 0
    for i in range(len(p)):
        if(p[i] == "("):
            left += 1
        else:
            right += 1
        last = p[i]
        if(left == right):
            if(last == ")"):
                return p[:i+1] + makeBalanced(p[i+1:])
            else:
                return reverse(p[:i+1], makeBalanced(p[i+1:]))

def reverse(u, v) :
    empty = '('
    empty += v + ')'
    for i in range(1, len(u)-1):
        if u[i] == '(':
            empty += ')'
        else:
            empty += '('
    return empty

def solution(p):
    if(isItRight(p)):
        return p
    return makeBalanced(p)

print(solution(")("))