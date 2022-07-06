# https://leetcode.com/problems/array-partition/

'''
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        res = [nums[i] for i in range(len(nums)) if i%2==0]
        return sum(res)
'''
nums = [1,4,3,2]
print(sum(sorted(nums)[::2]))