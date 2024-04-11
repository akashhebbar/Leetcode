nums = [6, 0, 8, 2, 3, 0, 4, 0, 1]


def move_all_zero(nums: list):
    k = 0
    for i in nums:
        if i > 0:
            nums[k] = i
            k += 1

    for i in range(k, len(nums)):
        nums[i] = 0


move_all_zero(nums)
print(nums)
