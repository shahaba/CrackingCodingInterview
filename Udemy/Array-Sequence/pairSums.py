# find all the unique pairs of ints that add to a value k

def pairSumsDS(arr, k):

    if len(arr) < 2:
        return 0

    seen, output = set(), set()

    for num in arr:

        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))

    return len(output)


# find all pair sums without extra space
def pairSumsNoDS(arr, target):

    if len(arr) < 2:
        return 0

    arr.sort()

    start, end = 0, len(arr) - 1
    numPairs = 0

    if (arr[end-1] + arr[end]) < target or arr[start] == target:
        return 0

    while start < end:

        sums = arr[start] + arr[end]

        if sums == target:
            numPairs += 1


        if sums > target:
            end = getNextIndex(end, -1, arr)
        else:
            start = getNextIndex(start, 1, arr)

    return numPairs


def getNextIndex(curr, incr, arr):

    while curr > 0 and curr < len(arr) - 1 and arr[curr] == arr[curr+incr]:
        curr += incr

    return curr+incr


arr = [1, 2, 2, 3, 3, 4]
print(pairSumsNoDS(arr, 4), pairSumsDS(arr, 5))