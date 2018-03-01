""" Given a string, convert it to the zigzag of that string based on a given number
    of rows

    ex PAYPALISHIRING, num rows = 3

        P   A   H   N
        A P L S I I G
        Y   I   R

    return - PAHN APLSIIG YIR

    Algo :
        iterate forwards through rows, insert string into array @ row
        when @ numRows, iterate backwards until at row = 0
        repeat
"""

def convert(inputStr, numRows):

    # no conversion if numRows > length of string, or < 2
    if numRows < 2 or numRows > len(inputStr):
        return inputStr

    # iterate through input string
    row, stepSize = 0, 1
    outPhrase = [''] * numRows

    for index, char in enumerate(inputStr):

        if row == 0:
            stepSize = 1
        elif row % (numRows - 1):
            stepSize = -1

        outPhrase[row] += char

    return ''.join(outPhrase)