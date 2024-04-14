from collections import deque

# Create an empty deque
my_deque = deque()

# Append elements to the right end of the deque
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# Append elements to the left end of the deque
my_deque.appendleft(0)
my_deque.appendleft(-1)

print("Deque:", my_deque)

# Pop elements from the right end of the deque
popped_element = my_deque.pop()
print("Popped element from the right end:", popped_element)

# Pop elements from the left end of the deque
popped_element = my_deque.popleft()
print("Popped element from the left end:", popped_element)

print("Updated deque:", my_deque)
