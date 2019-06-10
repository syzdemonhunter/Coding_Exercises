# https://leetcode.com/problems/closest-binary-search-tree-value/
# > 类型：DFS遍历 | 分制
# > Time Complexity O(N)
# > Space Complexity O(1)

# DFS中序遍历
# In-Order走一遍，因为BST的性质，In-Order扫描出来的顺序是上升有序，然后比较当前的root.val。这种方法比较无脑。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.result = float('inf')
        
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root:
            return None
        self.closestValue(root.left, target)
        if abs(root.val - target) < abs(self.result - target):
            self.result = root.val
        self.closestValue(root.right, target)
        return self.result
        
        