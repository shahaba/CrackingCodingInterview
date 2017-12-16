class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        self.min = None
        self.age = None

    def setMin(self, min_val):
        self.min = min_val

    def getMin(self):
        return self.min
