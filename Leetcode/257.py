# https://leetcode.com/problems/binary-tree-paths/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# > 类型：DFS遍历 | 分制
# > Time Complexity O(n)
# > Space Complexity O(1)

# DFS遍历
# 这里利用str是immutable的特性，不需要考虑每次backtrack时候对temp数组的更改。

# 如果没有左右孩子：将temp存入返回数组res


class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        result = []
        self.dfs(root, result, '')
        return result
    
    def dfs(self, root, result, tmp):
        tmp += str(root.val)
        if not root.left and not root.right:
            result.append(tmp)
        if root.left:
            self.dfs(root.left, result, tmp + '->')
        if root.right:
            self.dfs(root.right, result, tmp + '->')
        