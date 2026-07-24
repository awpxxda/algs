def inplace(nums: list[int]) -> list[int]:
    slow = 0
    fast = 0
    # 1 0 0 3 0 0 5 -> 1 3 5 0 0 0 0
    while fast < len(nums):
        if nums[fast] != 0:
            nums[fast], nums[slow] = nums[slow], nums[fast] 
            slow += 1
            fast += 1
        else:
            fast += 1
    return nums

print(inplace([1, 0, 0, 3, 0, 0, 5]))
