nums = [10, 9, 2, 5, 3, 7, 101, 18]
lst = [nums[0]]
max_len = 1
for num in nums[1:]:
    if num > lst[-1]:
        lst.append(num)
        max_len += 1
    else:
        ind =0
        while ind < len(lst) and lst[ind]< num:
            ind+=1
        lst[ind]=num
print(max_len)

