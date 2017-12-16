# Keeping track of min node in Stack
from Stack import Stack


stack = Stack()
stack.push(1)
stack.push(20)
stack.push(-1)
stack.push(1400)
print(stack.size)
print('min', stack.getMin())
stack.pop()
print('min', stack.getMin())
