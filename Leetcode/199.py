# https://leetcode.com/problems/binary-tree-right-side-view/
# https://www.youtube.com/watch?v=f72I2qz9K7k
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        
        result = []
        self.dfs(root, result, 0)
        return result
    
    def dfs(self, root, result, level):
        if not root:
            return
        
        if level == len(result):
            result.append(root.val)
            
        self.dfs(root.right, result, level + 1)
        self.dfs(root.left, result, level + 1)
        
        
        
        
        