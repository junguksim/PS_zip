import sys
input = sys.stdin.readline

def main():
    n = int(input())
    arr = []
    nums = [i for i in range(n+1)]
    answer = []
    for _ in range(n):
        arr.append(int(input()))

    i = 0
    idx = 0
    while idx < len(arr):
        try:
            if nums[i] < arr[idx]:
                i += 1
                answer.append("+")
            else:
                nums.pop(i)
                answer.append('-')
                i -= 1
                idx += 1
        except:
            print('NO')
            return
    for a in answer:
        print(a)
main()
