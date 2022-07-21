# https://leetcode.com/problems/minimum-distance-between-bst-nodes

import sys
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
  

# 중위 순회를 이용하여 풀어야 합니다!!!      
class Solution:
    prev = -sys.maxsize
    result = sys.maxsize
    
    def minDiffInBST(self, root):
        if root.left:
            self.minDiffInBST(root.left)
        
        self.result = min(self.result, root.val-self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
            
        return self.result
    
    
    def stack_minDiffInBST(self, root: Optional[TreeNode]) -> int:
            prev = -sys.maxsize
        result = sys.maxsize
        stack = []
        node = root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            result = min(result, node.val-prev)
            prev = node.val
            node = node.right
        return result
    
    
    # 내 풀이는 부모-자식 간의 차이만 고려해서 풀었음...
    def my_minDiffInBST(self, root: Optional[TreeNode]) -> int:
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
    
    
    
    
    