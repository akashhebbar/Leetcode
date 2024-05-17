class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, val):
        new_node = Node(val)
        new_node.next = self.top
        self.top = new_node

    def isEmpty(self):
        return self.top is None

    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            self.top = self.top.next

    def traverse(self):
        cur = self.top
        while cur is not None:
            print(cur.val)
            cur = cur.next


stack = Stack()
stack.pop()
stack.push(10)
stack.push(20)
stack.traverse()
stack.pop()
stack.isEmpty()
stack.traverse()
stack.isEmpty()
