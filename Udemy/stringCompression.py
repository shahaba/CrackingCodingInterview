
def compress(s):

    if len(s) == 0:
        return ''

    # if the compressed string > string, return string
    if len(set(s)) == len(s):
        return s

    curr, output = s[0], ''
    count = index = 1

    while index < len(s):

        if s[index] == curr:
            count += 1
        else:
            output += curr + str(count)
            count = 1
            curr = s[index]

        index += 1

    if curr != '':
        output += curr + str(count)

    return output


s = 'AAABCCDDDDD'
print(compress(s))
