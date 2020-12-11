import sys
def input(): return sys.stdin.readline().strip()


N = int(input())
change = 1000 - N
coins = [500, 100, 50, 10, 5, 1]
coinIdx = 0
answer = 0
while change > 0:
    answer += change // coins[coinIdx]
    change = change % coins[coinIdx]
    coinIdx += 1

print(answer)
