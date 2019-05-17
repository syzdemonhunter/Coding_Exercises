# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result, current = [], [root]
        
        while current:
            if len(result) % 2 != 0:
                result.append([n.val for n in current[::-1]])
            else:
                result.append([n.val for n in current])
                
            next_level = []
        
            for n in current:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)

            current = next_level
            
        return result