# https://leetcode.com/problems/path-sum-iii/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def dfs(self, root, cur, sum, prefix):
        if not root:
            return 0
        cur += root.val
        cnt = prefix.get(cur - sum, 0)
        if cur not in prefix:
            prefix[cur] = 1
        else:
            prefix[cur] += 1
        cnt += self.dfs(root.left, cur, sum, prefix)
        cnt += self.dfs(root.right, cur, sum, prefix)
        prefix[cur] -= 1
        return cnt
    
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        prefix = {0:1}
        return self.dfs(root, 0, sum, prefix)
        