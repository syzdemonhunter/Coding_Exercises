# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# T: O(n)
# S: O(1)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        dummy = ListNode(0)
        dummy.next = head
        fast, slow = dummy, dummy
        while n > 0 and fast.next:
            fast = fast.next
            n -= 1
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next