numbers = [2, 11, 7, 15]
target = 9
print(len(numbers))
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(i, j)
