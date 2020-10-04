def solution(n, words):
    stack = []
    for w in words:
        if len(stack) == 0:
            stack.append(w)
        elif stack[-1][-1] != w[0] or w in stack:
            stack.append(w)
            second= len(stack) % n
            if second == 0:
                second = n
            return [round(len(stack) / n), second]
        else:
            stack.append(w)
    return [0,0]