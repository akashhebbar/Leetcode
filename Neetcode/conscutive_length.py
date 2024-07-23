nums = [100, 4, 200, 1, 3,5, 2]
unique = set(nums)
lng = 0
for i in nums:
    if (i - 1) not in unique:
        long = 0
        while i + long in unique:
            long += 1
        lng = max(lng, long)

print(lng)
