# https://leetcode.com/problems/sort-list/
# T: O(log(n))
# S: O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def merge_two_lists(self, l1, l2):
        dummy = ListNode(0)
        p = dummy
        
        while l1 and l2:
            if l1.val >= l2.val:
                p.next = l2
                l2 = l2.next
            else:
                p.next = l1
                l1 = l1.next
            p = p.next
            
        if l1:
            p.next = l1
        if l2:
            p.next = l2
        return dummy.next
    
    def _mergesort(self, head):
        if not head or not head.next:
            return head
        fast, slow = head, head
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
        right = self._mergesort(slow.next)
        slow.next = None
        left = self._mergesort(head)
        return self.merge_two_lists(left, right)
        
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self._mergesort(head)