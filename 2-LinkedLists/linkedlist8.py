# Loop Detection
from singly_linkedlist import LinkedList


def find_loop(slow, fast):
    # length = 0
    #
    # while fast is not slow:
    #     length += 1
    #     fast = fast.next
    #
    # slow = llist.head
    #
    # for i in range(length):
    #     slow = slow.next
    #
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return fast.value


def is_loop(llist):
    if llist is None:
        return 'Empty'

    slow = llist.head
    fast = llist.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if slow is fast:
            break

    if not fast or not fast.next:
        return 'Not Circular'

    return find_loop(llist.head, fast)


loop_list = LinkedList()
loop_list.insert_end('C')
loop_list.insert_end('D')
loop_list.insert_end('E')
loop_list.end.next = loop_list.head

llist = LinkedList()
llist.insert('A')
llist.insert_end('B')
llist.insert_end('Z')
llist.end.next = loop_list.head

print(is_loop(llist))

norm_list = LinkedList()
norm_list.insert('D')
norm_list.insert('C')
norm_list.insert('B')
norm_list.insert('A')
print(is_loop(norm_list))
