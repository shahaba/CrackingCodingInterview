# using a hash list to store the values
def findMissing(lst1, lst2):

    ints = {}

    # first store the elements in the list with missing
    for num in lst2:
        if num in ints:
            ints[num] += 1
        else:
            ints[num] = 1

    missing = []

    # then substract the true list from missing list to find elemen
    for num in lst1:
        # if there is an element missing, return
        if num not in ints or ints[num] == 0:
            missing.append(num)
        else:
            ints[num] -= 1

    return missing

# using XOR to find missing element, but only works in the case of 1 missing element
def findMissingOpt(lst1, lst2):

    result = 0

    # i think this works because if there is only 1 missing value, if we xor with every element in the combined arrays
    # result will be unbalanced by the missing element
    for num in lst1 + lst2:
        result ^= num

    return result


lst1 = [1, 2, 3, 4, 5, 6, 7, 8]
lst2 = [3, 7, 2, 1, 6, 4]

print(findMissing(lst1, lst2))