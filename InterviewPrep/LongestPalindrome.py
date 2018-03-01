""" Given an input string, find the longest associated palindrome

    ex 'abad' --> 'aba' or 'ada'
    ex 'abcabcab' --> 'acaca' or 'bcbcb'

    Algo:
        1) check length of string doesn't fall in to {} or 1 letter case
                if < 1, return to user
        2) create a hash table to count letter frequency as it appears in input string
        3) check if letters in string fall into one of the two catagories:
                a) is palindrome if all freq are even, or there exist just one odd # frequency

"""

def longestPalindrome(inputStr):

    # if string is empty or only has one letter,
    # already is longest palindrome
    if len(inputStr) <= 1:
        return inputStr

    letter_freq = {}  # store letter freq in Hash Table

    # generate frequency count for letters in inputStr
    for letter in inputStr:
        if letter in letter_freq:
            letter_freq[letter] += 1
        else:
            letter_freq[letter] = 1


    # check if hash table can make palindrome
    return checkIsPalindrome(letter_freq)

def checkIsPalindrome(letter_freq):

    oddLetter, outputL, outputR = None, [], []

    for letter, freq in letter_freq.items():

        # if even freq
        if freq % 2 == 0:
            temp = letter * (freq // 2)
            outputL.append(temp)
            outputR.insert(0, temp)
        elif not oddLetter:
            oddLetter = letter

    if oddLetter:
        output = outputL + [oddLetter] + outputR
    else:
        output = outputL + outputR

    return ''.join(output)



def longestSubStringPalindrome(inputStr):
    """ Expanding around center of letter to check if it a palindrome
    """

    # check if the string is a single letter
    if len(inputStr) <= 1:
        return inputStr

    start, end = 0, 0

    for index in range(len(inputStr)):
        # check for valid palindromes
        lenOdd = expandedAroundCenter(index, index, inputStr)
        lenEven = expandedAroundCenter(index, index + 1, inputStr)
        maxLen = max(lenOdd, lenEven)

        # if the new substring is > previous substring
        if maxLen > end - start:
            start = index - (maxLen - 1) // 2
            end = index + (maxLen) // 2


    return inputStr[start + 1:end]


# Expand a the given indicies around a specified letter
def expandedAroundCenter(left, right, inputStr):

    while left >= 0 and right < len(inputStr) and inputStr[left] == inputStr[right]:
        left -= 1
        right += 1

    return right - left + 1