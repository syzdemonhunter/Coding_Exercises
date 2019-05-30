# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
# O(1) space and O(n) Time complexity

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
        head, prev, curr = root, None, None
        while head:
            curr = head
            prev = None
            head = None
            while curr:
                if curr.left:
                    if prev:
                        prev.next = curr.left
                    else:
                        head = curr.left
                    prev = curr.left
                if curr.right:
                    if prev:
                        prev.next = curr.right
                    else:
                        head = curr.right
                    prev = curr.right
                curr = curr.next
        return root
        
        