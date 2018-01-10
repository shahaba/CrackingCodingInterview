from Node import Node


class Queue:

    def __init__(self):
        self.head = None
        self.end = None

    def enqueue(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.end = self.head
            return

        temp = self.end
        self.end = Node(item)
        temp.next = self.end

    def dequeue(self):
        if self.isEmpty():
            return None

        temp = self.head
        self.head = self.head.next

        return temp.value

    def peek(self):
        return self.head

    def isEmpty(self):
        return True if not self.head else False
