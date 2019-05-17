# https://leetcode.com/problems/subtree-of-another-tree/
# T: O(m + n)
# S: O(m + n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def compute_hash(self, t):
        if not t:
            return '#'
        left = self.compute_hash(t.left)
        right = self.compute_hash(t.right)
        hash_value = left + right + str(t.val)
        self.tree_dict[t] = hash(hash_value)
        return hash_value
    
    def isSubtreeHelper(self, s, t):
        if not t:
            return True
        if not s:
            return False
        return (self.tree_dict[t] == self.tree_dict[s]) or \
               (self.isSubtreeHelper(s.left, t)) or \
               (self.isSubtreeHelper(s.right, t))
    
    
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        self.tree_dict = {}
        self.compute_hash(s)
        self.compute_hash(t)
        return self.isSubtreeHelper(s, t)