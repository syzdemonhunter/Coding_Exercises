# https://leetcode.com/problems/find-leaves-of-binary-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.helper(result, root)
        return result
    
    def helper(self, result, root):
        if not root:
            return -1
        
        left = self.helper(result, root.left)
        right = self.helper(result, root.right)
        level = max(left, right) + 1
        
        if len(result) == level:
            result.append([])
        result[level].append(root.val)
        
        root.left = None
        root.right = None
        return level
        