from Node import SNode

class SinglyLL:

    def __init__(self, val=None):
        self.head = None

    def insert(self, val):
        if not self.head:
            self.head = SNode(val)

        temp = self.head
        self.head = SNode(val)
        self.head.nextnode = temp
