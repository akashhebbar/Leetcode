nums = [6, -4, -3, 2, 3]

for i in range(len(nums)):
    left_sum = 0
    right_sum = 0
    for j in range(0, i):
        left_sum += nums[j]
    for k in range(i, len(nums)):
        right_sum += nums[k]

    if left_sum == right_sum:
        print(i)
print(-1)
