# https://leetcode.com/problems/binary-tree-right-side-view/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = []
        self.helper(result, root, 0)
        return result
    
    def helper(self, result, root, level):
        if not root:
            return
        if len(result) == level:
            result.append(root.val)
        self.helper(result, root.right, level + 1)
        self.helper(result, root.left, level + 1)
'''
# T: O(n)
# S: O(n)

import collections

class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        result = []
        q = collections.deque([root])
        while q:
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                if i == 0:
                    result.append(cur.val)
                if cur.right:
                    q.append(cur.right)
                if cur.left:
                    q.append(cur.left)
                    
        return result

