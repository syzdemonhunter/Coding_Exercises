# https://leetcode.com/problems/validate-binary-search-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.helper(root, None, None)
    
    def helper(self, root, lower, upper):
        if not root:
            return True
        if lower and root.val <= lower.val:
            return False
        if upper and root.val >= upper.val:
            return False
        return self.helper(root.left, lower, root) \
           and self.helper(root.right, root, upper) 
        
        