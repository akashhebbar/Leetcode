nums = [1, 0, 1, 1, 0, 1]
count = 1
maxcount = 1
for i in range(len(nums) - 1):
    if nums[i] == nums[i + 1]:

        count += 1
        maxcount = max(count, maxcount)
    else:
        count = 1

print(maxcount)
