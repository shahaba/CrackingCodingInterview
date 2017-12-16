# Sort Stack
from SortStack import SortStack


if __name__ == '__main__':

    sorted = SortStack()

    sorted.push(9)
    sorted.push(3)
    sorted.push(1)
    sorted.push(7)

    sorted.sortStack()
    print(sorted.pop())
