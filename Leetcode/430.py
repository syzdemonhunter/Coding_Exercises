# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# T: O(n)
# S: O(n)

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: 
            return None
        stack = [head]
        p = None
        while stack:
            r = stack.pop()
            if p:
                p.next, r.prev = r, p
            p = r
            if r.next:
                stack.append(r.next)
            if r.child:
                stack.append(r.child)
                r.child = None
        return head
        