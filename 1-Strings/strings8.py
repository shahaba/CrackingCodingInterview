# Zero Matrix, if an element in a NxM matrix is 0, the entire row and column
# are set to 0


def rowZeros(m, arr):
    for i in range(m):
        if arr[i][0] == 0:
            return True
    return False


def colZeros(n, arr):
    for i in range(n):
        if arr[0][i] == 0:
            return True
    return False


def scanMatrix(m, n, arr):
    for i in range(1, m):
        for j in range(1, n):
            if arr[i][j] == 0:
                arr[i][0] = 0
                arr[0][j] = 0


def replaceRow(m, n, arr):
    for i in range(1, m):
        if arr[i][0] == 0:
            for j in range(1, n):
                arr[i][j] = 0


def replaceCol(m, n, arr):
    for i in range(1, n):
        if arr[0][i] == 0:
            for j in range(1, m):
                arr[j][i] = 0


def zeroMatrix(m, n, arr):

    rowHasZero = rowZeros(m, arr)
    colHasZero = colZeros(n, arr)

    scanMatrix(m, n, arr)

    replaceRow(m, n, arr)
    replaceCol(m, n, arr)

    if rowHasZero:
        for i in range(m):
            arr[i][0] = 0

    if colHasZero:
        for i in range(n):
            arr[0][i] = 0


matrix = [[1 for i in range(3)] for i in range(4)]
matrix2 = [[1, 1, 1], [1, 0, 1], [1, 0, 1]]
print(matrix)
zeroMatrix(4, 3, matrix)
print(matrix)
zeroMatrix(3, 3, matrix2)
print(matrix2)
