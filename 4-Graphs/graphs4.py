# Check balance of binary tree. Height of 2 subtrees should never be more than 2
from BinarySearch import BinarySearchTree
from Node import TreeNode


def checkBalance(root):

    # Get height of left and right subtrees
    heightL = heightDFS(root.left, 1)
    heightR = heightDFS(root.right, 1)

    # Optimization - if any of the subtrees are not balanced
    if heightL is False or heightR is False:
        return False

    # Otherwise, it must be balanced
    return True


# Helper method - Recursive search subtrees
def heightDFS(root, height):
    # Base Case
    if root is None:
        return height

    heightL = heightDFS(root.left, height + 1)
    heightR = heightDFS(root.right, height + 1)

    # Check if L or R subtree are not balanced
    if heightL == False:
        return False

    if heightR == False:
        return False

    if abs(heightR - heightL) >= 2:
        return False

    # If height diff < 2, return max height between both subtrees
    return max(heightL, heightR)


if __name__ == '__main__':

    # Create unbalanced binary tree
    bt = BinarySearchTree()
    bt.root = TreeNode(7, 0, 0)
    bt.root.left = TreeNode(2, 0, 0)
    bt.root.right = TreeNode(9, 0, 0)
    bt.root.right.right = TreeNode(10, 0, 0)
    bt.root.right.right.right = TreeNode(11, 0, 0)

    # Create balanced binary tree
    bt2 = BinarySearchTree()
    bt2.insert(list(range(1, 10)))

    print(bt)

    if checkBalance(bt.root):
        print('1 Balanced')
    else:
        print('1 Not Balanced')

    if checkBalance(bt2.root):
        print('2 Balanced')
    else:
        print('2 Not Balanced')
