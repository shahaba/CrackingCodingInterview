# stack structure framework
import Node

class Stack:

    def __init__(self):
        self.head = None


    def push(self, value):

        if self.isEmpty():
            self.head = Node(value)
            return

        temp = self.head
        self.head = Node(value)
        self.head.prev = temp


    def pop(self):

        if self.isEmpty():
            return 'Empty'

        temp = self.head
        self.head = self.head.prev

        return temp


    def isEmpty(self):
        return self.head is None