# Queues via Stacks: implement queue using 2 stack
from StackQueue import StackQueue


myQueue = StackQueue()

myQueue.push(1)
myQueue.push(2)
myQueue.push(3)
print(myQueue.pop())
myQueue.push(4)
print(myQueue.pop())
print(myQueue.pop())
print(myQueue.pop())
