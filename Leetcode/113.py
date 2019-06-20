# https://leetcode.com/problems/path-sum-ii/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        if not root:
            return []
        result = []
        self.helper(result, [], root, total)
        return result
    
    def helper(self, result, path, root, total):
        if not root:
            return
        path.append(root.val)
        if total == root.val and not root.left and not root.right:
            result.append(path[:])
        self.helper(result, path, root.left, total - root.val)
        self.helper(result, path, root.right, total - root.val)
        path.pop()
        
        
        