# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
# 对于一棵树，我们设其根节点的位置为0。
# 对于任一非叶子节点，若其位置为x，设其左儿子的位置为x-1，右儿子位置为x+1。
# 按照以上规则bfs遍历整棵树统计所有节点的位置，然后按位置从小到大输出所有节点。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections

class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = collections.deque()
        my_dict = collections.defaultdict(list)
        q.append((root, 0))
        
        while q:
            node, x = q.popleft()
            if node:
                my_dict[x].append(node.val)
                q.append((node.left, x - 1))
                q.append((node.right, x + 1))
                
        return [my_dict[i] for i in sorted(my_dict.keys())]
            
        