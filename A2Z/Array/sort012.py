def sort_numbers(numbers):
    low = 0
    mid = 0
    high = len(numbers) - 1  # Adjusted the high index
    while mid <= high:
        if numbers[mid] == 0:
            numbers[low], numbers[mid] = numbers[mid], numbers[low]
            low += 1
            mid += 1
        elif numbers[mid] == 1:
            mid += 1
        else:  # numbers[mid] == 2
            numbers[mid], numbers[high] = numbers[high], numbers[mid]
            high -= 1


# Example usage:
numbers = [2, 0, 2, 1, 1, 0]
sort_numbers(numbers)
print("Sorted numbers:", numbers)
