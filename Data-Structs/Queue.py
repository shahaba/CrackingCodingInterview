# queue structure framework
import Node

class Queue:

    def __init__(self):
        self.head = None
        self.end = None


    def enqueue(self, value):

        if self.isEmpty():
            self.head = Node(value)
            self.end = self.head
            return


        temp = self.head
        self.head = Node(value)
        temp.next = self.head


    def dequeue(self):

        if self.isEmpty():
            return 'Empty'

        temp = self.end
        self.end = self.end.next

        return temp


    def isEmpty(self):
        return self.head is None


