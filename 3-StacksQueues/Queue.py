from Node import Node


class Queue:

    def __init__(self):
        self.head = None
        self.end = None

    def enqueue(self, value):
        if self.is_empty():
            self.head = Node(value)
            self.end = self.head
            return

        temp = self.end
        self.end = Node(value)
        temp.next = self.end

    def dequeue(self):
        if self.is_empty():
            return 'Empty'

        temp = self.head
        self.head = self.head.next
        return temp.value

    def peek(self):
        if self.isEmpty():
            return 'Empty'

        return self.head.value

    def is_empty(self):
        return self.head is None
