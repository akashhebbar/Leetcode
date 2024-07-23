numbers = [1, 2, 3, 4]
target = 5


def get_match(numbers: list, target: int) -> list:
    start = 0
    end = len(numbers) - 1
    if len(numbers) == 2:
        return [1, 2]
    while start < end:
        sum = numbers[start] + numbers[end]
        if sum == target:
            return [start + 1, end + 1]
        elif sum > target:
            end -= 1
        else:
            start += 1


ans = get_match(numbers, target)
print(ans)
