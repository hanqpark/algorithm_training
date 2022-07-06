# https://leetcode.com/problems/product-of-array-except-self

nums = [1,2,3,4]
res = []
p = 1

for i in range(0, len(nums)):
    res.append(p)
    p *= nums[i]
p=1

for i in range(len(nums)-1, 0-1, -1):
    res[i] = res[i]*p
    p *= nums[i]
print(res)