# Q1 in Arrays section
#   write the binary search algorithm

def search(lst, target):

    # given an input list
    lo, hi = 0, len(lst) - 1

    while hi > lo:

        mid = (hi + lo) // 2

        if lst[mid] == target:
            return mid
        elif lst[mid] > target:
            hi = mid - 1
        elif lst[mid] < target:
            lo = mid + 1

    return False


if __name__ == '__main__':

    target = 3
    lst = [1, 4, 5, 6, 7, 9]

    print(search(lst, target))
s
