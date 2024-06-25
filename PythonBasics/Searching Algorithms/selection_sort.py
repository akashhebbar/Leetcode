# code for selection sort (find the minimum and sort)

items = [20, 21, 4, -1, 66, 22, 4, 5, 21, 684, 99, 32, 53]


# swap function
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


# selection sort find the min in each iteration and then sort
def selection_sort(item_list: list):
    for i in range(len(item_list) - 1):
        min_item = i
        for j in range(i + 1, len(item_list)):
            if item_list[j] < item_list[min_item]:
                min_item = j
        swap(item_list, i, min_item)


selection_sort(items)

print(items)
