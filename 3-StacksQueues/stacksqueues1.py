# 3 in 1: 3 stacks in 1 array


class ThreeInOne:

    def __init__(self, size):
        self.arr = [0] * size
        self.capacity = size
        self.length = size // 3
        self.sizes = [0] * 3
        self.locs = [0, self.length, 2 * self.length]

    def push(self, stack, item):
        if self.isFull(stack):
            return 'Stack @ Capacity'

        indx = self.getIndex(stack) + 1

        if self.isEmpty(stack):
            indx -= 1

        self.arr[indx] = item
        self.setIndex(stack, indx)
        self.sizes[stack - 1] += 1

    def pop(self, stack):
        if self.isEmpty(stack):
            return 'Stack is Empty'

        indx = self.getIndex(stack)
        temp = self.arr[indx]
        self.arr[indx] = 0
        self.setIndex(stack, indx - 1)
        self.sizes[stack - 1] -= 1

        return temp

    def isFull(self, stack):
        return self.sizes[stack - 1] == self.length

    def isEmpty(self, stack):
        return self.sizes[stack - 1] == 0

    def getIndex(self, stack):
        return self.locs[stack - 1]

    def setIndex(self, stack, index):
        self.locs[stack - 1] = index
