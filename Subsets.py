nums = [1, 2, 3]
output = [[]]

for num in nums:
    new_subsets = []
    for current in output:
        new_subset = current + [num]
        new_subsets.append(new_subset)
    output.extend(new_subsets)




print(output)
