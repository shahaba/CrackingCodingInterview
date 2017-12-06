# Return kth to Last of singly LL
from singly_linkedlist import LinkedList


# get length of linked list
def get_length(node, count):
    if not node:
        return count

    return get_length(node.next, count + 1)


# recusively find kth element
def recurse(node, kth):
    if kth == 0:
        return node.value

    return recurse(node.next, kth - 1)


# Using two counters, traverse the list
def return_kth_to_last(linkedlist, kth):
    if not linkedlist:
        return 'Empty Input List'
    elif kth < 0:
        return 'Not valid entry for k'

    fast = linkedlist.head
    end = 1

    while fast.next:
        fast = fast.next
        end += 1
        if fast.next:
            end += 1
            fast = fast.next

    kth_node = (end - kth)

    if kth_node < 0:
        return 'K is larger than input list'

    current = linkedlist.head
    while kth_node != 0:
        current = current.next
        kth_node -= 1

    return str(current.value)


# setup linked list
ll_1 = LinkedList()
ll_1.insert(1)
ll_1.insert(2)
ll_1.insert(3)
ll_1.insert(4)

# iterative approach
print(return_kth_to_last(ll_1, 1))
print(return_kth_to_last(None, 1))
print(return_kth_to_last(ll_1, 5))

# recursive approach
length = get_length(ll_1.head, 0)
kth = 1
kth_node = recurse(ll_1.head, length - kth)
print(kth_node)
