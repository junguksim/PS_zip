import sys
input = sys.stdin.readline
from pprint import pprint

N = int(input())
def makeBoard(N):
    return [[0 for i in range(N)] for i in range(N)]

def setQueen(x,y,board, N):
    board[x][y] = 1
    board[x] = [1 for i in range(N)]
    for i in range(len(board)):
        board[i][y] = 1
        


board = makeBoard(N)
pprint(board, indent=0, width=N*5)