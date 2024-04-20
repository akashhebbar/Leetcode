# def find_missing_number(nums):
#     n = len(nums) + 1  # Expected length of the sequence
#     expected_sum = n * (n + 1) // 2  # Sum of a sequence from 1 to n
#     actual_sum = sum(nums)  # Sum of numbers in the array
#     missing_number = expected_sum - actual_sum
#     return missing_number
#
# # Example usage:
# nums = [1, 2, 4, 5, 6]
# missing_number = find_missing_number(nums)
# print("The missing number is:", missing_number)

nums = [1, 2, 4, 5,7]

maxval=max(nums)

for i in range(1,maxval+1):
    if i not in nums:
        print(i)

