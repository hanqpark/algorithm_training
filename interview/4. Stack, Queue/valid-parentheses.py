# https://leetcode.com/problems/valid-parentheses

import collections

class Solution:
    def isValid(self, s: str) -> bool:
        dq = collections.deque()
        pair = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for p in s:
            if p in pair.values():
                dq.append(p)
            else:
                if dq and dq[-1] == pair.get(p):
                    dq.pop()
                else:
                    return False     
        if dq: return False
        return True