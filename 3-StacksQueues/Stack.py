from Node import Node


class Stack:

    def __init__(self):
        self.head = None
        self.capacity = 10
        self.size = 1

    def push(self, item):
        # If stack is empty
        if self.isEmpty():
            # Insert first node
            self.head = Node(item)
            self.head.setMin(item)
            return

        # Insert new Node @ top of stack
        temp = self.head
        self.head = Node(item)
        self.head.next = temp
        self.size += 1

        # Update min value stored in Node
        if temp.min > item:
            self.head.setMin(item)
        else:
            self.head.setMin(temp.min)

    def pop(self):
        # If the stack is empty
        if self.isEmpty():
            return 'Empty'

        # Return top node
        temp = self.head
        self.head = self.head.next
        self.size -= 1

        return temp.value

    def peek(self):
        return self.head.value if self.head else None

    def isEmpty(self):
        return self.head is None

    def isFull(self):
        return self.size == self.capacity

    def getMin(self):
        return 'Empty' if self.head is None else self.head.getMin()
