# At each Depth, create a linked list
from Queue import Queue
from BinarySearch import BinarySearchTree
from LinkedList import LinkedList

def depthLL(setOfLL, parents, lvl):

    while not parents.isEmpty():
        children = Queue()
        lvl += 1

        while not parents.isEmpty():
            current = parents.dequeue()

            # If lvl is not present in Dictionary
            if lvl in setOfLL:
                setOfLL[lvl].insert(current)
            else:
                n_ll = LinkedList()
                n_ll.insert(current)

                setOfLL[lvl] = n_ll

            # Enqueue its children
            if current.left:
                children.enqueue(current.left)

            if current.right:
                children.enqueue(current.right)

        parents = children

    return setOfLL


# Create LL of nodes @ each depth
def listOfDepths(root):

    if root is None:
        return

    lvl = 0  # tracking current depth
    setOfLL = {}  # List of LL, at each depth
    parents = Queue()  # Parent queue

    # Insert root @ lvl 0
    root = LinkedList()
    root.insert(bst.root)

    setOfLL[lvl] = root

    # Enqueue its children
    parents.enqueue(bst.root.left)
    parents.enqueue(bst.root.right)

    return depthLL(setOfLL, parents, 0)

if __name__ == '__main__':

    # Create binary search tree to be used
    bst = BinarySearchTree()
    lst = list(range(1, 10))
    bst.insert(lst)
    print(bst)

    setLL = listOfDepths(bst.root)

    for ll in setLL:
        print(setLL[ll])
