# create Queue using lists
class Queue:

    # initialize queue as list
    def __init__(self):
        self.items = []

    # enqueue items to end of list
    def enqueue(self, item):
        self.items.insert(0, item)

    # dequeue items from front of list using pop
    def dequeue(self):
        return self.items.pop() if not self.isEmpty() else None

    # return if list is empty
    def isEmpty(self):
        return self.items == []

    # get length of items
    def size(self):
        return self.__size()

    def __size(items):
        return len(items)

queue = Queue()
print(queue.size())

