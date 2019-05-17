# https://leetcode.com/problems/partition-list/
# T: O(n)
# S: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return head
        smaller, bigger = ListNode(0), ListNode(0)
        ps, pg = smaller, bigger
        cur = head
        while cur:
            if cur.val < x:
                ps.next = cur
                ps = ps.next
            else:
                pg.next = cur
                pg = pg.next
            cur = cur.next
            
        ps.next = bigger.next
        pg.next = None
        return smaller.next
            
        