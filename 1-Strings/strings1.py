
def isUniqueDS(string):

    if len(string) == 0:
        return 'String can\'t be empty'

    if len(string) == 1:
        return True

    # using hash table
    unique = {}

    for i in string:
        if i in unique:
            return False
        else:
            unique[i] = 1

    return True


# without sorting
def isUniqueNDS(string):

    if len(string) == 0:
        return 'String can\'t be empty'

    if len(string) == 1:
        return True

    str_len = len(string)
    # if we can't sort
    for i in range(str_len):
        for j in range(i+1, str_len):
            if string[i] == string[j]:
                return False

    return True


# with sorting
def isUniqueSort(string):

    if len(string) == 0:
        return 'String can\'t be empty'

    if len(string) == 1:
        return True

    string.sort()

    for i in range(len(string)-1):
        if string[i] == string[i+1]:
            return False

    return True


case_1 = ['a', 'b', 'c', 'd']
case_2 = ['a', 'a']
case_3 = ['a']
case_4 = []
print(isUniqueDS(case_1))
print(isUniqueDS(case_2))
print(isUniqueDS(case_3))
print(isUniqueDS(case_4))
print(isUniqueNDS(case_1))
print(isUniqueNDS(case_2))
print(isUniqueNDS(case_3))
print(isUniqueSort(case_1))
print(isUniqueSort(case_2))
print(isUniqueSort(case_3))
