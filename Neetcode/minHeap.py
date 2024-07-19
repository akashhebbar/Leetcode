import heapq

numbers = [1, 2, 3, 4, 1, 3, 4, 3, 1, 33, 12, 1]
# numbers1 = [1, 2, 3, 4, 1, 3, 4, 3, 33, 12]
#
# heapq.heapify(numbers1)
# heapq._heapify_max(numbers)
# print(numbers)
#
# for i in range(0, 3):
#     print(heapq._heappop_max(numbers))
#
# print("*"*100)
# for i in range(0, 3):
#     print(heapq.heappop(numbers1))

heapq._heapify_max(numbers)
output=[heapq._heappop_max(numbers) for i in range(len(numbers))]

print(output)