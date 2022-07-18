# https://leetcode.com/problems/maximum-depth-of-binary-tree/

# Definition for a binary tree node.

from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        dq = deque([root])
        depth = 0
        
        while dq:
            depth += 1
            for _ in range(len(dq)):
                cur_root = dq.popleft()
                if cur_root.left:
                    dq.append(cur_root.left)
                if cur_root.right:
                    dq.append(cur_root.right)
        
        return depth

if __name__ == "__main__":
    