# https://leetcode.com/problems/subsets/

def dfs(idx, path):
    res.append(path)
    
    for i in range(idx, len(nums)):
        dfs(i+1, path+[nums[i]])
    
if __name__ == "__main__":
    nums, res = [1,2,3], []
    dfs(0, [])
    print(res)