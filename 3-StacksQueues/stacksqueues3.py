# Stack of Plates: stack within a stack
from Stack import Stack
from SetOfStacks import SetOfStacks


def push(stack_set, item):

    if stack_set.isEmpty():
        new_stack = Stack()
        new_stack.push(item)
        stack_set.push(new_stack)
        return

    current = stack_set.pop()

    if current.size == 10:
        stack_set.size += 1
        stack_set.push(current)
        current = Stack()

    current.push(item)
    stack_set.push(current)


def pop(stack_set):

    if stack_set.isEmpty():
        return 'Empty'

    current = stack_set.pop()

    if current.isEmpty():
        if not stack_set.isEmpty():
            current = stack_set.pop()
            stack_set.size -= 1
        else:
            return 'Empty'

    temp = current.pop()
    stack_set.push(current)

    return temp


stack_set = SetOfStacks()

push(stack_set, 1)
push(stack_set, 2)
push(stack_set, 3)
push(stack_set, 4)
push(stack_set, 5)
push(stack_set, 6)
push(stack_set, 7)
push(stack_set, 8)
push(stack_set, 9)
push(stack_set, 10)
push(stack_set, 11)
print(pop(stack_set))
print(stack_set.size)
print(pop(stack_set))
print(stack_set.size)
