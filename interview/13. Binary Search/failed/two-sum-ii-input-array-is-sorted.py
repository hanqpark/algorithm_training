# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
import bisect

def sol(nums, target):
    l, r = 0, len(nums)-1
    while l != r:
        if nums[l]+nums[r] < target:
            l += 1
        elif nums[l]+nums[r] < target:
            r -= 1
        else:
            return l+1, r+1

def twoSum(numbers, target):
    for i, num in enumerate(numbers):
        expected = target-num
        idx = bisect.bisect_left(numbers, expected, i+1)
        if idx < len(numbers) and numbers[idx]==expected:
            return i+1, idx+1