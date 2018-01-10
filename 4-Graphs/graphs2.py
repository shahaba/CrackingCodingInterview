from BinarySearch import BinarySearchTree


if __name__ == '__main__':

    lst = list(range(1, 20))

    bst = BinarySearchTree()
    bst.insert(lst)
    print(bst)
