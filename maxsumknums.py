def ms(nums: list[int], k: int) -> int:


    # 1 2 3 4, k = 2 -> 7
    window_sum = 0
    for i in range(k):
        window_sum += nums[i]
    max_sum = window_sum

    for r in range(k, len(nums)):
        l = r - k
        window_sum = window_sum + nums[r] - nums[l]
        max_sum = max(max_sum, window_sum)


    return max_sum

print(ms([1, 2, 3, 4], 2))


