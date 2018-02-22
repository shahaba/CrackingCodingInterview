
def permutate(string, permutations, index):
    # End case
    if index == len(string):
        return permutations

    # Avoid aliasing list
    perm_copy = permutations.copy()

    # Iterate and append
    for perm in perm_copy:
        permutations.append(perm + string[index])

    return permutate(string, permutations, index + 1)


if __name__ == '__main__':
    string = 'abcd'
    print(permutate(string, [''], 0))
