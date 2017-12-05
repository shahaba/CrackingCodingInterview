# 1.4 Palindrome, check if permutations of string are palindromes
# Ex. Tact Coa
# Output: True (permutations: taco cat, atco cta)


def isPalindromeDS(string):
    if len(string) <= 1:
        return False

    chars = [0 for i in range(26)]

    for i in string:
        index = ord(i) - 97
        chars[index] += 1

    repeated = 0
    for i in chars:
        if i > 0 and i % 2 == 0:
            repeated += i / 2

    req_len = 2*repeated
    if len(string) == req_len or len(string) == req_len + 1:
        return True

    return False


case1 = 'tatt'
print(isPalindromeDS(case1))
