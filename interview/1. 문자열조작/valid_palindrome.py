# https://leetcode.com/problems/valid-palindrome
# 팰린드롬: "같이합창합시다" 같이 뒤집어도 같은 녀석들

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in s if c.isalnum()]   # isalnum -> 문자 or 숫자인지 파악
        res = True if new_s == list(reversed(new_s)) else False
        return res