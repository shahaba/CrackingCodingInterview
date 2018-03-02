
# brute force algorithm
def maxProfitBrute(stockPrices):

    # need more than 2 stock values to get max profit
    if len(stockPrices) < 2:
        return 0

    profits = maxProfits = 0

    for i in range(len(stockPrices)-1):
        for j in range(i+1, len(stockPrices)):
            profits = stockPrices[j] - stockPrices[i]
            maxProfits = max(profits, maxProfits)

    return maxProfits


# using greedy algorithm
def maxProfitsOpt(stockPrices):

    if len(stockPrices) < 2:
        return 0

    currProfit = maxProfit = stockPrices[1] - stockPrices[0]
    minVal = min(stockPrices[0], stockPrices[1])

    for i in range(1, len(stockPrices)):
        currProfit = stockPrices[i] - minVal
        maxProfit = max(currProfit, maxProfit)
        minVal = min(minVal, stockPrices[i])

    return maxProfit


stockPrices = [10, 15, 5, 7, 1, 0]
print(maxProfitBrute(stockPrices), maxProfitsOpt(stockPrices))