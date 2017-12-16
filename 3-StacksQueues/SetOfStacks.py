from Node import Node


class SetOfStacks:

    def __init__(self):
        self.head = None
        self.size = 1

    def push(self, item):
        if self.isEmpty():
            self.head = Node(item)
            return

        temp = self.head
        self.head = Node(item)
        self.head.next = temp

    def pop(self):
        if self.isEmpty():
            return 'Empty'

        temp = self.head
        self.head = self.head.next

        return temp.value

    def peek(self):
        return self.head if not self.isEmpty() else 'Empty'

    def isEmpty(self):
        return self.head is None
