def min_difference(arr, m):
    arr.sort()
    n = len(arr)
    if n < m:
        return -1  # Not enough packets to distribute to all students

    min_diff = float('inf')

    for i in range(n - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff


# Test cases
arr1 = [7, 3, 2, 4, 9, 12, 56]
m1 = 3
print("Minimum difference for arr1:", min_difference(arr1, m1))  # Output: 2

arr2 = [3, 4, 1, 9, 56, 7, 9, 12]
m2 = 5
print("Minimum difference for arr2:", min_difference(arr2, m2))  # Output: 6
