# https://leetcode.com/problems/count-complete-tree-nodes/
# T: O(logn*logn)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        left = self.left_depth(root)
        right = self.right_depth(root)
        
        if left == right:
            return 2**left - 1 # (2^left - 1)
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right) 
        
    def left_depth(self, root):
        result = 0
        while root:
            root = root.left
            result += 1
        return result
    
    def right_depth(self, root):
        result = 0
        while root:
            root = root.right
            result += 1
        return result
        
        