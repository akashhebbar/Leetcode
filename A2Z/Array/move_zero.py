nums=[1, 0, 2, 3, 0, 4, 0, 1]
k=0

for i in nums:
    if i>0:
        nums[k]=i
        k+=1

for j in range(k,len(nums)):
    nums[j]=0

print(nums)


