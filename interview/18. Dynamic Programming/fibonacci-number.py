# https://leetcode.com/problems/fibonacci-number

def recursive(n):
    if n < 2:
        return n
    else:
        return recursive(n-1) + recursive(n-2)
    

def memoization(n):
    dp = [0,1]
    if n < 2: return n
    for i in range(2, n):
        dp.append(dp[i-2]+dp[i-1])
    return dp[n]