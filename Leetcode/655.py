# https://leetcode.com/problems/print-binary-tree/
# https://zxi.mytechroad.com/blog/tree/leetcode-655-print-binary-tree/

# Time complexity: O(m*n)
# Space complexity: O(m*n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        def fill(root, h, l, r):
            if not root:
                return
            mid = (l + r)//2
            m[h][mid] = str(root.val)
            if root.left:
                fill(root.left, h + 1, l, mid - 1)
            if root.right:
                fill(root.right, h + 1, mid + 1, r)
                
        h = height(root)
        w = 2**h - 1
        m = [['']*w for _ in range(h)]
        fill(root, 0, 0, w - 1)
        return m
        
        