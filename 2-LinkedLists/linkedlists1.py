# RemoveDups: Remove duplicates from unsorted LinkedList:


# Node object
class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


# Linked List Object
class SLinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return 'Empty'

        sll_str = []
        current = self.head

        while current:
            sll_str.append(str(current.value))
            current = current.next

        return ', '.join(sll_str)

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        temp = self.head
        self.head = Node(value)
        self.head.next = temp


# delete Node
def delNode(current, prev):
    prev.next = current.next
    return prev


# if we are allowed to use extra space
def removeDupsDS(head):

    prev = None
    current = head
    seen = {}

    while current:
        if current.value in seen:
            current = delNode(current, prev)
        else:
            seen[current.value] = True

        prev = current
        current = current.next


# If not allowed to use extra space
def removeDupsNoDS(head):

    current = head
    next = current.next

    while current and next:
        if current.value == next.value:
            delNode(next, current)
        else:
            current = current.next

        if next:
            next = next.next


sll1 = SLinkedList()
sll2 = SLinkedList()
sll1.insert(0)
sll1.insert(1)
sll1.insert(2)
sll1.insert(3)
sll1.insert(3)
sll1.insert(3)
sll1.insert(4)
sll1.insert(4)
sll2.insert(4)
sll2.insert(4)
sll2.insert(3)
sll2.insert(2)
sll2.insert(2)
sll2.insert(1)
sll2.insert(1)
sll2.insert(0)
print(sll1)
removeDupsDS(sll1.head)
print(sll1)


print(sll2)
removeDupsNoDS(sll2.head)
print(sll2)
