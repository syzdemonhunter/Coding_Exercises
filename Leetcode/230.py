# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
# https://www.youtube.com/watch?v=up0CTw38FnY
# 让stack的栈顶保存当前树的最小值。

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
            
        x = 1
        while stack and x <= k:
            n = stack.pop()
            x += 1
            
            w = n.right
            while w:
                stack.append(w)
                w = w.left
                
        return n.val
                