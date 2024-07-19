nums = [1, 1, 1, 2, 2, 3]
k = 2


def get_top_k_items(nums, k):
    item_count = {}
    for num in nums:
        item_count[num] = item_count.get(num, 0) + 1

    items = sorted(item_count.items(), key=lambda x: x[1], reverse=True)
    output = []
    for i in items[:k]:
        output.append(i[0])

    return output


print(get_top_k_items(nums, k))
