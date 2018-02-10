# Validate Binary Search Tree
from BinarySearch import BinarySearchTree
from Node import TreeNode
from Queue import Queue


def checkRoot(root, queue):

    if root.left:
        if root.left.value < root.value:
            queue.enqueue(root.left)
        else:
            return False

    if root.right:
        if root.right.value > root.value:
            queue.enqueue(root.right)
        else:
            return False

    return True


def validate(root):
    leftQ = Queue()
    rightQ = Queue()
    min_val = root.value
    max_val = root.value

    leftQ.enqueue(root.left)
    rightQ.enqueue(root.right)

    while not leftQ.isEmpty() and not rightQ.isEmpty():
        left = leftQ.dequeue()
        right = rightQ.dequeue()

        if left and left.value < min_val:
            max_val = max(max_val, left.value)

            if not checkRoot(left, leftQ):
                return False
        else:
            return False

        if right and right.value > max_val:
            min_val = min(min_val, right.value)

            if not checkRoot(right, rightQ):
                return False
        else:
            return False

    return True


if __name__ == '__main__':

    bt1 = BinarySearchTree()
    bt1.insert(list(range(1, 100)))
    print(validate(bt1.root))

    bt2 = BinarySearchTree()
    bt2.root = TreeNode(5, 0, 0)
    bt2.root.left = TreeNode(2, 0, 0)
    bt2.root.right = TreeNode(1, 0, 0)
    print(validate(bt2.root))

    bt3 = BinarySearchTree()
    bt3.root = TreeNode(5, 0, 0)
    bt3.root.left = TreeNode(2, 0, 0)
    bt3.root.left.right = TreeNode(7, 0, 0)
    bt3.root.right = TreeNode(8, 0, 0)
    bt3.root.right.right = TreeNode(9, 0, 0)
    bt3.root.right.left = TreeNode(6, 0, 0)
    print(validate(bt3.root))
