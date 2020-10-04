import sys
input = sys.stdin.readline
from collections import Counter

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))

def mean(nums):
    return round(sum(nums)/len(nums))

def median(nums):
    nums.sort()
    return nums[len(nums)//2]

def mode(nums):
    mode_dict = Counter(nums)
    modes = mode_dict.most_common()
    if len(nums) > 1:
        if modes[0][1] == modes[1][1]:
            mod = modes[1][0]
        else : 
            mod = modes[0][0]
    else : 
        mod = modes[0][0]

    return mod

def scope(nums):
    return max(nums) - min(nums)

print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))