# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii

def solution(prices):
    result = 0
    for i in range(len(prices)-1):
        if prices[i+1] > prices[i]:
            result += prices[i+1]-prices[i]
    return result

def solution2(prices):
    return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices)-1))