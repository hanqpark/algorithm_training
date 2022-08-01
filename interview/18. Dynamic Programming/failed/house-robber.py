# https://leetcode.com/problems/house-robber/submissions/

def recursive(nums):
    def _rob(i):
        if i<0: return 0
        return max(_rob(i-1), _rob(i-2)+nums[i])
    return _rob(len(nums)-1)

def tabulation(n):
    for i in range(len(n)):
        if i+2 < len(n):
            if i-1 >= 0:
                n[i+2] += max(n[i], n[i-1])
            else:
                n[i+2] += n[i]
        else:
            return max(n)