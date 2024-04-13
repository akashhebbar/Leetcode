nums = [2, 4, 2, 0, 1, 4, 55, 77, 33, 22, 66, 11]


def swap(nums: list, i: int, j: int):
    temp = nums[i]
    nums[i] = nums[j]
    nums[j] = temp


def bubble_sort(nums: list):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] > nums[j]:
                swap(nums, i, j)


bubble_sort(nums)
print("sorted:", nums)
