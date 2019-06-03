# https://leetcode.com/problems/closest-leaf-in-a-binary-tree/

# > 类型：DFS遍历树 + BFS遍历图
# > Time Complexity O(N)
# > Space Complexity O(N)


# 这道题对指定的target k和叶子节点的定义可以理解是一个无向图里面找寻k节点最近的邻居(这个邻居要满足是叶子节点的条件)

# 有了以上思路，先Preorder扫一遍Tree，然后创建一个图，具体参考子方程dfs，期间记住存储以下叶子节点，方便与之后处理邻居满足叶子节点这一返回条件

# 当图建立好了以后，在图里面进行遍历，如果找到的邻居也满足叶子条件的话，返回即可。




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Solution:
    def findClosestLeaf(self, root: TreeNode, k: int) -> int:
        self.res = None
        self.dic, self.leaves = collections.defaultdict(list), set()
        self.dfs(root)   
        self.bfs(k)
        return self.res

    def dfs(self, root):
        '''Preorder through the Tree and construct graph'''
        if not root: return
        if not root.left and not root.right:
            self.leaves.add(root.val)
            return
        if root.left:
            self.dic[root.val].append(root.left.val)
            self.dic[root.left.val].append(root.val)
            self.dfs(root.left)
        if root.right:
            self.dic[root.val].append(root.right.val)
            self.dic[root.right.val].append(root.val)
            self.dfs(root.right)
    
    def bfs(self, k):
        '''Find the closest neighbor of k that is also a leaf'''
        q = [k]
        while q:
            new_q = []
            for node in q:
                if node in self.leaves:
                    self.res = node
                    return
                new_q += self.dic.pop(node, [])
            q = new_q