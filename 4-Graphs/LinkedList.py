from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.end = None

    def __str__(self):
        ll_str = []
        curr = self.head

        while curr:
            ll_str.append(str(curr.value))
            curr = curr.next

        return ' '.join(ll_str)

    def insert(self, item):
        if self.isEmpty():
            self.head = Node(item)
            self.end = self.head
            return

        temp = self.end
        self.end = Node(item)
        temp.next = self.end

    def isEmpty(self):
        return self.head is None
