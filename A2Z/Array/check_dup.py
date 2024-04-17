from typing import List

# method 0
nums = [1, 1, 2, 2, 2, 3, 3]
s = set(nums)

out = []

# Append all unique elements of the set s to the beginning of the list out
out.extend(s)

# Fill the remaining positions with "-"
for _ in range(len(nums) - len(s)):
    out.append("-")

print(out)


# method 1


def removeDuplicates(arr: List[int]) -> int:
    st = set()
    for i in range(len(arr)):
        st.add(arr[i])
    k = len(st)
    j = 0
    for x in st:
        arr[j] = x
        j += 1
    return k


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")


#method 2


def removeDuplicates(arr: List[int]) -> int:
    i = 0
    for j in range(1, len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]
    return i + 1


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 3, 3]
    k = removeDuplicates(arr)
    print("The array after removing duplicate elements is ")
    for i in range(k):
        print(arr[i], end=" ")
