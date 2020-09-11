import sys
input = sys.stdin.readline

memo =[0] * 101
memo[1] = 1
memo[2] = 1
memo[3] = 1
for k in range(0, 98):
    memo[k+3] = memo[k]+memo[k+1]
answer = []
T = int(input())
for i in range(0, T):
    n = int(input())
    print(memo[n])

# * 1,1,1,2,2, 3(2+1),4(3+1),5(4+1),7(5+2),9(7+2),12(9+3),16(12+4),21(16+5),28(21+7),37(28+9)