# creating stack using lists
class Stack:

    # initialize list as stack
    def __init__(self):
        self.items = []

    # append item to the end of stack
    def push(self, item):

        self.items.append(item)

    # pop item from the end of stack
    def pop(self):

        return self.items.pop()

    # return the last element of stack, if not empty
    def peek(self):

        return self.items[-1] if not self.isEmpty() else None

    # return if the stack is empty
    def isEmpty(self):

        return self.items == []

    # return size of current stack
    def size(self):

        return len(self.items)
