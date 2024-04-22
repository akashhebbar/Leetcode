nums = [2,3,5]
max_len = 0
k = 2

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if sum(nums[i:j]) == k:
            max_len = max(max_len, len(nums[i:j]))

print(max_len)
