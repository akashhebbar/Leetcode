nums = [-2, 1, -3, 4, 1, 2, 1, -5, 4]


def kadane_max_sum(nums: list) -> int:
    max_ending = 0
    max_so_for = nums[0]
    for i in range(len(nums)):
        max_ending = max_ending + nums[i]
        if max_ending < 0:
            max_ending = 0
        elif max_ending > max_so_for:
            max_so_for = max_ending

    return max_so_for


ans = kadane_max_sum(nums)
print(ans)
