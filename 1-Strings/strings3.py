# Replace all spaces with %20 in a URL
# Ex. 'Mr John  Smith    '
# To Mr%20John%Smith
import re


def replaceSpacesBI(string):

    return '%20'.join(string.strip().split())


def replaceSpacesRe(string):

    return '%20'.join(re.split('\s+', string.strip()))


case1 = 'Mr  John   Smith     '
print(replaceSpaces(case1))
print(replaceSpacesRe(case1))
