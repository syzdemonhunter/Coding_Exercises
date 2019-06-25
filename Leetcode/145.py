# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
# T: O(n)
# S: O(n)

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        self.helper(result, root)
        return result
    
    def helper(self, result, root):
        if not root:
            return
        self.helper(result, root.left)
        self.helper(result, root.right)
        result.append(root.val)
'''
# T: O(n)
# S: O(n)
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result, stack = [], [root]
        while stack:
            cur = stack.pop()
            result.insert(0, cur.val)
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
                
        return result
            
        