# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/
# T: O(n)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        result = []
        def preorder(root):
            if not root:
                result.append('#')
            else:
                result.append(str(root.val))
                preorder(root.left)
                preorder(root.right)
                
        preorder(root)
        return ','.join(result)
                
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        q = collections.deque(data.split(','))
        def build_tree():
            char = q.popleft()
            if char == '#':
                return None
            else:
                node = TreeNode(char)
                node.left = build_tree()
                node.right = build_tree()
            return node
        
        return build_tree()
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))