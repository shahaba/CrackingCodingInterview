# implement a queue using 2 stacks
class Queue:

    # initialize stacks
    def __init__(self):
        self.stackPush = []
        self.stackPop = []

    # push item onto stack
    def enqueue(self, item):
        # if pop stack is not empty
        while self.stackPop != []:
            self.stackPush.append(self.stackPop.pop())

        # append item to push stack
        self.stackPush.append(item)

    # return top item from pop stack
    def dequeue(self):
        # if push stack is not empty
        while self.stackPush != []:
            self.stackPop.append(self.stackPush.pop())

        return self.stackPop.pop()

    # check if the queue is empty
    def isEmpty(self):
        return self.stackPush == [] and self.stackPop == []


queue = Queue()
for i in range(5):
    queue.enqueue(i)

for i in range(2):
    print(queue.dequeue())

queue.enqueue(3)
while not queue.isEmpty():
    print(queue.dequeue())