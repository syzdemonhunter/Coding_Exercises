# https://leetcode.com/problems/binary-tree-level-order-traversal/
# T: O(n)
# S: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result, q = [], [root]
        while q:
            q_len = len(q)
            i = 0
            tmp_result = []
            
            while i < q_len:
                node = q.pop(0)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                tmp_result.append(node.val)
                i += 1
            result.append(tmp_result)
            
        return result
        
        