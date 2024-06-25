def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def bubble_sort(arr: list):
    n = len(arr)
    for i in range(n):
        # Track whether any swaps were made in this pass
        swapped = False
        # Reduce the range of the inner loop as the last i elements are already sorted
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break


items = [20, 21, 4, -1, 66, 22, 4, 5, 21, 684, 99, 32, 53]
bubble_sort(items)
print(items)
