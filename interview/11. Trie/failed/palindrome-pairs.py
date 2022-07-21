# https://leetcode.com/problems/palindrome-pairs/
# 쉽지 않은 문자열(트라이) 문제... 깔끔하게 포기!

class Solution:
    def bruteforce(self, words: List[str]) -> List[List[int]]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i==j: continue
                coin = words[i]+words[j]
                if coin == "".join(reversed(list(coin))):
                    ans.append([i, j])
        return ans