# https://leetcode.com/problems/maximum-subarray/

def sol(nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1] if nums[i-1] > 0 else 0
    return max(nums)

if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = sol(nums)
    print(res)