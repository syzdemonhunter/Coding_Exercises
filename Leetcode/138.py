# https://leetcode.com/problems/copy-list-with-random-pointer/submissions/
# T: O(n)
# S: O(n)

"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        
        dic = {}
        cp = Node(head.val, None, None)
        p = head.next
        q = cp
        dic[head] = cp
        while p:
            q.next = Node(p.val, None, None)
            dic[p] = q.next
            p = p.next
            q = q.next
            
        cur = head
        cp_random = cp
        while cur:
            if cur.random:
                cp_random.random = dic[cur.random]
            cur = cur.next
            cp_random = cp_random.next
        return cp
            
        
            
        
        