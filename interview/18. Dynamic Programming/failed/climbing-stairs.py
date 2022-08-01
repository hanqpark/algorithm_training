# https://leetcode.com/problems/climbing-stairs/

from collections import defaultdict

class Solution:
    dp = defaultdict(int)
    def climbStairs(self, n: int) -> int:
        if n <= 2: return n
        if self.dp[n]: return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]

# n = 38일때 TLE 뜸
def recursive(n):
    if n == 1: return 1
    elif n == 2: return 2
    else:
        return recursive(n-1) + recursive(n-2)