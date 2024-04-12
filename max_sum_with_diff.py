nums=[4, 6, 2, 7, 9, 8 ]

nums.sort(reverse=True)
count=0
ans=''
for i in range(0,len(nums),2):
    count+=1
    ans+=str(nums[i])

print(ans)



print(nums)