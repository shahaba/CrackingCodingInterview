from node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.end = None

    def __str__(self):
        ll_str = []
        current = self.head

        while current:
            ll_str.append(str(current.value))
            current = current.next

        return ' '.join(ll_str)

    def insert(self, value):
        if not self.head:
            self.head = Node(value)
            self.end = self.head
            return

        temp = self.head
        self.head = Node(value)
        temp.prev = self.head
        self.head.next = temp

    def insert_end(self, value):
        if not self.head:
            self.head = Node(value)
            self.end = self.head
            return

        temp = self.end
        self.end = Node(value)
        self.end.prev = temp
        temp.next = self.end
