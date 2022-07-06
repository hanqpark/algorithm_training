# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

import sys

prices = [7,6,4,3,1]
profit = 0
min_price = sys.maxsize

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price-min_price)
print(profit) 