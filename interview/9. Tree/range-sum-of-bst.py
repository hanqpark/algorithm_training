# https://leetcode.com/problems/range-sum-of-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def dfs(root):
            if not root: return 0
            dfs(root.left)
            dfs(root.right)
            if root.val >= low and root.val <= high:
                ans.append(root.val)
        dfs(root)
        return sum(ans)