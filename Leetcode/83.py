# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# T: O(n)
# S: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        p = head
        q = p.next
        while q:
            if p.val == q.val:
                p.next = q.next
            else:
                p = p.next
            q = q.next
            
        return head
        