from Node import TreeNode
from Queue import Queue


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def __str__(self):
        bst = []
        height = 0
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.isEmpty():
            curr = queue.dequeue()
            bst.append(str(curr.value))
            height = max(curr.height, height)

            if curr.left:
                queue.enqueue(curr.left)

            if curr.right:
                queue.enqueue(curr.right)

        return ' '.join(bst) + ' Height: ' + str(height)

    def insert(self, lst):
        self.root = self.insertList(self.root, lst, 0, 1, None)

    def insertList(self, current, lst, height, depth, parent):
        length = len(lst)

        if length == 0:
            return None
        elif length == 1:
            return TreeNode(lst[0], height, height + 1)

        if length % 2 == 0:
            mid = (length // 2) - 1
        else:
            mid = length // 2

        current = TreeNode(lst[mid], height, height + 1)
        current.parent = parent

        current.left = self.insertList(current.left, lst[:mid], height + 1, height + 2, current)
        current.right = self.insertList(current.right, lst[mid + 1:], height + 1, height + 2, current)

        return current

    def isEmpty(self):
        return self.root is None
