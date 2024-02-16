# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
prices = [7,6,4,3,1]


def buy_and_sell_stock(prices):
    buy_price = prices[0]
    max_profit = 0
    for price in prices:
        current_profit = price - buy_price
        if current_profit > max_profit:
            max_profit = max(max_profit, current_profit)
        if current_profit < 0:
            buy_price = price

    return max_profit


print(buy_and_sell_stock(prices))
