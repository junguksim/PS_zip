import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    ropes = []
    values = []
    for _ in range(N):
        ropes.append(int(input()))
    ropes.sort(reverse=True)
    for i in range(N):
        values.append(ropes[i] * (i+1))
    print(max(values))

main()