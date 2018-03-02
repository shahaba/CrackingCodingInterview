# scan array, only reseting sum when <= 0
# keeping track of start and stop
def largestContinuousSum(arr):

    if len(arr) == 0:
        return 0

    maxSum = sums = 0
    start = stop = 0

    for index, val in enumerate(arr):

        sums += val

        if sums <= 0:
            start = index + 1
            sums = 0
        elif sums > maxSum:
            stop = index
            maxSum = sums

    return maxSum, [start, stop]


arr1 = [-1, 1]
print(largestContinuousSum(arr1))

arr2 = [1, 2, -1, 3, 4, 10, 10, -10, -1]
print(largestContinuousSum(arr2))

arr3 = [-1, -3, 5, 10, -10, -3, -2, 10, 15]
print(largestContinuousSum(arr3))