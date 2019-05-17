# https://leetcode.com/problems/path-sum-ii/
# T: O(n)
# S: O(n)


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, t, val, elem, result):
        if not t:
            return
        elem.append(t.val)
        if val == t.val and not t.left and not t.right:
            result.append(elem[:])
        self.dfs(t.left, val - t.val, elem, result)
        self.dfs(t.right, val - t.val, elem, result)
        elem.pop()
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        self.dfs(root, sum, [], result)
        return result