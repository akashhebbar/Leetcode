nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]


def get_majority_element(nums: list) -> int:
    k = 0
    ele = -1

    for i in range(len(nums)):
        if k == 0:
            ele = nums[i]
            k = 1

        elif ele == nums[i]:
            k += 1
        else:
            k -= 1

    return ele


ans = get_majority_element(nums)

print(ans)