# import sys
# input = sys.stdin.readline
import re

line = ""
ops = ["[", "]", "(", ")"]

def isRight(line):
    stack = []
    if len(line) == 0:
        print("yes")
        return
    for s in line:
        if s not in ops:
            continue
        if s == '(' or s == "[":
            stack.append(s)
        else:
            if not stack:
                print("no")
                return
            else:
                if s == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        print("no")
                        return
                elif s == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        print('no')
                        return
    if not stack:
        print("yes")
        return
    else:
        print("no")
        return
while True:
    line = input()
    if line == '.':
        break
    newLine = ""
    for s in line:
        if s not in ops:
            continue
        newLine += s
    isRight(newLine)
    
