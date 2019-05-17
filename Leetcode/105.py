# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, pre, pre_start, pre_end, in_start, in_pos):
        if pre_start > pre_end:
            return None
        root = TreeNode(pre[pre_start])
        root_idx = in_pos[pre[pre_start]]
        left_len = root_idx - in_start
        root.left = self.dfs(pre, pre_start + 1, pre_start + left_len, in_start, in_pos)
        root.right = self.dfs(pre, pre_start + left_len + 1, pre_end, root_idx + 1, in_pos)
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        if not inorder:
            return None
        in_pos = {}
        for i in range(len(preorder)):
            in_pos[inorder[i]] = i
        return self.dfs(preorder, 0, len(preorder) - 1, 0, in_pos)
            