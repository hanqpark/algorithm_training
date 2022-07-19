# https://leetcode.com/problems/minimum-distance-between-bst-nodes

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        minimum: int = 100001
        dq = deque([root])
        while dq:
            node = dq.popleft()
            left = node.left
            if left:
                minimum = min(minimum, node.val-left.val)
                dq.append(left)
            right = node.right
            if right:
                minimum = min(minimum, right.val-node.val)
                dq.append(right)
        return minimum
    

if __name__ == "__main__":
    root = TreeNode(90)
    root.left = TreeNode(69)
    root.left.left = TreeNode(49)
    root.left.right = TreeNode(89)
    root.left.left.right = TreeNode(52)
    
    sol = Solution()
    res = sol.minDiffInBST(root)
    print(res)
    
    
    
    
    