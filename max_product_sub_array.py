def max_product_subarray(nums):
    if not nums:
        return 0

    res = max(nums)
    curMax= 1
    curMin=1

    for i in nums:
        tmp = i*curMax
        curMax = max(i*curMin , i* curMax , i)
        curMin = min((i*tmp , i*curMin ,i))
        res = max(res , curMax)
    return res


# Example usage:
nums = [2,3,-2,4]
print(max_product_subarray(nums))  # Output: 180
