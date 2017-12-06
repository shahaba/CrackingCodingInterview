# Sum Lists
from singly_linkedlist import LinkedList


def get_length(llist):
    count = 0
    current = llist.head

    while current:
        count += 1
        current = current.next

    return count


def add_padding(llist1, llist2, is_fwd):
    len_1 = get_length(llist1)
    len_2 = get_length(llist2)

    if len_1 > len_2:
        pad_list(llist2, len_1 - len_2, is_fwd)
    elif len_1 < len_2:
        pad_list(llist1, len_2 - len_1, is_fwd)
    else:
        return


def pad_list(llist, padding, is_fwd):

    while padding > 0:
        if is_fwd:
            llist.insert_front(0)
        else:
            llist.insert_end(0)
        padding -= 1


def sum_lists_fwd(llist1, llist2):
    add_padding(llist1, llist2, True)

    sum_list = LinkedList()

    carry = add_sum_fwd(llist1.head, llist2.head, 0, sum_list)

    if carry == 1:
        sum_list.insert_front(1)

    return sum_list


def add_sum_fwd(node1, node2, carry, sum_list):

    if node1.next and node2.next:
        carry = add_sum_fwd(node1.next, node2.next, 0, sum_list)

    sum_node = node1.value + node2.value + carry

    carry = sum_node // 10
    sum_list.insert_front(sum_node % 10)

    return carry


def sum_lists_bwd(llist1, llist2):
    add_padding(llist1, llist2, False)

    sum_list = LinkedList()

    add_sum_bwd(llist1.head, llist2.head, 0, sum_list)

    return sum_list


def add_sum_bwd(node1, node2, carry, sum_list):

    if not node1 or not node2:
        return

    sum_node = carry + node1.value + node2.value

    sum_list.insert_front(sum_node % 10)
    carry = sum_node // 10

    add_sum_bwd(node1.next, node2.next, carry, sum_list)


ex1 = LinkedList()
ex1.insert_front(7)
ex1.insert_front(1)
ex1.insert_front(6)
ex1.insert_front(1)

ex2 = LinkedList()
ex2.insert_front(5)
ex2.insert_front(9)
ex2.insert_front(2)

ex3 = LinkedList()
ex3.insert_end(7)
ex3.insert_end(1)
ex3.insert_end(6)
ex3.insert_end(1)

ex4 = LinkedList()
ex4.insert_end(5)
ex4.insert_end(9)
ex4.insert_end(2)

print('fwd:', ex1, ex2, 'bwd:', ex3, ex4)
print(sum_lists_fwd(ex1, ex2))
print(sum_lists_bwd(ex3, ex4))
