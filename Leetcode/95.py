# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
T: O(n)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        result = [None]*(n + 1)
        result[0] = []
        if n == 0:
            return result[0]
        result[0].append(None)
        for i in range(1, n + 1):
            result[i] = []
            for j in range(i):
                for left in result[j]:
                    for right in result[i - j - 1]:
                        root = TreeNode(j + 1)
                        root.left = left
                        root.right = self.clone(right, j + 1)
                        result[i].append(root)
                        
        return result[n]
    
    def clone(self, root, k):
        if not root:
            return root
        cur = TreeNode(root.val + k)
        cur.left = self.clone(root.left, k)
        cur.right = self.clone(root.right, k)
        return cur
"""
# T: O(n)

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n == 0:
            return []
        return self.dfs(1, n)
        
    def dfs(self, start, end):
        path = []
        if start > end:
            path.append(None)
        for idx in range(start, end + 1):
            left_list = self.dfs(start, idx - 1)
            right_list = self.dfs(idx + 1, end)
            for left in left_list:
                for right in right_list:
                    root = TreeNode(idx)
                    root.left = left
                    root.right = right
                    path.append(root)
                    
        return path
            
            
            
        
        
                
        