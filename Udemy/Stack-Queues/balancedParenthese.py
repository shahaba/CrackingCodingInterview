# check if an input string is has a balanced set of parentheses
def balanceCheck(s):

    # edge case check: if there is an uneven num of elements
    if len(s) % 2 != 0:
        return False

    # create stack using list
    stack = []

    # create matching pairs using a hash table
    pairs = {'{':'}', '(':')', '[':']'}

    for paren in s:

        if paren in pairs:
            stack.append(paren)
        elif (stack != [] and pairs[stack.pop()] != paren):
            return False

    return True

paren = '([{}])'
print(balanceCheck(paren))
