# https://leetcode.com/problems/diameter-of-binary-tree

from typing import Optional

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    longest: int = 0
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node: TreeNode) -> int:
            # 마지막 node는 -1로 처리
            if not node:
                return -1
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left+right+2)
            return max(left, right) + 1
        
        dfs(root)
        return self.longest
        
if __name__ == "__main__":
    # Tree 생성
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right= TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    sol = Solution()
    res = sol.diameterOfBinaryTree(root)
    print(res)