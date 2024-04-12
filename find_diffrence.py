nums = [1, 5, 2, 2, 2, 5, 5, 4]

diff = 3


def find_diff_pair(nums: list, diff: int):
    count = {}
    for i in nums:
        count[i] = count.get(i, 0) + 1

    for i in nums:
        if i - diff in count and count[i - diff] > 0:
            print(i, i - diff)
        if i + diff in count and count[i + diff] > 0:
            print(i, i + diff)

        count[i] -= 1


find_diff_pair(nums, diff)
