# nums = [1,2,-3,-1,-2,-3]
# negative=[]
# positive=[]
# for  i in nums:
#     if i < 0:
#         negative.append(i)
#     else:
#         positive.append(i)
#
#
#
#
# ans = []
# i, j = 0, 0
# while i < len(negative) and j < len(positive):
#     ans.append(positive[i])
#     ans.append(negative[j])
#     i += 1
#     j += 1
#
# if i!=len(positive):
#     ans.extend(positive[i:])
# if j!=len(negative):
#     ans.extend(negative[j:])
# print(ans)

def rearrange_by_sign(A):
    # Define 2 lists, one for storing positive and other for negative elements of the array.
    pos = []
    neg = []

    # Segregate the array into positives and negatives.
    for i in range(len(A)):
        if A[i] > 0:
            pos.append(A[i])
        else:
            neg.append(A[i])

    # Positives on even indices, negatives on odd.
    for i in range(len(pos)):
        A[2 * i] = pos[i]
    for i in range(len(neg)):
        A[2 * i + 1] = neg[i]

    return A



# Array Initialisation.
A = [1, 2, -4, -5]
ans = rearrange_by_sign(A)

for i in range(len(ans)):
    print(ans[i], end=" ")
