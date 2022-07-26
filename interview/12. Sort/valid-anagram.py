# https://leetcode.com/problems/valid-anagram

from collections import Counter

def isAnagram(s, t):
    # return sorted(list(s)) == sorted(list(t))
    return Counter(s) == Counter(t)