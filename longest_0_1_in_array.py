# nums=[0, 0, 1, 0, 1, 0, 0]
#
# def findLargest(nums):
#     d={}
#     d[0]=-1
#
#     lenght=0
#     ending_index=-1
#     total =0
#     for i in range(len(nums)):
#         total+= 1 if nums[i] ==0 else 1
#         if total in d:
#             