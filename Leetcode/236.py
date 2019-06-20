# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path, q_path = [], []
        self.dfs(root, p, p_path)
        self.dfs(root, q, q_path)
        length = min(len(p_path), len(q_path))
        i = 0
        while i < length and p_path[i] == q_path[i]:
            i += 1
        return p_path[i-1]
    
    def dfs(self, root, node, path):
        if not root:
            return False
        path.append(root)
        if root == node:
            return True
        ret = self.dfs(root.left, node, path) or self.dfs(root.right, node, path)
        if ret:
            return True
        last = path[-1]
        path.remove(last)
        return False
        