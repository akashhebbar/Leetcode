nums = [5, 6, 8, 2, 4, 6, 9]
k = 2


def check_repeate(nums: list, k: int) -> bool:
    for i in range(len(nums)):
        distance = 0
        for j in range(i + 1, len(nums)):
            distance += 1
            if nums[j] == nums[i] and distance <= k:
                return True

    return False


ans = check_repeate(nums, k)
print(ans)


# #solution 2
# def check_repeate(nums: list, k: int) -> bool:
#     num_index = {}
#     for i, num in enumerate(nums):
#         if num in num_index and i - num_index[num] <= k:
#             return True
#         num_index[num] = i
#     return False
#
#
# nums = [5, 6, 8, 2, 4, 6, 9]
# k = 4
# ans = check_repeate(nums, k)
# print(ans)
