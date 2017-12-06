# Delete Middle Node: (any node but the first ad last nodes) of a singly linked list, give access to only that node
from singly_linkedlist import LinkedList


# delete the middle node by copying value to current and skipping next
def delete_mid_node(node):
    if not node.next:
        return 'Node can\'t be first or last element'

    nxt = node.next
    node.value = nxt.value
    node.next = nxt.next


ex = LinkedList()
ex.insert('f')
ex.insert('e')
ex.insert('d')
ex.insert('c')
ex.insert('b')
ex.insert('a')
print(ex)
delete_mid_node(ex.head.next)
print(ex)
