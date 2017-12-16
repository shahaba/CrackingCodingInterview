from Stack import Stack


class StackQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, item):
        if not self.s2.isEmpty():
            while not self.s2.isEmpty():
                self.s1.push(self.s2.pop())

        self.s1.push(item)

    def pop(self):
        if not self.s1.isEmpty():
            while not self.s1.isEmpty():
                self.s2.push(self.s1.pop())

        temp = self.s2.head
        self.s2.head = self.s2.head.next

        return temp.value

    def peek(self):
        return self.s1.head if not self.s1.isEmpty() else 'Empty'

    def isEmpty(self):
        return self.s1.isEmpty() and self.s2.isEmpty()
