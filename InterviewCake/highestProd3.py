# given a list of integers, find the highest product of 3 elements
def highestProdOf3(arr):

    if len(arr) < 3:
        return 0

    highest = max(arr[0], arr[1])
    lowest = min(arr[0], arr[1])

    highestProd2 = arr[0] * arr[1]
    lowestProd2 = arr[0] * arr[1]

    highestProd3 = arr[0] * arr[1] * arr[2]

    for i in range(2, len(arr)):

        current = arr[i]

        highestProd3 = max(highestProd3, current * highestProd2, current * lowestProd2)

        highestProd2 = max(highestProd2, current * highest, current * lowest)
        lowestProd2 = min(lowestProd2, current * highest, current * lowest)

        highest = max(highest, current)
        lowest = min(lowest, current)


    return highestProd3

# Follow ups - Highest of 4 and Highest of K...

lstInt = [1, 10, -5, 1, -100]
print(highestProdOf3(lstInt))
