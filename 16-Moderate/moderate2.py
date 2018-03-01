""" Word Frequency: Design a method to find the frequency of occurences of a given word in a book. What if we were running the algo multiple times
"""

def wordFrequency(book, findWord):

    # check for valid inputs
    if not book or not findWord:
        return 0

    wordFreq = {}

    for word in book:
        word = word.lower()

        if word in wordFreq:
            wordFreq[word] += 1
        else:
            wordFreq[word] = 1

    return wordFreq[findWord] if findWord in wordFreq else 0

print(wordFrequency(['Hello', 'World'], 'hello'))