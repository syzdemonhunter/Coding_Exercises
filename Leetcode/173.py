# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        self.helper(root)

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        n = self.stack.pop()
        self.helper(n.right)
        return n.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if self.stack == []:
            return False
        else:
            return True
        
    def helper(self, root):
        while root != None:
            self.stack.append(root)
            root = root.left
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()