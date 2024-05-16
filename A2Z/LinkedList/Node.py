class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n

    def insert_node(self, value):
        newnode = Node(value)

        newnode.next = self.head
        self.head = newnode

        self.n = self.n + 1

    def traverse(self):
        cur = self.head
        while cur != None:
            print("value", cur.value)
            cur = cur.next

    def insert_at_tail(self, value):
        new_node = Node(value)
        cur = self.head
        if self.head == None:
            self.head = new_node
            return
        while cur.next is not None:
            cur = cur.next

        cur.next = new_node


L = LinkedList()

L.insert_node(1)
L.insert_node(2)
# L.traverse()
L.insert_at_tail(5)
L.traverse()
print(L.n)
