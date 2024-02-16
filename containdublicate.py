nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]


def check_unique1(nums):
    unique = set(nums)
    return len(unique) == len(nums)


def check_unique2(nums):
    lst = []
    for i in nums:
        if i not in lst:
            lst.append(i)
        else:
            return False
    return True


ans = check_unique2(nums)
print(ans)
