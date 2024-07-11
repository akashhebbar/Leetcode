def add_one_to_num(num):
    if num >= 9:
        print(num)
        return num + 1
    else:
        print(num)
        num += 1

        return add_one_to_num(num)


get_nums = add_one_to_num(1)
print(get_nums)
