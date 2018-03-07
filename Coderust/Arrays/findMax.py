# Q2. Find maximum in Sliding Window

# using array
def findMax(lst, w):

    if w > len(lst) or len(lst) == 0:
        return None

    maxElm, index = 0, 0
    limit = len(lst) - w

    while index < limit:

        for i in range(index, index + w):
            maxElm = max(lst[i])

        index += w

    return maxElm


lst = [1, 2, 3, 4, 5, 6]
w = 3

print(findMax(lst, w))
