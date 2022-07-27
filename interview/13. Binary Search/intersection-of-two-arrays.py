# https://leetcode.com/problems/intersection-of-two-arrays/

def intersection(nums1, nums2):
    n1, n2 = set(nums1), set(nums2)
    return n1-(n1-n2) if len(n1) > len(n2) else n2-(n2-n1)
            