# https://leetcode.com/problems/kth-largest-element-in-an-array/submissions/

def findKthLargest(nums, k: int) -> int:
    nums.sort(reverse=True)
    return nums[k-1]