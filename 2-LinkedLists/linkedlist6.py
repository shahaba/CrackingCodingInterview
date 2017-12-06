# Palindrome: check if a list is a palindrome
from dbly_linkedlist import LinkedList as dbly
from singly_linkedlist import LinkedList as singly


def get_length(llist):
    slow = llist.head
    fast = slow
    count = 0
    left = [llist.head.value]

    while fast.next:
        fast = fast.next
        count += 1
        if fast.next:
            slow = slow.next
            left.append(slow.value)
            count += 1
            fast = fast.next

    return (count, left, slow.next)


def is_palindrome_dbly(llist):

    head = llist.head
    end = llist.end

    while head is not end and head.next is not end:
        if head.value != end.value:
            return False

        head = head.next
        end = end.prev

    return True


def is_palindrome_singly(llist):
    (length, left, current) = get_length(llist)

    if length % 2 == 0:
        left.pop()

    while current:
        if left.pop() != current.value:
            return False

        current = current.next

    return True


palin = dbly()
palin.insert(1)
palin.insert(2)
palin.insert(3)
palin.insert(3)
palin.insert(2)
palin.insert(1)
print(is_palindrome_dbly(palin))

palind = singly()
palind.insert(1)
palind.insert(2)
palind.insert(3)
palind.insert(4)
palind.insert(3)
palind.insert(2)
palind.insert(1)
print(is_palindrome_singly(palind))
