# https://leetcode.com/problems/same-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        stack = []
        stack.append(p)
        stack.append(q)
        
        while len(stack) > 0:
            node_p = stack.pop()
            node_q = stack.pop()
            
            if (not node_p) and (not node_q):
                continue
            if (not node_p) or (not node_q):
                return False
            if node_p.val == node_q.val:
                stack.append(node_p.left)
                stack.append(node_q.left)
                stack.append(node_p.right)
                stack.append(node_q.right)
            else:
                return False
            
        return True
        
        