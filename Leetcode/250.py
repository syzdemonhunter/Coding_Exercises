# https://leetcode.com/problems/count-univalue-subtrees/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count
    
     # bottom-up, first check the leaf nodes and count them, 
    # then go up, if both children are "True" and root.val is 
    # equal to both children's values if exist, then root node
    # is uniValue suntree node.
    
    def dfs(self, root):
        if not root:
            return True
        l, r = self.dfs(root.left), self.dfs(root.right)
        if l and r and (not root.left or root.left.val == root.val) and\
        (not root.right or root.right.val == root.val):
            self.count += 1
            return True
        return False