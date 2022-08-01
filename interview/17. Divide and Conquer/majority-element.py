# https://leetcode.com/problems/majority-element

from collections import Counter

def sol(nums):
    counter = Counter(nums)
    for k, v in counter.items():
        if v > len(nums)//2:
            return k