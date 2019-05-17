# https://leetcode.com/problems/path-sum/
# T: O(n)
# S: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        node_stack, sum_stack = [root], [sum]
        while node_stack:
            node = node_stack.pop()
            s = sum_stack.pop()
            
            if not node.left and not node.right and node.val == s:
                return True
            if node.left:
                node_stack.append(node.left)
                sum_stack.append(s - node.val)
            if node.right:
                node_stack.append(node.right)
                sum_stack.append(s - node.val)
                
        return False
        
        