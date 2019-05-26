# https://leetcode.com/problems/construct-quad-tree/
# We take topleft point as reference in each considered DFS grid (node) and l as length of its edges.
# If l is 1, we know it is a leaf node.
# Else, it gets its value as boolean XOR of children nodes which are tLeft, tRight, bLeft, bRight
# And it become also as a leaf if all children has same value and all children is also leaf.
# https://www.youtube.com/watch?v=G2bc30jV2pg

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(x, y, l):
            if l == 1:
                node = Node(grid[x][y] == 1, True, None, None, None, None)
            else:
                t_left = dfs(x, y, l // 2)
                t_right = dfs(x, y + l // 2, l // 2)
                b_left = dfs(x + l // 2, y, l// 2)
                b_right = dfs(x + l // 2, y + l // 2, l // 2)
                value = t_left.val or t_right.val or b_left.val or b_right.val
                if t_left.isLeaf and t_right.isLeaf and b_left.isLeaf and b_right.isLeaf \
                and t_left.val == t_right.val == b_left.val == b_right.val:
                    node = Node(value, True, None, None, None, None)
                else:
                    node = Node(value, False, t_left, t_right, b_left, b_right)
            return node
        return grid and dfs(0, 0, len(grid)) or None
                
        