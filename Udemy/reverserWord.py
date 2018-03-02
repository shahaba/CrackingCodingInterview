# reverse the input word

def reverseWordOpt(s):

    s = s.split()

    return ' '.join([word for word in reversed(s)])

# if i can't use the built in split function for strings
def reverseWord(s):

    if len(s) <= 0:
        return ''

    s = getWords(s)
    output = []

    for i in range(len(s) - 1, -1, -1):
        output.append(s[i])

    return ' '.join(output)

# replicated the split() function for strings
def getWords(s):

    curr, index, output = '', 0, []

    while index < len(s):

        if s[index] == ' ' and curr != '':
            output.append(curr)
            curr = ''
        elif s[index] != ' ':
            curr += s[index]

        index += 1

    if curr != '':
        output.append(curr)

    return output

s = '   this      is the best    line'
s = '1'
print(reverseWordOpt(s))