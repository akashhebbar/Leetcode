import heapq

nums = [3, 2, 1, 5, 6, 4]
k = 2


def findKthLargest(nums, k):
    if not nums:
        return 0
    heap = []
    for i in nums:
        heapq.heappush(heap, i)
        if len(heap) > k:
            heapq.heappop(heap)
    return heapq.heappop(heap)


print(findKthLargest(nums, k))
# this is a min heap and since we are removing smallest node from the heap root each time the lenght
# exceeds k, at the end of the loop we'll be having the largest element at the root of the heap, just pop and return
