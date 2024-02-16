arr = [22, 14, 8, 17, 35, 3]


def find_max_min(arr: list):
    max_val = 0
    min_val = 1000

    for num in arr:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return max_val, min_val


maxval, minval = find_max_min(arr)
print("max", maxval)
print("min", minval)
