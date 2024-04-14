import queue

# Create a priority queue
priority_queue = queue.PriorityQueue()

# Put elements into the priority queue with a priority
priority_queue.put((3, 'Apple'))
priority_queue.put((1, 'Banana'))
priority_queue.put((2, 'Orange'))

# Get elements from the priority queue in order of priority
while not priority_queue.empty():
    priority, item = priority_queue.get()
    print("Priority:", priority, "- Item:", item)
