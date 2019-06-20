# https://leetcode.com/problems/path-sum/
# time: O(n)
# space: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
class Solution:
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right:
            return total == root.val
        return self.hasPathSum(root.left, total - root.val) or self.hasPathSum(root.right, total - root.val)
'''
class Solution:
    def hasPathSum(self, root: TreeNode, total: int) -> bool:
        if not root:
            return False
        stack = [root]
        while stack:
            cur = stack.pop()
            if not cur.left and not cur.right:
                if cur.val == total:
                    return True
            if cur.right:
                stack.append(cur.right)
                cur.right.val += cur.val
            if cur.left:
                stack.append(cur.left)
                cur.left.val += cur.val
            
        return False
        
        