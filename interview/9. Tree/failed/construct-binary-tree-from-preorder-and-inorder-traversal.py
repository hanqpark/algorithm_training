# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildTree(preorder, inorder):
    if inorder:
        idx = inorder.index(preorder.popleft())
        
        node = TreeNode(inorder[idx])
        node.left = buildTree(preorder, inorder[:idx])
        node.right = buildTree(preorder, inorder[idx+1:])
        
        return node
    
    
if __name__ == "__main__":
    preorder = deque([1,2,4,5,3,6,7,9,8])
    inorder = [4,2,5,1,7,9,6,8,3]
    res = buildTree(preorder, inorder)
    print(res)