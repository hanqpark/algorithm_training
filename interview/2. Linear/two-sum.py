# https://leetcode.com/problems/two-sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        for i, num in enumerate(nums):
            if target-num in nums_map and i != nums_map[target-num]:
                return [i, nums_map[target-num]]
            

class MySolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp = target - nums[i]
            if temp in nums: 
                temp_idx = nums.index(temp)
                if i != temp_idx:
                    return [i, temp_idx]
            