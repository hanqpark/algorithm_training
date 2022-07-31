# https://leetcode.com/problems/minimum-window-substring/

from collections import Counter

class Solution:
    def minWindow(self, s, t):
        need = Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right-left <= end-start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1
        return s[start:end]
                    
    
    
    def counter_sol(self, s: str, t: str) -> str:
        t_cnt = Counter(t)
        c_cnt = Counter()
        
        stt = float('-inf')
        end = float('inf')
        
        l = 0
        for r, c in enumerate(s, 1):
            c_cnt[c] += 1
            
            while c_cnt & t_cnt == t_cnt:
                if r-l < end-stt:
                    stt, end = l, r
                c_cnt[s[l]] -= 1
                l += 1
        return s[stt:end] if end-stt <= len(s) else ""
    

if __name__ == "__main__":
    sol = Solution()
    res = sol.minWindow("ADOBECODEBANC", "ABC")
    print(res)