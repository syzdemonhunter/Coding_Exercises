# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.result = 0

    def longestConsecutive(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.helper(root, 0, root.val)
        return self.result
        
    def helper(self, root, max_val, target):
        if not root:
            return
        if root.val == target:
            max_val += 1
        else:
            max_val = 1
        self.result = max(self.result, max_val)
        self.helper(root.left, max_val, root.val + 1)
        self.helper(root.right, max_val, root.val + 1)
        