from Node import *


class Queue:

    def __init__(self):
        self.head = None
        self.end = None
        self.type = None

    def enqueue(self, value):
        if self.isEmpty():
            self.head = Node(value)
            self.end = self.head
            return

        temp = self.end
        self.end = Node(value)
        temp.next = self.end

    def enqueue(self, name, timestamp):
        if self.isEmpty():
            self.head = AnimalNode(name, timestamp)
            self.end = self.head
            return

        temp = self.end
        self.end = AnimalNode(name, timestamp)
        temp.next = self.end

    def dequeue(self):
        if self.isEmpty():
            return 'Empty'

        temp = self.head
        self.head = self.head.next
        return temp

    def peek(self):
        return None if self.isEmpty() else self.head

    def isEmpty(self):
        return self.head is None
