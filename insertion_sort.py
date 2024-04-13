nums = [2, 5, 6, 7, 3, 1, 22, 33, 11, 2, 77]


def insertion_sort(nums: list):
    for i in range(len(nums)):
        j = i
        while (j > 0 and nums[j - 1] > nums[j]):
            temp = nums[j - 1]
            nums[j] = nums[j - 1]
            nums[j - 1] = nums[j]
            j -= 1


insertion_sort(nums)
print("Sorted:", nums)
