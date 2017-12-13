# Keeping track of min node in Stack
from Stack import Stack


stack = Stack()
stack.push(1)
stack.push(2)
stack.push(-1)
print(stack.head.get_min())
stack.pop()
print(stack.head.get_min())
stack.pop()
print(stack.head.get_min())
stack.pop()
print(stack.head.get_min())
