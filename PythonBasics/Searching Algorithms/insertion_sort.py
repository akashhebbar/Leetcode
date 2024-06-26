# select item and insert into correct position
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        while i > 0 and arr[i] < arr[i - 1]:
            swap(arr, i, i - 1)
            i -= 1


# Call function

items = [20, 21, 4, -1, -8, 66, 22, 4, 5, 21, 684, 99, 32, 53]
insertion_sort(items)
print(items)
