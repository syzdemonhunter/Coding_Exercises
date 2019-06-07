# https://leetcode.com/problems/largest-bst-subtree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class SubTree:
    def __init__(self, largest, n, min_val, max_val):
        self.largest = largest          # largest BST
        self.n = n                      # number of nodes in this ST
        self.min_val = min_val          # min val in this ST
        self.max_val = max_val          # max val in this ST
        

class Solution:

    def largestBSTSubtree(self, root: TreeNode) -> int:
        res = self.dfs(root)
        return res.largest
    
    def dfs(self, root):
        if not root:
            return SubTree(0, 0, float('inf'), float('-inf'))
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        if root.val > left.max_val and root.val < right.min_val:  # valid BST
            n = left.n + right.n + 1
        else:
            n = float('-inf')
            
        largest = max(left.largest, right.largest, n)
        return SubTree(largest, n, min(left.min_val, root.val), max(right.max_val, root.val))
        