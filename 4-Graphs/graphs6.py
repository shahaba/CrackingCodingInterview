# Successor: find the "next" node in succession, where each node has a link to its parent
from BinarySearch import BinarySearchTree


def leftMostChild(node):
    if node is None:
        return None

    while node.left is not None:
        node = node.left

    return node


def getSuccessor(node):
    if node is None:
        return None

    if node.right is not None:
        return leftMostChild(node.right)
    else:
        q = node
        x = q.parent

        while x is not None and x.left is not q:
            q = x
            x = x.parent

        return x


if __name__ == '__main__':

    # initialize BST
    bst = BinarySearchTree()
    bst.insert(list(range(1, 10)))
    print(bst)
