# https://leetcode.com/problems/boundary-of-binary-tree/
# 最简单直接的思路就是进行三次DFS, 分别把左边界, 叶子, 右边界放到答案序列中.

# 左边界: 从根的左子节点开始, 优先向左, 没有左子节点就向右, 直到叶子节点, 沿路的所有节点放入答案序列
# 叶子节点: 遍历整棵树, 为了保证逆时针顺序, 需要先访问左子节点, 碰到叶子就放入答案序列
# 右边界: 与左边界类似, 只不过将节点放入答案序列的时机要延后 -- 在递归结束时放入



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        if not root.left and not root.right:
            return [root.val]
        
        left_b = self.find_left(root.left)
        leaves = self.find_leaves(root)
        right_b = self.find_right(root.right)
        
        if left_b and leaves and left_b[-1] == leaves[0]:
            leaves = leaves[1:]
        if leaves and right_b and leaves[-1] == right_b[-1]:
            leaves = leaves[:-1]
        return [root.val] + left_b + leaves + list(reversed(right_b))
    
    def find_leaves(self, root):
        stack = [root]
        leaves = []
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                leaves.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return leaves
    
    def find_left(self, root):
        left_b = []
        while root:
            left_b.append(root.val)
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                break
        return left_b
    
    def find_right(self, root):
        right_b = []
        while root:
            right_b.append(root.val)
            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            else:
                break
        return right_b