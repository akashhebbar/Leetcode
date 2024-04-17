from collections import Counter

nums = [10, 5, 10, 15, 10, 5]
count_map = {}

for i in nums:
    count_map[i] = count_map.get(i, 0) + 1

print(count_map)
#
# #method 2
# ans = Counter(nums)
# print(ans)


#count max freq
maxItem = {}
maxVale = 0
for item, val in count_map.items():
    if val > maxVale:
        maxItem = [item, val]
        maxVale = val
print(maxItem)
