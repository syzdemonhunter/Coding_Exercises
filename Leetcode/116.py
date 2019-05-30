# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
#O(1) memory+ O(n) time
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
        if not root:
            return None
        
        cur, level_start = root, root.left
        while level_start:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
                cur = cur.next
            else:
                cur = level_start
                level_start = level_start.left
                
        return root