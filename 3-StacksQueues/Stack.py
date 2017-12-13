from Node import Node


class Stack:

    def __init__(self):
        self.head = None
        self.capacity = 10
        self.size = 0

    def push(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.head.set_min(value)
            self.size += 1
            return

        self.size += 1
        temp = self.head

        # When stack is at capacity
        if self.size >= self.capacity:
            self.head = Stack()
            self.head.push(value)
        else:
            self.head = Node(value)

        self.head.next = temp

    def pop(self):
        if self.is_empty():
            return 'Empty'

        print(type(self.head))
        if isinstance(self.head, Stack):
            return 'is class'

        temp = self.head
        self.head = self.head.next
        self.size -= 1

        return temp.value

    def peek(self):
        return self.head

    def is_empty(self):
        return self.head is None
