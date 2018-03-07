# structures for different node types

# singly linked list node structure
class SNode:

    # value and next
    def __init__(self, val=None):
        self.val = val
        self.nextnode = None


# doubly linked list node structure
class DNode:

    def __init__(self, val=None):
        self.val = val
        self.nextnode = None
        self.prevnode = None


# tree node structure
class TreeNode:

    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# binary tree node structure
class BinaryTreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right