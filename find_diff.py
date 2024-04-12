def findPair(A, diff):
    # Create a dictionary to store the counts of each element
    count = {}

    # Iterate through the list to populate the dictionary
    for num in A:
        count[num] = count.get(num, 0) + 1
    print("count", count)
    # Iterate through the list again to find pairs
    for num in A:
        # Check if the difference exists in the dictionary
        if num - diff in count and count[num - diff] > 0:
            print((num, num - diff))
        if num + diff in count and count[num + diff] > 0:
            print((num, num + diff))

        # Decrement the count of the current number to avoid duplicate pairs
        count[num] -= 1


if __name__ == '__main__':
    A = [1, 5, 2, 2, 2, 5, 5, 4]
    diff = 3
    findPair(A, diff)