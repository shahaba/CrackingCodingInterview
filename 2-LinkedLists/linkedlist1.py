# RemoveDups: Remove duplicates from unsorted LinkedList:
from singly_linkedlist import LinkedList


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


sll1 = LinkedList()
sll2 = LinkedList()
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
