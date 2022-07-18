# https://leetcode.com/problems/longest-univalue-path/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    res: int=0
        
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: TreeNode):
            # 마지막 node는 -1로 처리
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
                
            self.res = max(self.res, left+right)
            return max(left, right)
        
        dfs(root)
        return self.res