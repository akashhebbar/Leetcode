prices = [7, 6, 4, 3, 1]
buy = prices[0]
maxi = 0
for i in range(1, len(prices)):
    sell = prices[i] - buy
    if sell > buy:
        maxi = max(maxi, sell)
    else:
        buy = prices[i]

print(maxi)
