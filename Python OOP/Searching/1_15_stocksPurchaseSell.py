# Find the best time to buy and sell the stocks

# Time Complexity - O(n)
# Space Complexity - O(1)
def bestDayToBuyAndSellStock(arr):
    minIndex, maxIndex, minPrice, maxProfit = 0, 0, float('inf'), float('-inf')

    for i, price in enumerate(arr):
        if price < minPrice:
            minPrice = price
            minIndex = i + 1
        elif price - minPrice > maxProfit:
            maxProfit = price - minPrice
            maxIndex = i + 1

    return minIndex, maxIndex


if __name__ == '__main__':
    arr = [2, 4, 1, 6, 5, 7, 3]

    print 'Stocks:', arr, '\nBest time to buy and sell stock is day %d and %d respectively' % bestDayToBuyAndSellStock(arr)

