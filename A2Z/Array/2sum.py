nums = [2, 6, 5, 8, 11]
hmap = {}
target = 14


# for i in range(len(nums)):
#     rem = target - nums[i]
#     if rem in hmap:
#         print(i)
#         print(hmap[rem], i)
#     else:
#
#         hmap[nums[i]] = i


def twoSum(nums, target):
    result_map = {}
    for i in range(len(nums)):
        tmp = target - nums[i]
        if tmp in result_map:
            return [result_map[tmp], i]
        result_map[nums[i]] = i


ans = twoSum(nums, target)
print(ans)
