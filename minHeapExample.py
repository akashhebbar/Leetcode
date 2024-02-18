import heapq

data = [5, 3, 8, 4, 2]

heapq.heapify(data)

heapq.heappush(data, 10)

min_item = heapq.heappop(data)

print("min_item:", min_item)
min_item = heapq.heappop(data)

print("min_item:", min_item)