# brute force solution
def listProductsBrute(lst):
    prodSoFar = [1] * len(lst)

    for i, val in enumerate(lst):
        for j, val in enumerate(lst):
            if j != i:
                prodSoFar[i] *= val

    return prodSoFar

# optimized solution
def listProductsOpt(lst):

    prodSoFar = [0] * len(lst)
    currProd = 1

    for index, val in enumerate(lst):
        prodSoFar[index] = currProd
        currProd *= val

    currProd = 1

    for i in range(len(lst)-1, -1, -1):
        prodSoFar[i] *= currProd
        currProd *= lst[i]

    return prodSoFar


lst = [1, 7, 5, 6, 10, 2, 0]
print(listProductsOpt(lst))
print(listProductsBrute(lst))