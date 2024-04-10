nums = [3, 4, -7, 3, 1, 3, 1, -4, -2, -2]


def get_sum_with_zero(nums: list) -> bool:
    add_values = set()
    add_values.add(0)
    total = 0
    for i in nums:
        total += i
        if total in add_values:
            return True

        add_values.add(total)

    return False


result = get_sum_with_zero(nums)
if result:
    print("Found sum zero")
else:
    print("Not found")
