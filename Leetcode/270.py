# https://cspiration.com/course/video?id=1217

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
# T: O(logn)
# S: O(1)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        result = root.val
        while root:
            if abs(target - root.val) < abs(target - result):
                result = root.val
            if root.val > target:
                root = root.left
            else:
                root = root.right
        return result
'''
# T: O(logn)
# S: O(n)
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.helper(root, target, root.val)
        
    def helper(self, root, target, val):
        if not root:
            return val
        if abs(target - root.val) < abs(target - val):
            val = root.val
        if root.val < target:
            val = self.helper(root.right, target, val)
        elif root.val > target:
            val = self.helper(root.left, target, val)
        return val
            
        