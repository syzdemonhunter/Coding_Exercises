# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
# T: O(n)
# S: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
'''
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return
        if root.left:
            root.left.next = root.right
        if root.next and root.right:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root
'''
# T: O(n)
# S: O(1)

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        start = root
        while start:
            cur = start
            while cur:
                if cur.left:
                    cur.left.next = cur.right
                if cur.right and cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            start = start.left
            
        return root
                
                    
                    
        

            
        

            
        