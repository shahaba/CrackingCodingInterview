# creating a deque, a hybrid stack-queue where we can remove and insert both
# at the front and the back
class DequeList:

    # initialize empty list as deque
    def __init__(self):
        self.items = []

    # return if the list is an empty list
    def isEmpty(self):
        return self.items == []

    # add to front of deuque
    def addFront(self, item):
        self.items.insert(0, item)

    # add to rear of deque
    def addRear(self, item):
        self.item.append(item)

    # remove item from front
    def removeFront(self):
        return self.items.pop(0) if not self.isEmpty() else None

    # remove item from rear
    def removeRear(self):
        return self.items.pop() if not self.isEmpty() else None

    # get size of list
    def size(self):
        return len(self.items)
