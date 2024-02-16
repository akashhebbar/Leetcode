nums = [5,4,-1,7,8]


# use kadane algorithm

def get_maxi(nums):
    sum = 0
    maxi = nums[0]

    for num in nums:
        sum += num
        maxi = max(maxi, sum)
        if sum < 0:
            sum = 0
    return maxi


print(get_maxi(nums))
