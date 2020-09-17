def solution(nums):
    count = int(len(nums) / 2)
    types = list(set(nums))
    if len(types) < count:
        return len(types)
    elif len(types) >= count:
        return count