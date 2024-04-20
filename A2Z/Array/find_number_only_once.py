nums = [4, 1, 2, 1, 2]

dict = {}

for i in nums:
    dict[i] = dict.get(i, 0) + 1

print(dict)
for i, j in dict.items():
    if j == 1:
        print(i)
