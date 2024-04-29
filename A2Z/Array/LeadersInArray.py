nums = [10, 22, 12, 3, 0, 6]

maxi = 0
result = []

for i in range(len(nums)-1, 0, -1):
    if nums[i] > maxi:
        maxi = nums[i]
        result.append(maxi)

print(result)
