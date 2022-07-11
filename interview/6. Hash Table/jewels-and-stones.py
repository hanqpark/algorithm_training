# https://leetcode.com/problems/jewels-and-stones/

import collections

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        table = collections.Counter(stones)
        res = 0
        for k, v in table.items():
            if k in jewels:
                res += v
        return res
    
class Solution_4:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum([s in jewels for s in stones])