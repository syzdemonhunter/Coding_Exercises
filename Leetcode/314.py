# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# 这道题看似诡异，但是很重要
# T: O(n)
# S: O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution:
    def __init__(self):
        self.min_val = 0
        self.max_val = 0
        
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        self.helper(root, 0)
        for i in range(self.min_val, self.max_val + 1):
            result.append([])
            
        q = collections.deque([root])
        index = collections.deque([-self.min_val])
        while q:
            cur = q.popleft()
            idx = index.popleft()
            result[idx].append(cur.val)
            if cur.left:
                q.append(cur.left)
                index.append(idx - 1)
            if cur.right:
                q.append(cur.right)
                index.append(idx + 1)
                
        return result
        
    def helper(self, root, idx):
        if not root:
            return
        
        self.min_val = min(self.min_val, idx)
        self.max_val = max(self.max_val, idx)
        self.helper(root.left, idx - 1)
        self.helper(root.right, idx + 1)
        