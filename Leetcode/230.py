# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
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
        self.count = 0
        self.result = 0
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.count = k
        self.helper(root)
        return self.result
    
    def helper(self, root):
        if not root:
            return 
        self.helper(root.left)
        self.count -= 1
        if self.count == 0:
            self.result = root.val
        self.helper(root.right)
        
        