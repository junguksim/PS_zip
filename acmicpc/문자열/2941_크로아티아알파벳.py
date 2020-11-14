import sys
def input(): return sys.stdin.readline().strip()


alphas = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
s = input()
for i in range(len(alphas)):
    s = s.replace(alphas[i], alphas[i][0].upper())
print(len(s))
