class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class TreeNode:

    def __init__(self, value, height, depth):
        self.value = value
        self.left = None
        self.right = None
        self.height = height
        self.depth = depth

    def __str__(self):
        return str(self.value)
