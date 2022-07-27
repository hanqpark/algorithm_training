# https://leetcode.com/problems/single-number

from collections import Counter

def mysol(nums):
    count = Counter(nums)
    for k,v in count.items():
        if v==1: return k
        
def solution(nums):
    ans = 0
    for n in nums:
        ans ^= n
    return ans


solution([1,4,1,2,2])