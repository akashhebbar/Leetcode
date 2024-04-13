nums = [2, 4, 6, 8, 4, 2, 45, 7, 3, 24, 56]


def selection_sort(nums: list):
    for i in range(len(nums) - 1):
        small_index = i
        for j in range(i, len(nums)):
            if nums[j] < nums[small_index]:
                small_index = j

        nums[i], nums[small_index] = nums[small_index], nums[i]


selection_sort(nums)
print("Sorted:", nums)
