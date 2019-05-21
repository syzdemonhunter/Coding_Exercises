# https://leetcode.com/problems/serialize-and-deserialize-bst/
# https://www.youtube.com/watch?v=IDg-vB90gkM&t=107s

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections 

class Codec:
    # recursive function to serialize BST
    # using a pre-order traversal
    # simply stores node values to a list
    def serialize_helper(self, root, preorder):
        if not root:
            return
        preorder.append(str(root.val))
        self.serialize_helper(root.left, preorder)
        self.serialize_helper(root.right, preorder)
        
    # serialize BST to pre-order traversal  
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        preorder = []
        self.serialize_helper(root, preorder)
        return ','.join(preorder)
        
    # recursive function to deserialize BST from preorder queue      
    def deserialize_helper(self, q, max_val):
        # base case: empty queue
        if len(q) == 0:
            return None
        # if the head of the queue is too big
        # then this node is not meant to be placed here
        if int(q[0]) > max_val:
            return None
        # create root node
        root = TreeNode(int(q.popleft()))
        # create left and right subtrees
        root.left = self.deserialize_helper(q, root.val)
        root.right = self.deserialize_helper(q, max_val)
        # return root node
        return root
    
    # deserialize BST pre-order traversal
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # sanity check: empty input be ignored, don't creat queue
        if len(data) == 0:
            return None
        q = collections.deque(data.split(','))
        # the maximum value is infinity
        root = self.deserialize_helper(q, float('inf'))
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))