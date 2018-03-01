# Number Swapper: Write a function to swap a number in place (i.e. withouth a temp variable)

# using algebra trick to swap numbers
def numSwap(a, b):
    a += b
    b = a - b
    a -= b

    return (a, b)

# using bit manipulation ...