nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [2, 3, 4, 4, 5, 11, 12]
union_array = []

# Set up pointers for both arrays
i = 0
j = 0


# Merge the arrays while maintaining sorted order
while i < len(nums1) and j < len(nums2):
    if nums1[i] < nums2[j]:
        union_array.append(nums1[i])
        i += 1
    elif nums1[i] > nums2[j]:
        union_array.append(nums2[j])
        j += 1
    else:  # If both elements are equal, add either one to the union array
        union_array.append(nums1[i])
        i += 1
        j += 1

# Add remaining elements from nums1 (if any)
while i < len(nums1):
    union_array.append(nums1[i])
    i += 1

# Add remaining elements from nums2 (if any)
while j < len(nums2):
    union_array.append(nums2[j])
    j += 1

print(union_array)
