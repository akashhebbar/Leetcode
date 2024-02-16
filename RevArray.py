arr = [1, 2, 3, 4, 5, 6]


def reverse(arr):
    return arr[::-1]


def reverse2(arr):
    ar2 = []
    for i in range(len(arr) - 1, -1, -1):
        ar2.append(arr[i])
    return ar2


# ans = reverse2(arr)


def reverse3_inplace(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

    return arr


ans = reverse3_inplace(arr)

print(ans)


