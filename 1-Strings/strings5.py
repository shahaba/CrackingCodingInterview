# One Away: using 3 types of edits, find if two strings are 1 edit away from
# each other
# Ex pale, ple = True
# pales, pale = True
# pale, bale = True
# pale, bake = True


def oneAwayDS(str1, str2):
    if abs(len(str1) - len(str2)) >= 2:
        return False

    if str1 == str2:
        return True

    chars = [0] * 26

    for i in str1:
        index = ord(i) - 97
        chars[index] += 1

    for i in str2:
        index = ord(i) - 97
        chars[index] -= 1

    sum_chars = 0
    for i in chars:
        if i >= 2:
            return False
        sum_chars += i

    if sum_chars <= 1:
        return True

    return False


def oneAwayNDS(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    if str1 == str2:
        return True

    if len(str1) >= len(str2):
        s1 = str1
        s2 = str2
    else:
        s1 = str2
        s2 = str1

    index1 = 0
    index2 = 0
    diffFound = False
    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            if(diffFound):
                return False
            diffFound = True
        index2 += 1
        index1 += 1

    return True


pale = 'pale'
ple = 'bae'
oneAwayDS(pale, ple)
oneAway(pale, ple)
