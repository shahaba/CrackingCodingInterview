# check if string is composed of unique characters
def uniqueChar(s):

    chars = set()

    for letter in s:
        if letter in chars:
            return False
        else:
            chars.add(letter)

    return True


def uniqueCharLoop(s):

    index = 1

    while index < len(s):

        if s[index-1] == s[index]:
            return False

        index += 1

    return True

s = 'aaabcde'
print(uniqueChar(s), uniqueCharLoop(s))