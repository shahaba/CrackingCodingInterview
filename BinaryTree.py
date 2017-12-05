class BinaryTrNode:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    # Insert value into Tree
    def insert(self, data):
        if self.root is None:
            self.root = BinaryTrNode(data)
            return

        self.insertR(self.root, data)

    # Not Balanced Tree
    def insertR(self, node, data):
        if data > node.data:
            if node.right is None:
                node.right = BinaryTrNode(data)
            else:
                self.insertR(node.right, data)
        elif data < node.data:
            if node.left is None:
                node.left = BinaryTrNode(data)
            else:
                self.insertR(node.left, data)

    # Remove from BinaryTree
    def remove(self, data):
        pass

    # Rebalancing Methods
    def rotate(self):
        pass

    # initiate recursive search
    def search(self, value):
        if self.root is None:
            return False

        self.searchR(self.root, value)

    # Recursive Search
    def searchR(self, node, value):
        if node is None or node.data == value:
            return node

        if node.data > value:
            return self.searchR(node.right, value)

        return self.searchR(node.left, value)

    # Iterative search
    def searchIterative(self, value):
        current = self.root

        while current:
            if current.data == value:
                return current
            elif current.data > value:
                current = current.right
            else:
                current = current.left

        return current if current else False

    # Depth First Search Methods:
    def inOrderTraversal(self, root):
        if root:
            self.inOrderTraversal(root.left)
            print(root.data)
            self.inOrderTraversal(root.right)

    def postOrderTraversal(self, root):
        if root:
            self.postOrderTraversal(root.left)
            self.postOrderTraversal(root.right)
            print(root.data)

    def preOrderTraversal(self, root):
        if root:
            print(root.data)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)

    # Bredth First Search Methods:


# class MyTest(unittest.TestCase):
#     bt = BinaryTree()
#
#     def test_insert(self):
#         self.assertEqual()
bt = BinaryTree()
bt.insert(2)
bt.insert(3)
bt.insert(1)
bt.insert(-1)
bt.insert(10)
print('In')
bt.inOrderTraversal(bt.root)
print('Pre')
bt.preOrderTraversal(bt.root)
print('Post')
bt.postOrderTraversal(bt.root)
