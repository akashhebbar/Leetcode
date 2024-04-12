nums = [5, 6, 3, 4, 3, 6, 4]


def find_index(nums: list) -> int:
    hash_map = {}
    min_index = 100000000
    for i in range(len(nums)):
        if nums[i] in hash_map:
            min_index = min(min_index, hash_map[nums[i]])

        else:
            hash_map[nums[i]] = i
    if min_index:
        return min_index
    return -1


ans = find_index(nums)
print(ans)
print()
