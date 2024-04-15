num = 123


def get_count_digit(num: int) -> tuple:
    count = 0
    rev = ""
    while num > 0:
        last = num % 10
        rev += str(last)
        count = count + 1
        num = num // 10
    return count, rev


ans = get_count_digit(num)
cnt,rev = ans
print(cnt,rev)
