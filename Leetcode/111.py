# https://leetcode.com/problems/minimum-depth-of-binary-tree/
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        queue = []
        queue.append(root)
        depth = 1
        
        while len(queue) > 0:
            length = len(queue)
            for i in range(length):
                q = queue.pop(0)
                if not q.left and not q.right:
                    return depth
                if q.left:
                    queue.append(q.left)
                if q.right:
                    queue.append(q.right)     
            depth += 1
        