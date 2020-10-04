import sys
input = sys.stdin.readline

print(''.join((sorted(list(input()), reverse=True))[:-1]))
