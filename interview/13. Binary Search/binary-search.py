# https://leetcode.com/problems/binary-search

import bisect

def search(nums, target):
    try:
        return nums.index(target)
    except ValueError:
        return -1
    
    
def binary_search(nums, target):
    def recursive(l, r):
        if l <= r:
            mid = (l+r)//2
            
            if nums[mid] < target:
                return recursive(mid+1, r)
            elif nums[mid] > target:
                return recursive(l, mid-1)
            else:
                return mid
        else:
            return -1
    return recursive(0, len(nums)-1)


def b_l(nums, target):
    idx = bisect.bisect_left(nums, target)
    if idx < len(nums) and nums[idx]==target:
        return idx
    else:
        return -1
    