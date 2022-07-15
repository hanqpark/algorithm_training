# https://leetcode.com/problems/letter-combinations-of-a-phone-number

import collections
from typing import List

class MySolution:
    def letterCombinations(self, digits: str) -> List[str]:
        graph = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        res = collections.deque()
        for d in digits:
            if not res:
                res.extend(graph[int(d)])
            else:
                for _ in range(len(res)):
                    temp = res.popleft()
                    for a in graph[int(d)]:
                        res.append(temp+a)
        return res
                    

class Solution:
    def letterCombinations(self, digits: dict) -> List[str]:
        def dfs(idx, path):
            if len(path)==len(digits):
                res.append(path)
                return
            
            for i in range(idx, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path+j)
                    
        if not digits:
            return []
        
        dic = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z'],
        }
        res = []
        dfs(0, "")
        
        return res
            