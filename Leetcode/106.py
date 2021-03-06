# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
    3
   / \
  9  20
    /  \
   15   7

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
'''

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder:
            return None
        if not postorder:
            return None
        in_pos = {}
        for i in range(len(inorder)):
            in_pos[inorder[i]] = i
        return self.dfs(postorder, 0, len(postorder) - 1, 0, in_pos)
                
    def dfs(self, post, post_start, post_end, in_start, in_pos):
        if post_start > post_end:
            return None
        root = TreeNode(post[post_end])
        root_idx = in_pos[post[post_end]]
        left_len = root_idx - in_start
        root.left = self.dfs(post, post_start, post_start + left_len - 1, in_start, in_pos)
        root.right = self.dfs(post, post_start + left_len, post_end - 1, root_idx + 1, in_pos)
        return root
    
        
        