# Linked list intersection
from singly_linkedlist import LinkedList


def get_length(llist):
    count = 0
    current = llist.head

    while current:
        count += 1
        current = current.next

    return count


def fast_fwd(node, distance):

    while distance > 0:
        distance -= 1
        node = node.next

    return node


def intersection(llist1, llist2):
    if not llist1 or not llist2:
        return 'Invalid Entry'

    len_1 = get_length(llist1)
    len_2 = get_length(llist2)

    curr_1 = llist1.head
    curr_2 = llist2.head

    if len_1 > len_2:
        curr_1 = fast_fwd(curr_1, len_1 - len_2)
    elif len_1 < len_2:
        curr_2 = fast_fwd(curr_2, len_2 - len_1)

    while curr_1 is not curr_2:
        curr_1 = curr_1.next
        curr_2 = curr_2.next

    if not curr_1 or not curr_2:
        return False

    if curr_1 is curr_2:
        return True

    return False


list1 = LinkedList()
list2 = LinkedList()
list3 = LinkedList()

list3.insert(1)
list3.insert(2)
list3.insert(3)
list3.insert(4)
list3.insert(5)

list2.insert_list(list3)

list1.insert(1)
list1.insert(2)
list1.insert_list(list3)
print(intersection(list1, list2))
