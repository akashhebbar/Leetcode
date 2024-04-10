nums = [1, 0, 1, 0, 1, 0, 0, 1]


def swap(nums: list, i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def sort_list(nums: list):
    pivot = 1
    j = 0

    for i in range(len(nums)):
        if nums[i] < pivot:
            swap(nums, i, j)
            j += 1


sort_list(nums)
print(nums)
