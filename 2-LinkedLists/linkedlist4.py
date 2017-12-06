# Partition list at node with value x
from singly_linkedlist import LinkedList


# partition list at value x
def partiton(root, x):
    left = []
    right = []

    current = root

    while current:
        if current.value >= x:
            right.append(current.value)
        else:
            left.append(current.value)

        current = current.next

    return combine(left, right)


def combine(left, right):
    combined_list = LinkedList()

    for node in right:
        combined_list.insert(node)

    for node in left:
        combined_list.insert(node)

    return combined_list


ex = LinkedList()
ex.insert(1)
ex.insert(2)
ex.insert(10)
ex.insert(5)
ex.insert(8)
ex.insert(5)
ex.insert(3)
ex.insert(6)
ex.insert(4)
ex.insert(3)
part = partiton(ex.head, 5)
print(part)
part = partiton(ex.head, 4)
print(part)
