# anagram checker

def isAnagram(s1, s2):

    wordFreq = {}

    for letter in s1:
        if letter is " ":
            continue
        elif letter in wordFreq:
            wordFreq[letter] += 1
        else:
            wordFreq[letter] = 1

    for letter in s2:
        if letter == " ":
            continue
        elif not wordFreq or letter not in wordFreq:
            return False
        elif letter in wordFreq:
            wordFreq[letter] -= 1

            if wordFreq[letter] == 0:
                del wordFreq[letter]

    print(wordFreq)

    return True if not wordFreq else False

if __name__ == '__main__':

    word1 = 'public relations'
    word2 = 'crap built on lies'
    print(isAnagram(word1, word2))