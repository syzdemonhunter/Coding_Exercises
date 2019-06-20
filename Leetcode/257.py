# https://leetcode.com/problems/binary-tree-paths/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = []
        self.dfs(result, root, '')
        return result
    
    def dfs(self, result, root, path):
        if not root.left and not root.right:
            result.append(path + str(root.val))
        if root.left:
            self.dfs(result, root.left, path + str(root.val) + '->')
        if root.right:
            self.dfs(result, root.right, path + str(root.val) + '->')
        
        