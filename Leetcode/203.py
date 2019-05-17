# https://leetcode.com/problems/remove-linked-list-elements/
# T: O(n)
# S: O(1)


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        p = dummy
        
        while p.next:
            if p.next.val == val:
                p.next = p.next.next
            else:
                p = p.next
                
        return dummy.next