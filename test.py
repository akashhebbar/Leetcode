nums = [-1, 0, 1, 2, -1, -4]


#get sum
def get_sum(nums: list) -> list:
    ans = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if i != j and i != j and j != k and nums[i] + nums[j] + nums[k] == 0:
                    ans.append([nums[i], nums[j], nums[k]])

    return ans

#

result = get_sum(nums)
print(result)
