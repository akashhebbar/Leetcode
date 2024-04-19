nums = [1, 2, 3, 4, 5]
N = 2
# out = []
# first = nums[:N]
# sec = nums[N:]
# first.reverse()
# first.extend(sec)
# print(first)
#
#
def left_rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Ensure k is within the range of array length
    reverse(arr, 0, k - 1)  # Reverse the first k elements
    reverse(arr, k, n - 1)  # Reverse the remaining elements
    reverse(arr, 0, n - 1)  # Reverse the entire array

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

# Example usage:
arr = [1, 2, 3, 4, 5]
k = 2
left_rotate_array(arr, k)
print("Array after left rotation:", arr)

