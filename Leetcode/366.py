# https://leetcode.com/problems/find-leaves-of-binary-tree/
# > 类型：DFS分制
# > Time Complexity O(N)
# > Space Complexity O(N)
# 利用分制，每次bottom up的时候返回当前叶子节点的高度，然后在相对应的全球数组里面开辟数组，并且往里面增值。

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        self.result = []
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        height = max(left, right) + 1
        
        if len(self.result) < height:
            self.result.append([])
        self.result[height - 1].append(root.val)
        return height
        
        