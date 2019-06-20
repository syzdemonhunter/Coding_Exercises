# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# T: O(n)
# S: O(1)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        head, pre, cur = None, None, root
        while cur:
            while cur:
                if cur.left:
                    if pre:
                        pre.next = cur.left
                    else:
                        head = cur.left
                    pre = cur.left
                    
                if cur.right:
                    if pre:
                        pre.next = cur.right
                    else:
                        head = cur.right
                    pre = cur.right
                cur = cur.next
            cur = head
            pre = None
            head = None
        return root