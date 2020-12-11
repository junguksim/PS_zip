import sys
from itertools import permutations
def input(): return sys.stdin.readline().strip()


N = int(input())
words = []

for i in range(N):
    words.append(list(input()))
values = [0 for i in range(26)]
for word in words:
    lengthOfWord = len(word)
    for idx, alphabet in enumerate(word):
        values[ord(alphabet) - 65] += 10 ** (lengthOfWord - idx - 1)
values.sort(reverse=True)
result, cnt = 0, 9
for value in values:
    result += cnt * value
    cnt -= 1


print(result)
