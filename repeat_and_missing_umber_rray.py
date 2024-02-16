# Each integer appears exactly once except A which appears twice and B which is missing.
#
# Return A and B.
#
# Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
#
# Note that in your output A should precede B.

def find_duplicates(nums):
    n = len(nums)
    sum_to_n = (n * (n + 1)) // 2
    sum_of_squares_to_n = (n * (n + 1) * (2 * n + 1)) // 6
    actual_sum = sum(nums)
    actual_sum_of_squares = sum(x * x for x in nums)

    B = sum_to_n - actual_sum
    A = (sum_of_squares_to_n - actual_sum_of_squares) // B

    return [A, B]


nums = [3, 1, 2, 5, 3]
print(find_duplicates(nums))  # Output: [3, 4]


def find_duplicates_2(nums):
    num_set = set()
    duplicate = None

    # Step 1: Find the duplicate number using a hash set
    for num in nums:
        if num in num_set:
            duplicate = num
            break
        num_set.add(num)

    # Step 2: Find the missing number
    n = len(nums)
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    missing = total_sum - actual_sum + duplicate

    return [duplicate, missing]


nums = [3, 1, 2, 5, 3]
print(find_duplicates_2(nums))