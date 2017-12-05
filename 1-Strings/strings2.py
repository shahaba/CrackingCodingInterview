# Q: Given two strings, decide if one is a permutation of the other

# using extra DS --> O(n) time, plus extra space
def isPermutationDS(str1, str2):

    if len(str1) != len(str2) or str1 == str2:
        return 'NO'

    permutation = [i for i in str1]

    for i in str2:
        try:
            permutation.remove(i)
        except ValueError:
            return 'NO'

    if len(permutation) == 0:
        return 'YES'

    return 'NO'


# O(n log n) if we can sort strings and then compare. requires moding strings
def isPermutationSort(str1, str2):
    if len(str1) != len(str2) or str1 == str2:
        return 'NO'

    str1 = ''.join(sorted(str1))
    str2 = ''.join(sorted(str2))

    if str1 == str2:
        return 'YES'

    return 'NO'


str1 = 'abs'
str2 = 'asb'
str3 = 'absdcdsdfs'
str4 = 'bsa'
print(isPermutationDS(str1, str2))
print(isPermutationDS(str1, str3))
print(isPermutationDS(str1, str4))
print(isPermutationSort(str1, str2))
print(isPermutationSort(str1, str3))
print(isPermutationSort(str1, str4))
