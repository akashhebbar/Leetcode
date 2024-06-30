# Partition the list into two sublists with the same sum
def partition(A):
    # do for each element in the list
    for i in range(len(A)):
        left_sum = 0
        for j in range(i):
            left_sum += A[j]

        right_sum = 0
        for j in range(i, len(A)):
            right_sum += A[j]

        # if the sum of `A[0…i-1]` is equal to `A[i, n-1]`
        if left_sum == right_sum:
            return i

    # invalid input
    return -1


if __name__ == '__main__':

    A = 6, -4, -3, 2, 3

    # get index `i` that points to the starting of the second sublist
    i = partition(A)

    if i != -1:
        print(A[:i])  # print the first sublist, `A[0, i-1]`
        print(A[i:])  # print the second sublist, `A[i, n-1]`
    else:
        print("The list can't be partitioned")