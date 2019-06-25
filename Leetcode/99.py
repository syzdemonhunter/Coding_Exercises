# https://leetcode.com/problems/recover-binary-search-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(-sys.maxsize-1)
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.helper(root)
        self.first.val, self.second.val = self.second.val, self.first.val
        
    def helper(self, root):
        if not root:
            return
        
        self.helper(root.left)
        if self.prev and self.prev.val >= root.val:
            if not self.first:
                self.first = self.prev
            self.second = root
            
        self.prev = root
        self.helper(root.right)
'''
class Solution:
    def __init__(self):
        self.first = None
        self.second = None
        self.prev = TreeNode(-sys.maxsize-1)
        
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        cur = root
        stack = []
        while stack or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                if self.prev and cur.val <= self.prev.val:
                    if not self.first:
                        self.first = self.prev
                    self.second = cur
                    
                self.prev = cur
                cur = cur.right
                
        self.first.val, self.second.val = self.second.val, self.first.val
            
    