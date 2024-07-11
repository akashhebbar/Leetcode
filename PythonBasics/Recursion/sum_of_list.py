items = [1, 2, [3, 4], [5, 6]]


def get_sum(items):
    total = 0

    for i in items:
        if type(i) == list:
            total += get_sum(i)
        else:
            total += i
    return total


print(get_sum(items))
