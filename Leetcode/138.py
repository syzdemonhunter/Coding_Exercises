# https://leetcode.com/problems/copy-list-with-random-pointer/
# T: O(n)
# S: O(n)


"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        
        map_table = {}
        cp = Node(head.val, None, None)
        p = head.next
        q = cp
        map_table[head] = cp
        while p:
            q.next = Node(p.val, None, None)
            map_table[p] = q.next
            p = p.next
            q = q.next
            
        h = head
        i = cp
        while h:
            if h.random:
                i.random = map_table[h.random]
            h = h.next
            i = i.next
            
        return cp
        