from Stack import Stack


class SortStack:

    def __init__(self):
        self.stack = Stack()
        self.extra_stack = Stack()

    def push(self, item):
        self.stack.push(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack.peek()

    def isEmpty(self):
        return self.stack.isEmpty()

    def sortStack(self):

        while not self.stack.isEmpty():
            tmp = self.stack.pop()

            if self.extra_stack.isEmpty():
                self.extra_stack.push(tmp)
                continue

            while not self.extra_stack.isEmpty() and self.extra_stack.peek() > tmp:
                self.stack.push(self.extra_stack.pop())

            self.extra_stack.push(tmp)

        while not self.extra_stack.isEmpty():
            self.stack.push(self.extra_stack.pop())
