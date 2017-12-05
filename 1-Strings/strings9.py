# String rotation: check if s2 is a rotation of s1, with only 1 call to
# substring


def isSubstring(s1, s2):
    if s1 is None or s2 is None:
        return False

    # length of s1 and s2 should match
    if len(s1) != len(s2):
        return False

    # assuming that if strings are the same, not a rotation
    if s1 == s2:
        return False

    # change s2 to that it is s2s2
    s2 = s2+s2

    return True if s2.find(s1) > 0 else False


s1 = 'hello'
s2 = 'lohen'
print(isSubstring(s1, s2))
