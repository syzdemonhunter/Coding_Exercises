# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# T: O(n)
# S: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result, q = [], [root]
        while len(q) > 0:
            level_result = []
            q_len = len(q)
            for i in range(q_len):
                node = q.pop(0)
                level_result.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            result.append(level_result)
            
        result.reverse()
        return result