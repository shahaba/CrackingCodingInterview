from Node import Node


class MinStack:

    def __init__(self):
        self.head = None

    def push(self, value):
        if self.is_empty():
            return

        temp = self.head
        self.head = Node(value)
        self.head.next = temp

    def pop(self):
        if self.is_empty():
            return

        temp = self.head
        self.head = self.head.next
        return temp

    def peek(self):
        return self.head.value

    def is_empty(self):
        return self.head is None
